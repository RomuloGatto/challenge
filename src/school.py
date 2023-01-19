import csv
import itertools
import time
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

    def search(
        self, query: str
    ) -> tuple[str, list[tuple[int, School]], list[tuple[int, School]]]:
        hits = []

        start = time.time()
        query_prep = tuple(query.upper().split(" "))
        for school in self.school_list:
            to_lookup = (
                tuple(school.SCHNAM05.split(" "))
                + tuple(school.LCITY05.split(" "))
                + tuple(school.LSTATE05)
            )

            hit = set(query_prep).intersection(to_lookup)
            if hit:
                if query_prep[0] == school.LCITY05.split(" ")[0]:
                    hit.add(school.LCITY05)

                hits.append((len(hit), school))

        sorted_hits = sorted(hits, key=lambda x: x[0], reverse=True)
        result = list(filter(lambda x: x[0] == sorted_hits[0][0], hits))

        best_hits = []
        if sorted_hits[0][0] > 1:
            best_hits = list(filter(lambda x: x[0] == sorted_hits[0][0] - 1, hits))

        end = time.time()
        title = f"Results for '{query}' (search took: {round(end-start, 3)}s)"

        return (title, result, best_hits)
