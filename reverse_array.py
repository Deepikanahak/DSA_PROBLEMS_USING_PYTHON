#without using recursion
array = [1,2,3,4,5,6,7]
r_array = []
for i in array[::-1]:
    r_array.append(i)
print(r_array)

#using recursion
def array_reverse(array,left,right):
    if left >= right:
        return
    else:
        array[left],array[right] = array[right],array[left]
    array_reverse(array,left+1,right-1)
array = [1,2,3,4,5,6,7]
array_reverse(array,0,6)
print(array)