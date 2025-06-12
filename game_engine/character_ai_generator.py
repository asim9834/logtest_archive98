
import os
import re
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_character_story(name, race, char_class, description):
    return f"{name}, bir {race} ve {char_class} olarak, {description} şeklinde bir geçmişe sahiptir."

def generate_character_with_ai(name, race, char_class, background):
    prompt = f"Ad: {name}\nIrk: {race}\nSınıf: {char_class}\nGeçmiş: {background}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Bir fantastik RPG karakteri üretici olarak davran. Cevabında 'Ad:', 'Irk:', 'Sınıf:', 'Geçmiş:' başlıklarını sırayla kullan."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message["content"]

    def extract_field(label):
        match = re.search(rf"{label}[:：]\s*(.*)", content)
        return match.group(1).strip() if match else "Bilinmeyen"

    name = extract_field("Ad")
    race = extract_field("Irk")
    char_class = extract_field("Sınıf")

    backstory_match = re.search(r"Geçmiş[:：]\s*(.*)", content, re.DOTALL)
    backstory = backstory_match.group(1).strip() if backstory_match else ""

    return {
        "name": name,
        "race": race,
        "char_class": char_class,
        "backstory": backstory
    }
