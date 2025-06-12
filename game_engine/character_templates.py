
from game_engine.character import Character

# Hazır karakter: Dwarf Barbar
durok_steelhammer = Character(
    name="Durok Steelhammer",
    race="Dwarf",
    char_class="Barbarian",
    level=1,
    stats={"strength": 16, "dexterity": 10, "constitution": 15, "intelligence": 8, "wisdom": 12, "charisma": 9},
    background="Bir dağ klanında doğdu, ailesi devler tarafından katledildi. Öfke kontrolü sorunlu, savaşta acımasız.",
    personality="Agresif, sadık, emir almaktan hoşlanmaz.",
    abilities=["Rage", "Reckless Attack", "Stone's Endurance"],
    alignment="Chaotic Good"
)

# Hazır karakter: Elf Rogue
sylen_varithiel = Character(
    name="Sylen Varithiel",
    race="Elf",
    char_class="Rogue",
    level=1,
    stats={"strength": 9, "dexterity": 17, "constitution": 11, "intelligence": 12, "wisdom": 13, "charisma": 10},
    background="Çocukken avcılıkla uğraştı, kazayla bir insan öldürmesi onu karanlık yollara itti. Şimdi ölüm sessizliğiyle dost.",
    personality="Sessiz, gözlemci, aniden karar verir.",
    abilities=["Sneak Attack", "Darkvision", "Evasion"],
    alignment="Neutral"
)

# Hazır karakter: Human Wizard
caelus_veylor = Character(
    name="Caelus Veylor",
    race="Human",
    char_class="Wizard",
    level=1,
    stats={"strength": 8, "dexterity": 12, "constitution": 10, "intelligence": 17, "wisdom": 14, "charisma": 11},
    background="Bir büyü akademisinde yetişti. Bilgiye olan açlığı nedeniyle akademiden kovuldu. Şimdi büyünün sırlarını tek başına keşfediyor.",
    personality="Analitik, ketum, duygularını bastırır.",
    abilities=["Firebolt", "Mage Armor", "Arcane Recovery"],
    alignment="Lawful Neutral"
)

# Liste halinde dışa aktar
prebuilt_characters = [durok_steelhammer, sylen_varithiel, caelus_veylor]

CHARACTER_CLASSES = ["Barbarian", "Rogue", "Wizard", "Fighter", "Bard", "Cleric", "Druid", "Paladin", "Ranger", "Monk", "Sorcerer", "Warlock"]
