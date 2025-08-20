numList = []
for i in range(10):
    x = int(input("Enter number: "))
    numList.append(x)

print(numList)

mx = -1
for k in range(10):
    if numList[k] > mx:
        mx = numList[k]
        mi = k
    print("k = ", k, "numList[k] = ", numList[k], "mx = ", mx)

print("Max num =", mx)

temp = numList[0]
numList[0] = mx
numList[mi] = temp

print(numList)