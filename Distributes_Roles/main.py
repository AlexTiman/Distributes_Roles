# Main File to execute Script.
from functions import ideas_roles_distribution


project_author_list = [
    ("1", "Alex"),
    ("2", "Jura"),
    ("3", "Roma"),
    ("4", "Sofa"),
    ("5", "Vlad"),
]
names_list = ["Alex", "Roma", "Vlad", "Sofa", "Jura"]

if __name__ == "__main__":
    result = ideas_roles_distribution(project_author_list, names_list)
    for project in result:
        print(project)
