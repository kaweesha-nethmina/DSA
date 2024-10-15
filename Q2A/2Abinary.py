#arr =Array
#low = start index
#high = end index
#x = search value
#mid = Mid_Index

#Binary search
arr = []
for v in range(4):
    num = int(input("Enter the Number : "))
    arr.append(num)
print(arr)

x = int(input("Enter the Search Value : "))

def binary_search(arr,low,high,x):
    if high >= low:
        
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr(mid) > x:
            return binary_search(arr,low,mid-1,x)

        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

#funtion call
result = binary_search(arr,0,len(arr)-1,x)

if result != -1:
    print("Elemnrt is precent at Index ",str(result))
else:
    print("Element is not present array")
