# Function to merge two halves
def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from left and right arrays and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left and right arrays
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Function to implement merge sort
def mergeSort(A):
    # Base case: if the array has one element, it's already sorted
    if len(A) <= 1:
        return A

    # Split the array into two halves
    mid = len(A) // 2
    left_half = mergeSort(A[:mid])
    right_half = mergeSort(A[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

# Main program to test the function
A = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", A)
sorted_A = mergeSort(A)
print("Sorted Array:", sorted_A)
