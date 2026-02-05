num = int(input("enter a number: "))
n = num
l1 = []
for i in range(1,n+1):
    if n%i == 0:
       l1.append(i)
print("factors are",l1)

#2nd approach
num = int(input("enter a number: "))
n = num
l1 = []
for i in range(1,n//2+1):
    if n%i == 0:
        l1.append(i)
l1.append(n)
print(l1)

#3rd and optimized approach
num = int(input("enter a number: "))
n = num
l1 = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        l1.append(i)
        if n//i != i:
            l1.append(n//i)
l1.sort()
print(l1)


