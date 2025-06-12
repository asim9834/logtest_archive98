
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Character:
    name: str
    race: str
    class_: str
    level: int
    stats: Dict[str, int]  # Örn: {"strength": 10, "dexterity": 12, ...}
    background: str
    personality: str
    abilities: List[str] = field(default_factory=list)
    alignment: str = "Neutral"

    def summary(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Race: {self.race}\n"
            f"Class: {self.class_}\n"
            f"Level: {self.level}\n"
            f"Stats: {self.stats}\n"
            f"Alignment: {self.alignment}\n"
            f"Background: {self.background}\n"
            f"Personality: {self.personality}\n"
            f"Abilities: {', '.join(self.abilities)}"
        )
