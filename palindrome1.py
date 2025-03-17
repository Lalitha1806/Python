s=input()
str=s.upper()
print(str)
rev=s[-1: :-1]
if rev==s:
    print("palindrome")
else:
    print("Not palindrome")
