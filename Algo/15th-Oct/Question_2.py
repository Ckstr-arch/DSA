arr = [35, 18, 62, 9, 47, 25]
n = len(arr)

#User Query
target = float(input("Enter a target to remove: "))

def liear_search(arr, target):
    for i in range(n):
        if arr[i] == target:
            arr.pop(i)
            return arr
    return -1

result = liear_search(arr, target)

if result == -1:
    print("Target Not Found")
else:
    print("et voilà")