length = float(input("Enter the length in cm: "))

if length < 42:
    print("Release the fish back into lake.")
    print("The fish is", 42 - length, "cm too short.")
else:
    print("You can keep  fish.")