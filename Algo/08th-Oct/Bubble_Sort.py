import random

arr = []
swaps = 0

for i in range(8):
    arr.append(random.randint(1, 100))

print("Original array:", arr)

for i in range(len(arr)):
    swapped = False

    for j in range(0, len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
            swapped = True

    print("After pass", i+1, "array:", arr)

    if not swapped:
        print("Array is already sorted!")
        break

print("Sorted array:", arr)
print("Number of swaps:", swaps)