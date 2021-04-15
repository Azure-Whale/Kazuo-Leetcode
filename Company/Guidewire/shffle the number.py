import random
arr = [1,2,3,4,5,6,7,8,9]

for i in range(len(arr)):
    temp = random.randint(0,len(arr)-1)
    arr[i],arr[temp] = arr[temp],arr[i]
print(arr)
random.shuffle(arr)
print(arr)