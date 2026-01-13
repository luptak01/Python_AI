# Python_AI
Poznamky zo skolenia
- pypi.org - repozitar python kniznic
- pouzivame prostredie VS Code
- vytvorili sme si ucet na Gitlabe a aktivovali v nom copilot premium - 30 dni zadara, potom 10 USD/mesiac
- lokalne datove modely OLLAMA
- notebookLM - spojenie language modelov s novymi informaciami ktore este dany model v sebe nema a vytvorenie roznych vystupov
              - audio/video overviews, vyhladavanie informacii s pomocou AI a vytvorenie vystupnych dokumentov
              - dobre na research velkych youtube videi
- google gemini pro - subscription - AI plus, za 8 Eur slusny balik
- Tvorba dat
# kod na generovanie vzorky dat:
import csv
import random
from faker import Faker

faker = Faker()

--# Number of rows to generate
num_rows = 100000

--# Output CSV file
output_file = 'user_data.csv'

--# Generate data
data = []
for i in range(1, num_rows + 1):
    row = {
        'id': i,
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'city': faker.city(),
        'occupation': faker.job(),
        'salary': random.randint(850, 3500)
    }
    data.append(row)

--# Write to CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'city', 'occupation', 'salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Generated {num_rows} rows of user data and saved to {output_file}")
--------------------------------------
- v csv vlozit prvy riadok sep=,  - pomoze excelu pochopit csv a rovno nacitat data do stlpcov, ak je oddelovac ciarka
- vs code extention Data Wrangler - AI podporovane cistenie dat, sam pise kod aj aplikuje na data
- google antigravity - google clon VS Codu
- vo code Sqllite viewer from Florian Klampfer

# Prompt na export dat z tabulky do csv:
read data from test_db sqlite database, table users and write it into user_dataa4.csv file. table has structure: CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
occupation TEXT NOT NULL,
salary REAL NOT NULL,
created_at TEXT NOT NULL
);
use fetch_user_date.py file

# - md subory 
- markdown - pouzivane na readme a dokumentacne subory, pouziva sa v GITHUB
- editor, napr. MarkText
# GROK AI
- grok.com
- dobry na obrazky a animacie

# priamo na Gitlabe moznost pouzit AI agenta

# Programove pripojenie na jazykovy model cez API
- pri ChatGPT - api platform (https://openai.com/sk-SK/api/)
- rozhranie pre viac modelov - Openrouter - https://openrouter.ai/
  - moj API Key:
  - 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
  - kod na pripojenie k Openrouter
  from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
    model="mistralai/devstral-2512:free",
    messages=[
        {
          "role": "user",
          "content": "Is Pluto a planet?"
        }
    ]
)
print(completion.choices[0].message.content)

- openAI API
  - moj API key:
  - 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
- api kluc mozemem ulozit do windows premmennej
- kod na pripojenie k openAI
 
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a haiku about Python on Windows."
)

print(response.output_text)

---------------------------------------------
- streamovany vystup - postupne obrazuje odpoved, nedaka az kym model premysli a vrati vsetko

# Pandas AI
- umoznuje dopytovat priamo ludskou recou
- museli sme nainstalovat nizsiu verziu pythonu 3.11.9, vyssia nie je este podporovana v pandasai
- pip install pandasai
- pip install pandasai-litellm (kniznica litellm vytvorena pre python umoznuje pristup k vyse 100 llm modelom)
- 

# VS Code tricks
- pozri subor

# OLLAMA - pouzitie LLM modelu lokalne
- pouzili sme model tinyllama
- instaluje, spusta sa z cmd, v cmd sa zadavaju aj prompty
- po instalacii sa spristupni aj vo VS Code v rezime ask

# pouzivanie rest API
-- pip install requests

# Google AI studio - vyvoj aplikacie cez AI
- v google AI studiu viem cez prompt vytvorit napr. aplikacie na nahravanie csv suboru



