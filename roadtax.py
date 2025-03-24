a = int(input())

if 1 < a <= 10:
    charge = a * 10
    print(charge)
elif 11 <= a <= 20:
    charge = (10 * 10) + ((a - 10) * 12)
    print(charge)
elif 21 <= a <= 30:
    charge = (10 * 10) + (10 * 12) + ((a - 20) * 15)
    print(charge)
else:
    print("Hema Sundar will collect the charge")
