gender = input("Enter your gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin level (g/L): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin is low")
    elif hemoglobin <= 155:
        print("Hemoglobin is normal")
    else:
        print("Hemoglobin is high")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin is low")
    elif hemoglobin <= 167:
        print("Hemoglobin is normal")
    else:
        print("Hemoglobin is high")

else:
    print("Invalid gender")