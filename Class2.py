# loading....
distance = int(input("Input the distance : "))
sum = 0
if distance < 5 :
    print("No Servrice")
elif distance < 50 :
    sum += 10
elif distance < 100 :
    sum += 15
elif distance < 300 :
    sum += 25
elif distance < 500 :
    sum += 35
else:
    sum == 45
print(sum)