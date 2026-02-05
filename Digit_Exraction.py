#1.Extraction of digits from an integer
num = int(input("enter number: "))  #Take a input from the user
n = num     #assign it to a tempory variable so that we don't loose our original data
while n>0:  #since we don't know number of iteration use while loop
    r = n%10  #finding the remainder
    print("digits are:",r)  #printing individual digits
    n = n//10 #stores the quotient

# time complexity o(log base 10(n))
