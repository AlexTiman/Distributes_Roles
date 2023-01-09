# Module with all functions to use in main file


def get_names_combinations(names: list[str]) -> list[tuple[str, str]]:
    """
    Receives list of names and returns managers and developers names combinations,
    using each name for each position only once.
    """

    names_extended = names.copy()
    names_extended.append(names[0])
    names_combinations = []
    for i in range(len(names_extended) - 1):
        names_combinations.append((names_extended[i], names_extended[i + 1]))
    return names_combinations


def ideas_roles_distribution(
    project_author: list[tuple[str, str]], names: list[str]
) -> list[dict[str, str]]:
    """
    Receives list of tuples of str pairs: project name, project author.
    Creates list of dicts for every project based on Rules.
    Rules:
    1. Author can't manage or developer his own project
    2. Manager can't develop project
    3. Each person has to develop and manage exactly one project.
    4. If one person has more than one idea,they should be used after everyone else's ideas are assigned
    """

    names_combinations = get_names_combinations(names)
    final_combinations = []
    used_ideas_authors = []
    not_used_ideas = project_author.copy()
    for project in project_author:
        if not len(names_combinations):
            print("Every manager and developer already has a project")
            for project_left in not_used_ideas:
                print(f"Unused idea {project_left}")
            return final_combinations
        if project[1] not in used_ideas_authors:
            for names_variant in names_combinations:
                if project[1] not in names_variant:
                    final_combinations.append(
                        {
                            "project": project[0],
                            "author": project[1],
                            "manager": names_variant[0],
                            "developer": names_variant[1],
                        }
                    )
                    names_combinations.remove(names_variant)
                    used_ideas_authors.append(project[1])
                    not_used_ideas.remove(project)
                    break
    if not_used_ideas:
        for project in not_used_ideas:
            for names_variant in names_combinations:
                if project[1] not in names_variant:
                    final_combinations.append(
                        {
                            "project": project[0],
                            "author": project[1],
                            "manager": names_variant[0],
                            "developer": names_variant[1],
                        }
                    )
                    names_combinations.remove(names_variant)
    return final_combinations
