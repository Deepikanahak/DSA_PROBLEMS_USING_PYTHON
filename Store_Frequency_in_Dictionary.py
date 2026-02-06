# Normal Approach
# take input from user
l = list(input("enter elements into list: "))
freq = {}
for i in range(len(l)):
    if l[i] in freq:
        freq[l[i]] += 1
    else:
        freq[l[i]] = 1
print(freq)

#2nd approach
l = list(input("enter elements into the list: "))
hash_map = {}
for i in range(len(l)):
    hash_map[l[i]] = hash_map.get(l[i],0) + 1
    #let l = [1,2,3,2,4,2,3,4,5,4]
    #hash_map[3] = hash_map.get(3,0)+1
    #hash_map[3] = 1+1 or 2
print(hash_map)