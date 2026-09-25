stack1 = [12, 25, 38, 41, 56]
stack2 = [12, 25, 38, 41, 60]
result = True

def Pop():
    if len(stack1) > 0 and len(stack2) > 0:
        a = stack1.pop() 
        b = stack2.pop()         
        print(f"Stack#1: {stack1}, Stack#2: {stack2}")
        return a, b

print(f"Initial Stack#1: {stack1}")
print(f"Initial Stack#2: {stack2}")

while len(stack1) > 0 and len(stack2) > 0:
    a, b = Pop()  # Capture the popped values here
    if a != b:
        result = False

if len(stack1) != len(stack2):
    result = False

print(f"Stack 1 and Stack 2 is Equal: {result}")