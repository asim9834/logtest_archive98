# game_engine/character.py

class Character:
    def __init__(self, name, race, class_, story=""):
        self.name = name
        self.race = race
        self.class_ = class_
        self.story = story

    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "class": self.class_,
            "story": self.story
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            race=data.get("race", ""),
            class_=data.get("class", ""),
            story=data.get("story", "")
        )
