def multiplication(n):
    product = 1
    for i in range(1,11):
        print(n, "X", i, "=", n*i)
num = int(input("Enter a number of which you want to print a table: "))
table = multiplication(num)
print("multiplication table is:\n",table)
#Write a function that checks whether a number