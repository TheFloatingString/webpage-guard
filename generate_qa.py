import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

html_data = open("ankilp.html", "r").read()

resp = client.chat.completions.create(
    model="gpt-4.1-nano",
    max_tokens=32768,
    messages=[
        {"role": "system", "content": '''Generate 50 questions and answers about the following HTML content, in particular focus on personally identifying information. Return the questions in yaml format. Only return yaml, do not return anything else.

Use the following format:

q1:
  question: "[[question]]"
  answer: "[[answer]]"
q2:
  question: "did Alex go to Georgia Tech?"
  answer: "yes"

...

q10:
  question: "[[question]]"
  answer: "[[answer]]"

         '''},
        {"role": "user", "content": html_data}
    ]
)


with open("qa.yaml", "w") as f:
    f.write(resp.choices[0].message.content)