#2.Count the number of digits in an integer

num = int(input("enter a number: "))    #take a number as input from user
n = num
count = 0   #will count number of digits present
while n>0:
    r = n%10
    n =n//10
    count+= 1
print("number of digits in the numbers: ",count)
