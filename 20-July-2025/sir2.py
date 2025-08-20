numList = []
for i in range(10):
    x = int(input("Enter number: "))
    numList.append(x)

print("Numbers in the list:", numList)

k = 0; mx = -1
while k < 10:
    if numList[k] > mx:
        mx = numList[k]
    print("k = ", k, "numList[k] = ", numList[k], "mx = ", mx)
    k += 1

print("Max number is:", mx)