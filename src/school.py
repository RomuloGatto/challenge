import csv
import itertools
from dataclasses import dataclass
from enum import Enum
from typing import Callable


@dataclass
class School:
    NCESSCH: str
    LEAID: str
    LEANM05: str
    SCHNAM05: str
    LCITY05: str
    LSTATE05: str
    LATCOD: str
    LONCOD: str
    MLOCALE: str
    ULOCALE: str
    status05: str


class SearchType(Enum):
    STATE = "LSTATE05"
    METROCENTRIC = "MLOCALE"
    CITY = "LCITY05"


class Schools:
    school_list: list[School]

    def __init__(self, file_path: str) -> None:
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            self.school_list = [School(**row) for row in reader]

    def group_by(self, key: SearchType) -> dict[str, list[School]]:
        key_func: Callable[[School], str] = lambda x: x.__dict__[key.value]
        return {
            key: list(group)
            for key, group in itertools.groupby(self.school_list, key_func)
        }

    def find_most_schools(
        self, grouped: dict[str, list[School]]
    ) -> dict[str, list[School]]:
        biggest_group = {(key := list(grouped.keys())[0]): grouped[key]}
        for key in grouped.keys():
            if len(grouped[key]) > len(list(biggest_group.values())[0]):
                biggest_group = {key: grouped[key]}

        return biggest_group
