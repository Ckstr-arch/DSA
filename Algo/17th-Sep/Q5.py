import random

Arr1 = []
for i in range(10):
    Arr1.append(random.randint(1, 100))

Arr2 = []
for i in range(10):
    Arr2.append(random.randint(1, 100))

print("Original Array _ 1:", Arr1)
print("Original Array _ 2:", Arr2)

for i in range(len(Arr1)):
    Arr1.append(Arr2[i])

print("Updated Array _ 1:", Arr1)