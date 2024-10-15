def Multiply(M,n):
    if n == 1:
        return M;
    else:
        return (M + Multiply(M,n-1) )
    
while True:

    M = int(input("Enter number(M) : "))

    n = int(input("Enter number(n) : "))

    ans = Multiply(M,n)

    print(ans)

    if M == -1 or n == -1:
        break


