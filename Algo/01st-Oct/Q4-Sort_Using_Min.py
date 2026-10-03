def selection_sort_with_min(arr):
    n = len(arr)
    for i in range(n - 1):
        min_val = min(arr[i:])
        
        min_index = i + arr[i:].index(min_val)
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

test_arr = [42, 17, 35, 17, 63, 8, 42, 25]

sorted_arr = selection_sort_with_min(test_arr.copy())
print("Sorted Array:", sorted_arr)
