def insertion_sort(arr):
    # complexity : O(n^2)
    # is stable algorithm
    # is in place algorithm

    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j > - 1 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


arr = [9, 7, 0, -6, -4, 1, 4, 3, 100, 10, 30]
sorted_list = insertion_sort(arr)
print('Sorted list is : ', end=' ')
for i in sorted_list:
    print(i, end='  ')
