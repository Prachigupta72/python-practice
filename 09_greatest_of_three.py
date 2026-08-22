n = int(input("Enter first number:"))
m = int(input("Enter second number:"))
x = int(input("Enter third number:"))
if n>m and n>x:
    print("Greatest:",n)
elif m>n and m>x:
    print("Greatest:",m)
else:
    print("Greatest:",x)
    
