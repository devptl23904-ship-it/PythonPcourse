numbers = []

while True:
    num = input("Enter number: ")

    if num == "":
        break

    numbers.append(int(num))

numbers.sort(reverse=True)

print(numbers[:5])