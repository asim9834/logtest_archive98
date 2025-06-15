# game_engine/prebuilt_characters.py

from game_engine.character import Character

# Hazır karakterler
durok = Character(
    name="Durok Steelhammer",
    race="Cüce",
    char_class="Barbar",
    level=1,
    stats={"strength": 16, "dexterity": 10, "constitution": 15, "intelligence": 8, "wisdom": 12, "charisma": 9},
    background="Bir dağ klanında doğdu, ailesi devler tarafından katledildi.",
    personality="Sadık, çabuk sinirlenen",
    abilities=["Reckless Attack", "Rage", "Stone's Endurance"],
    alignment="Kaotik İyi"
)

sylen = Character(
    name="Sylen Varithiel",
    race="Elf",
    char_class="Haydut",
    level=1,
    stats={"strength": 9, "dexterity": 17, "constitution": 11, "intelligence": 12, "wisdom": 13, "charisma": 10},
    background="Kazayla birini öldürdükten sonra yer altına karıştı.",
    personality="Soğukkanlı, gözlemci",
    abilities=["Sneak Attack", "Darkvision", "Evasion"],
    alignment="Tarafsız"
)

caelus = Character(
    name="Caelus Veylor",
    race="İnsan",
    char_class="Büyücü",
    level=1,
    stats={"strength": 8, "dexterity": 12, "constitution": 10, "intelligence": 17, "wisdom": 14, "charisma": 11},
    background="Akademiden atıldıktan sonra yasak büyülere yöneldi.",
    personality="Analitik, mesafeli",
    abilities=["Mage Armor", "Firebolt", "Arcane Recovery"],
    alignment="Yasacı Tarafsız"
)

# Dışa aktarım
prebuilt_characters = [durok, sylen, caelus]
