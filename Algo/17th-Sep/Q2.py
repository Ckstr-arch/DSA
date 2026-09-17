import random

arr = []
for i in range(10):
    arr.append(random.randint(1, 100))

print("Original Array:", arr)

while True:
    index = int(input("Enter the index : "))
    if index >= 0 and index <= len(arr)+1:
        break

value = int(input("Enter the value to insert : "))

for j in range(len(arr)-1, index-1, -1):
    arr[j] = arr[j-1]

arr[index] = value

print("Updated Array:", arr)