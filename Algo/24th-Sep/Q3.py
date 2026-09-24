arr = []
size = 6

def ENQUEUE(value):
    if len(arr) < size:
        arr.append(value)
        print(arr)
    else:
        print("Queue is Full!")

def DEQUEUE():
    if len(arr) > 0:
        arr.pop(0)
        print(arr)

def PEEK():
    if len(arr)>0:
        print(arr[0])

ENQUEUE(5)
ENQUEUE(15)
ENQUEUE(25)
DEQUEUE()
ENQUEUE(35)
ENQUEUE(45)
DEQUEUE()
ENQUEUE(55)
PEEK()
ENQUEUE(65)