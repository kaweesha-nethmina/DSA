def func(num):
    if num == 1:
        return 1
    else:
        return num +(func(num-1))

while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    else:
        out = func(num)
        print(out)
