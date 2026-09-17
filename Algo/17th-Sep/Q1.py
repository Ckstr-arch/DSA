import random

Arr = []
for i in range(10):
    Arr.append(random.randint(1, 100))

print("Original Array:", Arr)

for j in range(len(Arr)):
    print(f"Element at index {j}: {Arr[j]}")