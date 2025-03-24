n=int(input())
if n%4==0:
    cars = n//4
    print("cars required:",cars)
else:
    cars=(n//4)+1
    print("cars required:", cars)
