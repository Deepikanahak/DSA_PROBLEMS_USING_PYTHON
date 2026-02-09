#Write a function to take a number as input and check whether it is even or odd
def Check_even_odd(n):
    if n%2 == 0:
        return "True"
    else:
        return "False"
n = int(input("enetr a number: "))
print(Check_even_odd(n))

#Write a function that takes two numbers as input and returns their sum and difference
def sum_diff(n1,n2):
    return n1+n2,n1-n2
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
print(sum_diff(n1,n2))

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
print(find_largest(n1,n2,n3))

#Write a function to print numbers from 1 to n using a loop
#Write a function to calculate the factorial of a number using a loop
#Write a function that accepts a list and returns only the even numbers
#Write a function to count the number of vowels in a given string
#Write a function to reverse a string without using built-in reverse functions
#Write a function to print the multiplication table of a given number
#Write a function that checks whether a number is prime or not
#Write a function to find the sum of all elements in a list using a loop
#Write a function that accepts a dictionary and prints all keys and values
#Write a function to generate Fibonacci series up to n terms
#Write a function to find the maximum and minimum values in a list
#Write a function to check whether a string is a palindrome