from openai import OpenAI
from dotenv import load_dotenv
import os
import yaml
import tqdm

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


html_data = open("alex.html", "r").read()

yaml_prompts = yaml.safe_load(open("prompts.yaml", "r"))

for prompt in tqdm.tqdm(yaml_prompts.keys()):
    print(yaml_prompts[prompt]["name"])
    print(yaml_prompts[prompt]["prompt"])
    print("-" * 100)

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        max_tokens=32768,
        messages=[
            {"role": "system", "content": yaml_prompts[prompt]["prompt"]},
            {"role": "user", "content": html_data}
        ]
    )

    print(resp.choices[0].message.content)

    with open(f"results/alex_with_guard-{yaml_prompts[prompt]['name']}.html", "w") as f:
        f.write(resp.choices[0].message.content)