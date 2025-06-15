# game_engine/character.py

class Character:
    def __init__(
        self,
        name,
        race,
        class_,
        description="",
        story="",
        alignment=None,
        level=1,
        stats=None,
        background="",
        personality="",
        abilities=None
    ):
        """
        Tam kapsamlı karakter yapısı.
        """
        self.name = name
        self.race = race
        self.class_ = class_
        self.description = description
        self.story = story
        self.alignment = alignment
        self.level = level
        self.stats = stats or {}
        self.background = background
        self.personality = personality
        self.abilities = abilities or []

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "class": self.class_,
            "description": self.description,
            "story": self.story,
            "alignment": self.alignment,
            "level": self.level,
            "stats": self.stats,
            "background": self.background,
            "personality": self.personality,
            "abilities": self.abilities
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            race=data.get("race", ""),
            class_=data.get("class", ""),
            description=data.get("description", ""),
            story=data.get("story", ""),
            alignment=data.get("alignment"),
            level=data.get("level", 1),
            stats=data.get("stats", {}),
            background=data.get("background", ""),
            personality=data.get("personality", ""),
            abilities=data.get("abilities", [])
        )
