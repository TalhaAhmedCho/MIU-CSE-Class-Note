numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort()
print("Numbers in the list (sorted):", numbers)