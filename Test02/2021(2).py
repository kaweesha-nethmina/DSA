def func(num):
    if num == 1:
        return 2
    else:
        return func(num -1)/2
    
while True:
    num = int(input("Enter number: "))

    if num == -1:
        break
    else:
        ans = func(num)
        print(ans)

#output
# Enter number: 1
# 2
# Enter number: 2
# 1.0
# Enter number: 3
# 0.5
# Enter number: 4
# 0.25
# Enter number: 5
# 0.125