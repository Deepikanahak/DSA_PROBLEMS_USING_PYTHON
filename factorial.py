def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
f = factorial(5)
print("factorial of num is:",f)
# Time and Space Complexity is O(n)