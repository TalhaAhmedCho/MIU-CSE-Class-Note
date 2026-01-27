numList = []
for i in range(10):
    x = int(input("Enter number: "))
    numList.append(x)

for i in range(10):
    z = numList[i]
    y = z * z
    numList[i] = y

numList.sort(reverse=True)
print("Numbers from largest to smallest:", numList)
  
print("Numbers in the list after squaring:", numList)