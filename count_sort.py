def count_sort(arr):
    # complexity : O(n + k)
    # is not in place algorithm
    # is stable algorithm
    # can not be used for sorting negative numbers
    # used only for sorting positive integer numbers
    # need huge space

    max_element = max(arr)
    sorted_elements = [0] * (max_element + 1)
    for i in arr:
        sorted_elements[i] += 1

    j = 0

    for k in range(len(sorted_elements)):
        while sorted_elements[k] != 0:
            arr[j] = k
            j += 1
            sorted_elements[k] -= 1
    return arr


arr = [9, 5, 0, 4, 5, 1, 4, 3, 100, 10, 30]
sorted_list = count_sort(arr)
print('Sorted list is : ', end=' ')
for i in sorted_list:
    print(i, end='  ')
