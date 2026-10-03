def is_balanced(expression: str) -> bool:
    stack = []
    # Map each closing bracket to its corresponding opening bracket
    bracket_map = {")": "(", "}": "{", "]": "[", ">": "<"}
    opening_brackets = set(bracket_map.values())

    for char in expression:
        if char in opening_brackets:
            stack.append(char)  # Push opening brackets onto the stack
        elif char in bracket_map:
            # If it's a closing bracket, it must match the top of the stack
            if not stack or stack.pop() != bracket_map[char]:
                return False
                
    # If the stack is empty, all brackets were perfectly matched
    return len(stack) == 0

# --- Test execution ---
txt = input("Enter a string: ").strip()

if is_balanced(txt):
    print("Balanced")
else:
    print("Not Balanced")
