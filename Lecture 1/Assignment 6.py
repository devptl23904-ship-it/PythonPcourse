import random

code1 = ""
for i in range(3):
    code1 += str(random.randint(0, 9))

code2 = ""
for i in range(4):
    code2 += str(random.randint(1, 6))

print("3-digit lock code:", code1)
print("4-digit lock code:", code2)