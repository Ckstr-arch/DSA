print("STACK APPLICATIONS\n")
print("1. Check Palindrome \n2. Check Balanced Brackets\n3. Exit")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        user_input = input("Enter a string to check if it's a palindrome: ").strip().lower()
        user_input = user_input.replace(" ", "")
        
        for char in ".,/{()}[]|*&!~`#$%^":
            user_input = user_input.replace(char, "")
        
        arr = list(user_input)
        
        def PUSH(arr):
            reverse_arr = []
            n = len(arr)
            for i in range(n-1,-1,-1):
                reverse_arr.append(arr[i])
            return reverse_arr
        
        reverse_arr = PUSH(arr)
        
        def is_Palindrome(arr, reverse_arr):
            if arr==reverse_arr:
                return True
            else:
                return False
        
        print(f"{user_input} is a palindrome: {is_Palindrome(arr, reverse_arr)}")

    case 2:
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

    case 3:
        exit()

    case _:
        print("Invalid Choice")