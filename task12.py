def sort_names(students: list) -> list:
    return list(map(lambda x: x.capitalize() ,sorted(map(lambda x: x.lower(), students))))

print(sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"]))
# ["Ali", "Aziza", "Hasan", "Husan", "Vali"]

print(sort_names(["Zara", "Bobur", "Anvar"]))
# ["Anvar", "Bobur", "Zara"]
