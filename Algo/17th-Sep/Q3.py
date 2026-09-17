import random

arr = []

for i in range(8):
    arr.append(random.randint(1, 100))

print("Original Array:", arr)

while True:
    index = int(input("Enter the index : "))
    if index >= 0 and index <= len(arr):
        break
for j in range(index, len(arr)-1):
    arr[j] = arr[j+1]

arr.pop()

print("Updated Array:", arr)