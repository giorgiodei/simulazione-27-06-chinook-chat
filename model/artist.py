from dataclasses import dataclass


@dataclass(frozen=True)
class Artist:
    ArtistId: int
    Name: str

    def __str__(self):
        return self.Name
