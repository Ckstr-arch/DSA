import random

Arr = []
for i in range(6):
    Arr.append(random.randint(1, 100))

print("Original Array:", Arr)

while True:
    index = int(input("Enter the index : "))
    if index >= 0 and index <= len(Arr):
        break

value = int(input("Enter the value to replace : "))

Arr[index] = value

print("Updated Array:", Arr)