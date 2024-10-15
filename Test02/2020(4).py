
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


while True:
    
        x = int(input("Enter the base (x), or -1 to quit: "))
        if x == -1:
            print("Exiting program.")
            break
        
        n = int(input("Enter the exponent (n), or -1 to quit: "))
        if n == -1:
            print("Exiting program.")
            break

        result = power(x, n)
        print(f"The result of {x} raised to the power of {n} is: {result}")


