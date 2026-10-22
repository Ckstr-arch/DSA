#Basic Palindrome Checking
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