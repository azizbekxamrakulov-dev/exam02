def analyze_grades(students):
    avg = sum(students.values()) / len(students)
    above = [name for name, g in students.items() if g > avg]
    return {"average": round(avg, 2), "above_average": above}


print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))
print(analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5}))