def selection_sort(arr):
    # complexity : O(n^2)
    # is not stable algorithm
    # is in place algorithm

    for i in range(len(arr)):
        k = i
        for j in range(i, len(arr)):
            if arr[j] < arr[k]:
                k = j
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
    return arr


arr = [9, 7, 0, -6, -4, 1, 4, 3, 100, 10, 30]
sorted_list = selection_sort(arr)
print('Sorted list is : ', end=' ')
for i in sorted_list:
    print(i, end='  ')
