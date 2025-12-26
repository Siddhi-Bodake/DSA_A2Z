#Given an array of N integers, write a program to implement the Bubble Sorting algorithm.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("sorted array : ", arr)

arr=[2,1,4,3,7,6]
bubble_sort(arr)