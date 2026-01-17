def calculate_stats(numbers: list) -> dict:
    total = sum(numbers)
    avaerage = total / len(numbers)
    
    return {"sum": total, "average": round(avaerage, 2)}


print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))
# {"sum": 44, "average": 6.29}

print(calculate_stats([10, 20, 30]))
# {"sum": 60, "average": 20.0}
