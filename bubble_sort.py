def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

         
n = int(input("Enter number of elements:"))
arr=[]
for i in range(0, n):
    ele = int(input())
    arr.append(ele)  
print("Original array:")
print(arr)
bubbleSort(arr)
print("Sorted arra:")
print(arr)
