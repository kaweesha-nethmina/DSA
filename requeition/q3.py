def func(num):
    if num == 1:
        return 1
    else:
        return (num-1) + (func(num-1))
    

while True:
    num = int(input("Enter number : "))

    if num == -1:
        break
    else:
        result = func(num)
        print("output : ",result)