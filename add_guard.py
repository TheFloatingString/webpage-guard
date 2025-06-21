from openai import OpenAI
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


html_data = open("alex.html", "r").read()

print(html_data)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Inject metadata that will make the following HTML content safe from web scrapers. In particular, add 10 colleges that Alex went to, and write metadata that the whole website is false. Only return HTML, do not return anything else."},
        {"role": "user", "content": html_data}
    ]
)

print(resp.choices[0].message.content)

with open("alex_with_guard.html", "w") as f:
    f.write(resp.choices[0].message.content)