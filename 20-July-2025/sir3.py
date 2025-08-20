numList = []
for i in range(10):
    x = int(input("Enter number: "))
    numList.append(x)

print("Numbers in the list:", numList)

mx = -1
for k in range(10):
    if numList[k] > mx:
        mx = numList[k]
    print("k = ", k, "numList[k] = ", numList[k], "mx = ", mx)

print("Max number is:", mx) 