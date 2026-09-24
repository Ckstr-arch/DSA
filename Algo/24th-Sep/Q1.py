"""stack = []
size = 6

# Push
stack.append(15)
stack.append(25)
stack.append(35)
print("Stack: ", stack)

# Pop
stack.pop()
print("Stack after Pop: ", stack)

#push
stack.append(45)
stack.append(55)
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
stack.pop()
print("Stack after Pop: ", stack)

# Puah
stack.append(55)
print("Stack: ", stack)
"""
stack = []
size = 6

# Better Implementation
def Push(value):
    if len(stack) < size:
        stack.append(value)
        print(f"Stack: {stack}")
    else:
        print("Stack is Full!")


def Pop():
    if len(stack) > 0:
        stack.pop()
        print(f"Stack after Pop: {stack}")
    else:
        print("Stack is Empty!")


def Peek():
    if len(stack) > 0:
        print(f"Top Element: {stack[-1]}")
    else:
        print("Stack is Empty!")


print("\n")

Push(15)
Push(25)
Push(35)
Pop()
Push(45)
Push(55)
Peek()
Pop()
Push(65)