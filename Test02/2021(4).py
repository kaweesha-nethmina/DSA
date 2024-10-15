def func(num):
    if num == 1:
        return 1
    else:
        return (num -1 ) + func(num-1)
    
while True:
    num = int(input("Enter number : "))

    if num == -1:
        break
    else:
        ans = func(num)
        print("Output: ",ans)


#OUTPUT

# Enter number : 1
# Output:  1
# Enter number : 2
# Output:  2
# Enter number : 3
# Output:  4
# Enter number : 4
# Output:  7
# Enter number : 5
# Output:  11