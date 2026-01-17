def count_by_grade(grades, target_grade):
    students = [n for n, g in grades.items() if g == target_grade]
    return {"count": len(students), "students": students}


print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))
print(count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4))