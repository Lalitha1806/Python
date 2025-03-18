n=0
while n<=100:
    if(n%2==0):
        if (n%4==0):
            print(n)
        else:
            print("Even,but not multiple of 4")
    else:
        if(n%3==0):
            print(n)
        else:
            print("Odd,but not multiple of 3")
    n+=1           
        
