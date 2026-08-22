n=int(input("Enter units:"))
if n <= 100:
    bill1=100*2
    print("Electricity bill=",bill1)
elif n>100 and n<=200:
    bill2=100*2+(n-100)*3
    print("Electricity bill=",bill2)
else:
    bill3=100*2+100*3+(n-200)*5
    print("Electricity bill=",bill3)
    
