arr = [25, 12, 58, 21, 46, 7]

n = len(arr)

for i in range(n):
    # Find minimum value in the unsorted portion
    minimum = min(arr[i:])

    # Find the index of that minimum value
    min_index = arr.index(minimum, i)

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:", arr)