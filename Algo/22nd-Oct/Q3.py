# Balanced Parentheses
user_input = input("Enter an expression: ").strip()
arr = list(user_input)

def PUSH(stack, char):
    stack.append(char)

def POP(stack):
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def is_Balanced(arr):
    stack = []

    for i in range(len(arr)):
        if arr[i] in "({[":
            PUSH(stack, arr[i])

        elif arr[i] in ")}]":
            top = POP(stack)

            if top == -1:
                return False
            if arr[i] == ")" and top != "(":
                return False
            if arr[i] == "}" and top != "{":
                return False
            if arr[i] == "]" and top != "[":
                return False
            

    if len(stack) == 0:
        return True
    else:
        return False

if len(arr) == 0:
    print("Input an Expression")
elif is_Balanced(arr):
    print("The Expression is Balanced")
else:
    print("The Expression is not Balanced")