num = int(input("enter a number: "))    #take a number as input from user
n = num
rev = 0#will count number of digits present
while n>0:
    r = n%10
    rev = rev*10+r
    n =n//10
if rev == num:
    print("this number is a palindrom")
else:
    print("not a palindrom")