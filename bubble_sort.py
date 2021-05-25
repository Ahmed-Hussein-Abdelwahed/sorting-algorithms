def bubble_sort(arr):
    # complexity: O(n^2)
    # is stable algorithm
    # is in place algorithm

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr


arr = [9, 7, 0, -6, -4, 1, 4, 3, 100, 10, 30]
sorted_list = bubble_sort(arr)
print('Sorted list is : ', end=' ')
for i in sorted_list:
    print(i, end='  ')
