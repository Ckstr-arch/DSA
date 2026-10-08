arr = [75, 42, 89, 56, 91, 68, 33, 80]

swaps = 0

print("Original array:", arr)

for i in range(len(arr)):
    swapped = False

    for j in range(0,len(arr)-1-i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps +=1
            swapped = True

    print("After pass", i+1, "array:", arr)

    if not swapped:
        break

print("Highest Mark:",arr[0])
print("Lowest Mark:", arr[-1])
print("Sorted array:", arr)
print("Original array:", arr)
