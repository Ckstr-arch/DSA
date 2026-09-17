import random

cart = []

for i in range(5):
    cart.append(random.randint(1, 100))

print("Original Cart:", cart)

while True:
    index = int(input("Enter the index : "))
    if index >= 0 and index <= len(cart):
        break

qnt = int(input("Enter the quantity to be changed : "))

cart[index] = qnt

res = input("Do you wanna add another item to the cart (y/n) : ")
if res.lower() == 'y':
    item = int(input(""))