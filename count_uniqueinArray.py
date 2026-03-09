#there is a sorted array we need to rearrange the array and count unique elements in it
array = list(map(int,input("enter a sorted array: ").split()))
i = 0
j = 1
count = 1
for j in range(1,len(array)): 
    if array[i]==array[j]:
        j = j + 1
    else:
        array[i+1] = array[j]
        j = j + 1
        i = i + 1
        count = count + 1
print(count)
