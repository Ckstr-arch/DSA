"""string = input("Enter a string: ").strip()

arr = []
reversed = []
size = len(string)

def PUSH(char):
    if len(arr) <size:
        arr.append(char)


def POP():
    if len(arr) > 0:
        reversed.append(arr.pop())

for i in range (len(string)):
    PUSH(string[i])

for i in range((len(arr)),0, -1):
    POP()

print(reversed)
"""
#is this the most optimal algorithm ?
#No, Two pointer approach is more optimal than this one. This is just a stack implementation of the same problem.
string = input("Enter a string: ").strip()

# Convert string to a list to allow character swapping
chars = list(string)

left = 0
right = len(chars) - 1

# Swap elements from both ends moving towards the middle
while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1

# Reconstruct the reversed string
reversed_string = "".join(chars)
print(reversed_string)