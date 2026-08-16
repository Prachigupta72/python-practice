n = int(input("Enter the number:"))
original=n
sum=0
while n>0:
    m = n%10
    sum=(m**3)+sum
    n=n//10
if original == sum:
    print("Armstrong number")
else:
    print("Not an armstrong number")
