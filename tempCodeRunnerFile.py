#Write a program to find the largest of three numbers using conditional statements
def find_largest(n1,n2,n3):
    if n1>n2 and n2>n3:
        return n1
    elif n2>n3 and n2>n1:
        return n2
    else:
        return n3
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
n3 = int(input("enter a number: "))
find_largest(n1,n2,n3)