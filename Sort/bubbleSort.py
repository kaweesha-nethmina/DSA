A=[]
for v in range(1,5):
    A.append(int(input('Enter a Number : ')))
print(A)

# Bubble Sort function
def bubbleSort(A):
    n = len(A)
    # Outer loop for each element in the list
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:  # Swap if the element is smaller than the previous one
                A[j], A[j - 1] = A[j - 1], A[j]

# Sort the array using Bubble Sort
bubbleSort(A)

print('Sorted Array:')
print(A)

    

