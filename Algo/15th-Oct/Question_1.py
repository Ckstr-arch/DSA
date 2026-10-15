arr = [35, 18, 62, 9, 47, 25]
n = len(arr)

def liear_search(arr):
    min_index = 0
    for i in range(1,n):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

print("Minimum Index: ", liear_search(arr))