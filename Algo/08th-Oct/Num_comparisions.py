arr = [25, 17, 31, 13, 2, 45, 8]

comparisons = 0
swaps = 0

for i in range(len(arr)):
    swapped = False

    for j in range(0, len(arr)-1-i):
        comparisons += 1
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
            swapped = True

    if not swapped:
        break

print("Sorted array:", arr)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)
