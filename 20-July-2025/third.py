numList = []
for i in range(10):
    x = int(input("Enter number: "))
    numList.append(x)

print("Numbers in the list:", numList)

print("Numbers from largest to smallest:")
tempList = numList.copy()
for n in range(10):
    mx = -float('inf')
    idx = -1
    for i in range(len(tempList)):
        if tempList[i] > mx:
            mx = tempList[i]
            idx = i
    print(mx, end=' ')
    tempList[idx] = -float('inf')

print()  # for newline

mx = -1
for k in range(10):
    if numList[k] > mx:
        mx = numList[k]
    print("k = ", k, "numList[k] = ", numList[k], "mx = ", mx)
