numbers = []

while True:
    num = input("Enter a number: ")

    if num == "":
        break

    numbers.append(float(num))

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers entered.")