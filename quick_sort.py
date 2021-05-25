def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # swap according to pivot element

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot element on the right place
    return i + 1


def quick_sort(arr, low, high):
    # complexity : theta(n log(n))
    # is in place algorithm
    # is not stable algorithm

    if len(arr) == 1:  # arr contains 1 element so it is sorted
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)  # sorting part on the left side
        quick_sort(arr, pi + 1, high)  # sorting part on the right side


arr = [9, 7, 0, -6, -4, 1, 4, 3, 100, 10, 30]
quick_sort(arr, 0, len(arr) - 1)
print('Sorted list is : ', end=' ')
for i in arr:
    print(i, end='  ')
