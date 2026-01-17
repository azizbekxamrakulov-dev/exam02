text = "Withdraw uchun balans yetarli emasligini tekshiring"
text = "Manfiy summa kiritsa xato qaytaring"

def atm_operation(balance, operation, amount):
    if operation == "deposit":
        return balance + amount
    elif operation == "withdraw":
        if amount > balance:
            return text
        elif amount < 0:
            return text
        else:
            return balance - amount
    else:
        return "Noto'g'ri operatsiya turi"
atm_operation(100000, "deposit", 50000) # 150000

atm_operation(100000, "withdraw", 20000) # 80000

atm_operation(100000, "withdraw", 150000) # "Withdraw uchun balans yetarli emasligini tekshiring"

print(atm_operation(100000, "deposit", 50000))
print(atm_operation(100000, "withdraw", 20000))
print(atm_operation(100000, "withdraw", 150000))
