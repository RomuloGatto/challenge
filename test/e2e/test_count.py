from src.school import Schools, SearchType


def test_count_schools():
    schools = Schools("data/sl051bai.csv")
    state = schools.group_by(SearchType.STATE)
    assert len(state) == 21

    metrocentric = schools.group_by(SearchType.METROCENTRIC)
    assert len(metrocentric) == 9

    city = schools.group_by(SearchType.CITY)
    assert len(city) == 4852

    most_schools = schools.find_most_schools(city)
    assert len(most_schools.keys()) == 1
    assert most_schools.get("EVANSVILLE")
    assert len(most_schools["EVANSVILLE"]) == 43
