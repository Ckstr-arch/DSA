arr = arr = [35, 18, 62, 9, 47, 25]


def selection_sort(arr):
    n = len((arr))
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort(arr))

user_query = int(input("Target: "))

def binary_search(arr, target):
    low = 0
    high = (len(arr)-1)
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

result = binary_search(arr, user_query)

if result == -1:
    print("Target not found!")
else:
    print(f"et voilà. Target is at {result}")