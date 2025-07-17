from dataclasses import dataclass

@dataclass
class Record:
    title: str
    artist: str
    year: int | None
    genre: str
    cover_image: str
    link: str

    def to_dict(self) -> dict:
        return self.__dict__

    def is_valid(self) -> bool:
        return self.title and self.artist and self.cover_image is not None
