def selectionSort(A):
    n = len(A)

    for j in range (n):
        smallest =j

        for i in range(j+1,n):
            if A[i] < A[smallest]:
                smallest = i

        A[j],A[smallest] = A[smallest],A[j]


def findRange(A):
    range = A[-1] - A[0]
    return range

def findMedian(A):
    if len(A) % 2 == 0:
        median = (A[len(A) // 2] + A[len(A) // 2] -1) / 2
    else:
        median = A[len(A) // 2]

    return median


A = []

for i in range(4):
    num = int(input("Marks : "))
    A.append(num)


selectionSort(A)
print("Sorted marks  : ",A)

print("Range is :",findRange(A))
print("Median is : ",findMedian(A))
