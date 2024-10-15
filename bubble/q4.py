
def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i],A[j] = A[j],A[i]


A = []

for i in range(8):
    num = int(input("Number : "))
    A.append(num)

print("Before sort : ",A)
bubbleSort(A)
print("After sort : ",A)

