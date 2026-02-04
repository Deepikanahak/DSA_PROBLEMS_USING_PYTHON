num = int(input("enter a number: "))
n = num
l1 = []
for i in range(1,n+1):
    if n%i == 0:
       l1.append(i)
print("factors are",l1)