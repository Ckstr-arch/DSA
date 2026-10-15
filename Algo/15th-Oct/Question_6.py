arr = [5, 12, 18, 24, 31, 37, 43, 49, 56, 62, 68, 74, 81, 87, 93]

user_query = int(input("Target: "))

def binary_search(arr, target):
    comp = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        comp += 1
        mid = (low + high) // 2

        print("Current middle value:", arr[mid])

        if arr[mid] == target:
            return mid, comp

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comp

index, comp = binary_search(arr, user_query)

if index == -1:
    print("Number not Found")
else:
    print(f"et voilà! Target found at index {index}")

print(f"Total comparisons: {comp}")