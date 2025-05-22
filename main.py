import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# News-Beispiel: Wird später ersetzt durch Scraping
nachricht = "Die EZB will KI regulieren."

# GPT-Abfrage im Mises-Stil
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Kommentiere wirtschaftliche Nachrichten im Stil von Ludwig von Mises. Sei libertär, kritisch gegenüber Zentralbanken, pro Bitcoin, intelligent, zugespitzt, auf Deutsch und Englisch."
        },
        {
            "role": "user",
            "content": f"Nachricht: {nachricht}"
        }
    ]
)

antwort = response['choices'][0]['message']['content']
print(antwort)
