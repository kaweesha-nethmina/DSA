def bubbleSort(A):
    n = len(A)

    for i in range (n):
        for j in range (n-1,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]

def findRange(A):
    range = A[-1] - A[0]
    return range

def findMedian(A):
    if len(A) % 2 == 0:
        median = ( A[len(A) // 2] + A[len(A) // 2] -1  ) / 2
    else:
        median = A[len(A) // 2]
    return median


A=[90,67,98,12]

bubbleSort(A)
print(A)

print("Range  : ",findRange(A))
print("Median : ",findMedian(A))
