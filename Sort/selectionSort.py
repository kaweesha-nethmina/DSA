def selectionSort(A):
    n = len(A)  # Get the length of the array
    # Loop through the array
    for j in range(n):
        smallest = j  # Assume the current index is the smallest
        # Loop through the unsorted portion of the array
        for i in range(j + 1, n):
            # Update smallest if a smaller element is found
            if A[i] < A[smallest]:
                smallest = i
        # Swap the found smallest element with the first unsorted element
        A[j], A[smallest] = A[smallest], A[j]

# Example usage
if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print("Original array:", A)
    selectionSort(A)
    print("Sorted array:", A)
