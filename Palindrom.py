#without using recursion means using loops
def checkPalindrom(str):
    l = len(str)
    left = 0
    right = l-1
    while left < right:
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
str = input("enter a strinng to check palidrom: ")
x = checkPalindrom(str)
print(x)
#Time complexity is O(n/2) but ignoring constant it's O(n) and space complexity is S(1)

#using recursion
def palindrom(str, left,right):
    if left >= right:
        return True
    if str[left]!=str[right]:
        return False
    return palindrom(str,left+1,right-1)
str = "this is my journey towards"
x=palindrom(str,0,10)
print(x)
