tokens = [101, 102, 103, 104, 105]
size = 5
tot = 0

def put(value):
    if len(tokens) < size:
        tokens.append(value)
    else:
        print("Queue is Full!!")

def get():
    if len(tokens)<0:
        a = tokens.pop(0)
        print(a)
        tot += 1
    return tot

print(f"Current Queue size: {len(tokens)}")

put(101)
put(102)
put(103)
put(104)
put(105)

get()
get()

print(tokens)
print(f"Remaining customers: {len(tokens)}")