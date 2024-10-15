def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)
    
while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    else:
        result = Fibonacci(num)
        print("The ",num, "Fibonacci number is :",result)