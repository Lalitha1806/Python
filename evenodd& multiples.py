for i in range(1,101):
    if(i%2==0):
        if (i%4==0):
            print(i)
        else:
            print("Even,but not multiple of 4")
    else:
        if(i%3==0):
            print(i)
        else:
            print("Odd,but not multiple of 3")
        
