def insertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j]>key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key

def findRange(A):
    range = A[-1] - A[0]
    return range


def findMedian(A):
    if len(A) % 2 == 0:
        median = (A[len(A)//2] + A[len(A)//2] -1)/2
    else:
        median = A[len(A) // 2]

    return median




A=[]

for i in range(3):
    num = int(input("Enter Marks: "))
    A.append(num)

print("before sort",A)

insertionSort(A)

print("After Sort: ",A)


print("Range is : ",findRange(A))
print("Median is : ",findMedian(A))
