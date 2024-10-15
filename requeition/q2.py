def func(num):
    if num == 1:
        return 1
    else:
        return num + (func(num - 1))
    

while True:
    num = int(input("Enter Number : "))

    if num == -1:
        break
    else:
        result = func(num)
        print("Outrput : ",result)