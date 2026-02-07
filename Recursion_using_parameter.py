def func(num,n):
    if n==0:
        return
    print(num)
    func(num,n-1)
func(15,3)