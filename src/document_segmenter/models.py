from dataclasses import asdict, dataclass


@dataclass(frozen=True, slots=True)
class Segment:
    text: str
    type: str = "paragraph"
    level: int | None = None
    source: str | None = None

    def to_dict(self) -> dict[str, str | int | None]:
        return asdict(self)
