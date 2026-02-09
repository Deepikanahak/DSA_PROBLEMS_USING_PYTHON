# without using function
n = int(input("enter a number: "))
i = 0
j = 1
if n<0:
    print("Invalid data: Re-enter a value more than 1 ")
elif n==1:
    print(i)
elif n ==2:
    print(i,j)
else:
    print(i,j,end = " ")
    for num in range(2,n):
        sum = i+j
        print(sum,end =" ")
        i = j
        j = sum


# using Recursion
def fibonacci(n,i,j,sum):
    if n ==0 or n==1:
        return 
n = int(input("enter a number: "))
fibonacci(n)


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
num = int(input("enter a number: "))
for i in range(num):
    print(fib(i), end=" ")
