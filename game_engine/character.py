# game_engine/character.py

class Character:
    def __init__(self, name, race, class_, description="", story="", alignment=None, level=1):
        """
        Tüm karakter özelliklerini destekleyen kapsamlı yapılandırıcı.
        """
        self.name = name
        self.race = race
        self.class_ = class_
        self.description = description  # Oyuncunun girdiği kısa tanım veya arka plan notu
        self.story = story              # AI tarafından ya da rastgele oluşturulan uzun hikaye
        self.alignment = alignment      # İsteğe bağlı: karakterin ahlaki yönelimi
        self.level = level              # İsteğe bağlı: karakter seviyesi (default 1)

    def to_dict(self):
        """
        Karakteri sözlük formatına dönüştürür (kaydetme ve yükleme için).
        """
        return {
            "name": self.name,
            "race": self.race,
            "class": self.class_,
            "description": self.description,
            "story": self.story,
            "alignment": self.alignment,
            "level": self.level
        }

    @classmethod
    def from_dict(cls, data):
        """
        Sözlük verisinden karakter nesnesi oluşturur.
        """
        return cls(
            name=data.get("name", ""),
            race=data.get("race", ""),
            class_=data.get("class", ""),
            description=data.get("description", ""),
            story=data.get("story", ""),
            alignment=data.get("alignment"),
            level=data.get("level", 1)
        )
