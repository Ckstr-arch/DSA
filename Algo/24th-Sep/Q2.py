stack1 = [12, 25, 38, 41, 56]
stack2 = [12, 25, 38, 41, 60]

for _ in range(len(stack1)):
    a = stack1.pop()
    print(f"Stack1: {stack1}")
    b = stack2.pop()
    print(f"Stack2: {stack2}")
    if a == b:
        print("Same Element is being Poped!!, Stacks are equal so far!!!!")
    else:
        print("Different values!")
