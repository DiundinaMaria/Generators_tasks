from decimal import Decimal, getcontext

sqrt = 0
eleven = Decimal(11)
getcontext().prec = 100503200
print(getcontext().prec)
try:
    sqrt = eleven.sqrt()
except MemoryError:
    print("Not enough memory")
    with open("sqrt11.txt", "w") as file:
        file.write(f"{sqrt}")
else:
    print("Success")
    with open("sqrt.txt", "w") as file:
        file.write(f"{sqrt}")
