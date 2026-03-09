#take a input array and return the numbers whose sum is equal to target 9
num = list(map(int, input("enter numbers separated by space: ").split()))
target = 9
num.sort()
i = 0
j = len(num)-1
while i<j:
    if num[i]+num[j] == target:
        print([num[i],num[j]])
        i=i+1
        j=j-1
    if num[i]+num[j] < target:
        i+=1
    if num[i]+num[j] > target:
        j=j-1