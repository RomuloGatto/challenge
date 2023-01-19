from src.school import Schools


def test_search_schools():
    schools = Schools("data/sl051bai.csv")

    query = "elementary school highland park"
    result_title, search_result, search_best_hits = schools.search(query)
    assert len(search_result) == 2
    assert len(search_best_hits) == 230

    query = "jefferson belleville"
    result_title, search_result, search_best_hits = schools.search(query)
    assert len(search_result) == 1
    assert len(search_best_hits) == 210

    query = "riverside school 44"
    result_title, search_result, search_best_hits = schools.search(query)
    assert len(search_result) == 1
    assert len(search_best_hits) == 40

    query = "granada charter school"
    result_title, search_result, search_best_hits = schools.search(query)
    assert len(search_result) == 2
    assert len(search_best_hits) == 479

    query = "foley high alabama"
    result_title, search_result, search_best_hits = schools.search(query)
    assert len(search_result) == 1
    assert len(search_best_hits) == 6436

    query = "KUSKOKWIM"
    result_title, search_result, search_best_hits = schools.search(query)
    assert len(search_result) == 1
    assert len(search_best_hits) == 0
