def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n
    
while True:
    num = int(input("Enter a positive integer: "))

    if num == -1:
        break
    else:
        ans = sum(num)
        print(ans)