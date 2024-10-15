#insession sort
A=[]
n = 3

for i in range(0,n):
    number = int(input(" Enter the Nunmber: "))
    if(number>10 and number<20):
        A.append(number)
    else:
        print("Invalid Number : ")
    i =i+1
print(A)

# def InsertionSort(A):
    
#     for i in range (1,len(A)):
#         key = A[i]
#         j = i-1
#         while j>=0 and key<A[j]:
#             A[j +1]=A[j]
#             j= j-1
#         A[j+1] = key


def insertionSort(A):

    
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and key < A[j]:
            A[j+1] = A[j]
            j = j-1
        
        A[j+1] = key





# A.sort()
print("Sorted Array : ",A)

