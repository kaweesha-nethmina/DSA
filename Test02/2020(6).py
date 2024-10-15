def func(n):
    if n == 1:
        return 1
    else:
        return func(n-1) + n*n*n
    

while True:
    num = int(input("Enter positive integer: "))

    if num == -1:
        break
    else:
        ans = func(num)
        print(ans)