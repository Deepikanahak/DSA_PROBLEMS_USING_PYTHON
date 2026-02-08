def palindrom(str, left,right):
    if left >= right:
        return True
    if str[left]!=str[right]:
        return False
    return palindrom(str,left+1,right-1)
str = "this is my journey towards"
x=palindrom(str,0,10)
print(x)