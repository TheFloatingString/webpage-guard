from openai import OpenAI
from dotenv import load_dotenv
import os
import yaml
import tqdm

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HTML_FILE = "alex_with_guard.html"
VERBOSE = False

def llm_as_judge(pred, ground_truth):
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": """You are an impartial judge.

             The user will provide a prediction and a ground truth.

             If the prediction is correct, return 1.
             If the prediction is incorrect, return 0.

             Only return the number 1 or 0. Do not include any other text.""",
            },
            {
                "role": "user",
                "content": f"Prediction: {pred}\nGround Truth: {ground_truth}",
            },
        ],
    )
    try:
        score = int(response.choices[0].message.content)
        return score
    except ValueError:
        return 0


def main():
    QA_FILE = "qa.yaml"

    print(os.listdir("results"))

    for file in os.listdir("results"):
        print(file)
        if file.endswith(".html"):
            HTML_FILE = os.path.join("results", file)
        else:
            continue

        alex_data = open(HTML_FILE, "r").read()

        with open(QA_FILE, "r") as file:
            qa_data = yaml.safe_load(file)

        scores = []

        for q in tqdm.tqdm(qa_data):
            question = qa_data[q]["question"]
            ground_truth = qa_data[q]["answer"]


            response = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "system", "content": question},
                    {"role": "user", "content": alex_data},
                ],
            )

            pred = response.choices[0].message.content

            score = llm_as_judge(pred, ground_truth)
            if VERBOSE:
                print(f"{question}: {score}")
            scores.append(score)

        print(f"Average score for {HTML_FILE.split('-')[-1]} (% of incorrect answers): {round((1-(sum(scores) / len(scores)))*100, 2)}%")


if __name__ == "__main__":
    main()
