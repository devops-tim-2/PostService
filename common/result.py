from dataclasses import dataclass, asdict


@dataclass
class Result:
    result: object
    code: int


    def get_dict(self):
        return asdict(self)
