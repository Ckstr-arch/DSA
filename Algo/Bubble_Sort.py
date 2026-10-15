arr = [5,10,4,12,8]

n = len(arr)

while sorted:
   sorted = False
   for i in range(0,n-1):
      for j in range(0,n-1-i):
          if arr[i] > arr[i+1]:
              arr[i],arr[i+1]=arr[i+1],arr[i]
              sorted = True

print(arr)