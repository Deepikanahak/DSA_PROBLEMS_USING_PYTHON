#HEAD RECURSION

count = 0
def fun():
    global count
    if count == 4:
        return
    print("Deepika")
    count += 1
    fun()
fun()

#TAIL RECURSION
count = 0
def fun():
    global count
    if count == 4:
        return
    count +=1
    fun()
    print("Deepika")
fun()
    