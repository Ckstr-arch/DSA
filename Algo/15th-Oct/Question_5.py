arr = [65, 42, 89, 42, 76, 55, 42, 91, 68, 42]

user_query = int(input("Enter a target to find: "))

def linear_search(arr, target):
    index = []
    comp = 0

    for i in range(len(arr)):
        comp += 1

        if arr[i] == target:
            index.append(i)

    return index, comp

index, comp = linear_search(arr, user_query)

if len(index) == 0:
    print("Number not Found")
else:
    print(f"et voilà! Target found at indices: {index}")
    print(f"Total occurrences: {len(index)}")

print(f"Total comparisons: {comp}")