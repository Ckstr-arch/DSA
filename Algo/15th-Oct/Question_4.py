arr = [5, 12, 18, 23, 29, 34, 41, 47, 53, 58, 64, 69, 72, 78, 83, 87, 91, 95, 98, 100]

user_query = int(input("Target: "))

def binary_search(arr, target):
    comp = 0
    low = 0
    high = len(arr)-1

    while low <= high:
        comp +=1
        mid = (low + high) // 2

        if arr[mid] == target:
            return (f"Position: {mid} # Comparisions: {comp}")
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