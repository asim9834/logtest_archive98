import os
import re
import random

# Eğer AI entegrasyonu istenirse bu satırlar aktif edilir:
# import openai
# from dotenv import load_dotenv
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_character_story(name: str, race: str, class_: str, description: str) -> str:
    """
    Basit bir hikaye üretici. İsim, ırk, sınıf ve tanım girdilerinden karakter hikayesi oluşturur.
    Eğer AI kullanılırsa, bu fonksiyon yerine OpenAI çağrısı yapılır.
    """
    intro = f"{name}, bir {race} ırkından ve {class_} sınıfından biri olarak tanınıyor."

    if description:
        intro += f" Geçmişinde: {description}"

    traits = [
        "Cesur yürekli",
        "Kurnaz zekalı",
        "Gizemli bir geçmişe sahip",
        "Sadakatiyle bilinir",
        "Gölge gibi sessiz hareket eden"
    ]

    intro += " " + random.choice(traits) + "."
    return intro

# AI destekli karakter üretimi (şu an devre dışı, ama kolayca aktif edilebilir)
def generate_character_with_ai(name: str, race: str, class_: str, description: str) -> dict:
    """
    Karakter sözlüğü döner. AI ya da basit metinle hikaye üretimi yapılır.
    """

    # Eğer AI kullanılacaksa bu blok aktif edilebilir:
    """
    prompt = f\"\"\"Karakter Adı: {name}
    Irk: {race}
    Sınıf: {class_}
    Geçmiş: {description}

    Bu karakterin detaylı bir hikayesini yaz:
    \"\"\"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sen bir RPG hikaye yazarı AI'sın."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )
    story = response.choices[0].message["content"]
    """

    # Geçici olarak AI devre dışı:
    story = generate_character_story(name, race, class_, description)

    return {
        "name": name,
        "race": race,
        "class": class_,
        "description": description,
        "story": story
    }
