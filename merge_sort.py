def merge_sort(arr):
    # complexity : theta(n log(n))
    # is stable algorithm
    # is in place algorithm

    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        left_part = arr[:mid]

        # into 2 halves
        right_part = arr[mid:]

        # Sorting the first half
        merge_sort(left_part)

        # Sorting the second half
        merge_sort(right_part)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1


arr = [9, 7, 0, -6, -4, 1, 4, 3, 100, 10, 30]
merge_sort(arr)
print('Sorted list is : ', end=' ')
for i in arr:
    print(i, end='  ')
