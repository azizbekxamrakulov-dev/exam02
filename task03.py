def calculate_tax(salary):
    if salary <= 5_000_000:
        rate = 0
    elif salary <= 10_000_000:
        rate = 0.12
    elif salary <= 20_000_000:
        rate = 0.18
    else:
        rate = 0.25

    tax = int(salary * rate)
    net = salary - tax

    return {
        "gross": salary,
        "tax": tax,
        "net": net,
        "rate": f"{int(rate*100)}%"
    }


print(calculate_tax(8_000_000))
print(calculate_tax(3_000_000))