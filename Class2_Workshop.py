distance = int(input("Input the Distance : "))
total = 0
if distance < 5:
    print("Don't express ")
elif distance <= 50:
    total = 10
elif distance <= 100:
    total = 15
elif distance <= 300:
    total = 25
elif distance <= 500:
    total = 35
elif distance >= 500:
    total = 45
else:
    print("Don't express")

print("Total price",total, "Bath")