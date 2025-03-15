A=input()
B=input()
if(A=='rock' and B=='scissor'):
    print("A is winner")
elif(A=='rock' and B=='paper'):
     print("A is winner")
elif(A=='scissor' and B=='rock'):
    print("B is winner")
elif(A=='scissor' and B=='paper'):
    print(" A is winner")
elif(A=='paper' and B=='rock'):
    print(" B is winner") 
elif(A=='paper' and B=='scissor'):
    print(" B is winner")
elif(A=='rock' and B=='rock'):
    print("Tie")
elif(A=='paper' and B=='paper'):
    print("Tie")
elif(A=='scissor' and B=='scissor'):
    print("Tie")
    
