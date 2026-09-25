queue = []
stack = []
processed = []
a = 0

def Enqueue(value):
    queue.append(value)

def Dequeue():
    if len(queue) > 0:
        global a
        a = queue.pop(0)
        processed.append(a)
        return a
    else:
        print("Queue is empty!")

def Push(value):
    stack.append(value)

def POP():
    if len(stack) > 0:
        global a
        a = stack.pop()
        return a
    else:
        print("Stack is empty!")

def remove_customer(inquiry):
    if inquiry in queue:
        queue.remove(inquiry)
        stack.append(inquiry)

Enqueue(201)
Enqueue(202)
Enqueue(203)
Enqueue(204)
Enqueue(205)

#print(queue)
Dequeue()
print(f"Served : Customer #{a}")
Dequeue()
print(f"Served : Customer #{a}")


inquiry = int(input("Enter the customer number to remove: "))
remove_customer(inquiry)

#print(stack)
#print(queue)
#print(processed)

Dequeue()
print(f"Served : Customer #{a}")

Enqueue(206)
inquiry = int(input("Enter the customer number to remove: "))
remove_customer(inquiry)

print(f"Cancelled: {stack}")
print(f"Remaining: {queue}")
print(f"Processed: {processed}")

POP()

print(f"Recently cancelled order: {a}")
print(f"Remaining cancelled orders: {stack}")
print(f"Final active orders in queue: {queue}")