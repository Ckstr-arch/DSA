"""tokens = []
size = 5
tot = 0 

def put(value):
    if len(tokens) < size:
        tokens.append(value)
    else:
        print("Queue is Full!!")

def get():
    if len(tokens)>0:
        a = tokens.pop(0)
        print(f"Served : Customer #{a}")
        global tot
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

#print(tot)
print(tokens)
print(f"Remaining customers: {len(tokens)}")

put(106)
print(f"Updated Queue: {tokens}")
"""
import queue

# 1. Create a queue with a maximum size of 5
tokens = queue.Queue(maxsize=5)

# 3. Display current queue size (before adding)
print(f"Current Queue size: {tokens.qsize()}")

# 2. Add five customer tokens using put()
for token in [101, 102, 103, 104, 105]:
    tokens.put(token)

# 4 & 5. Serve first two customers using get() and display token numbers
print(f"Served : Customer #{tokens.get()}")
print(f"Served : Customer #{tokens.get()}")

# 6. Display all remaining customers in the queue
print(f"Remaining customers: {list(tokens.queue)}")

# 7. Display current queue size after serving
print(f"Current Queue size after serving: {tokens.qsize()}")

# 8. Add a new customer with token number 106
tokens.put(106)

# 9. Display updated queue
print(f"Updated Queue: {list(tokens.queue)}")