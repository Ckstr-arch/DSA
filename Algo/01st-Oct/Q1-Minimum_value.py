arr = [25, 12, 58, 21, 46, 7]
min = arr[0]

for i in range(1,len(arr)):
    if arr[i] < min:
        min = arr[i]

print("Minimum value in the array is:", min)