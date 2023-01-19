from school import Schools


def search_schools(query: str):
    schools = Schools("data/sl051bai.csv")
    result_title, search_result, search_best_hits = schools.search(query)

    print(result_title)
    last_index_result = 0
    for i, result in enumerate(search_result):
        print(f"{i+1}. {result[1].SCHNAM05}")
        print(f"{result[1].LCITY05}, {result[1].LSTATE05}")
        last_index_result = i + 1

    if last_index_result < 3:
        for i, best_hit in enumerate(search_best_hits):
            if i + last_index_result == 3:
                break

            print(
                f"{i + last_index_result + 1}. [Next Best Hit] {best_hit[1].SCHNAM05}"
            )
            print(f"{best_hit[1].LCITY05}, {best_hit[1].LSTATE05}")


search_schools("elementary school highland park")
search_schools("jefferson belleville")
search_schools("riverside school 44")
search_schools("granada charter school")
search_schools("foley high alabama")
search_schools("KUSKOKWIM")
