from school import Schools, SearchType


def print_counts():
    schools = Schools("data/sl051bai.csv")
    state = schools.group_by(SearchType.STATE)

    print(f"Total Schools: {len(schools.school_list)}")
    print("Schools by State:")
    for school_state in state:
        print(f"{school_state}: {len(state[school_state])}")

    metrocentric = schools.group_by(SearchType.METROCENTRIC)
    print("\nSchools by Metro-centric locale:")
    for school_metrocentric in metrocentric:
        print(f"{school_metrocentric}: {len(metrocentric[school_metrocentric])}")

    city = schools.group_by(SearchType.CITY)
    most_schools = schools.find_most_schools(city)
    city_most_school_name = list(most_schools.keys())[0]
    print(
        f"\nCity with most schools: {city_most_school_name} ({len(most_schools[city_most_school_name])} schools)"
    )
    print(f"\nUnique cities with at least one school: {len(city)}")


print_counts()
