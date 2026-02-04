num = int(input("enter a number: "))
n = num
sum = 0
while n>0:
    r = n%10
    sum = sum + r**3
    n = n//10
if sum == num:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")