#----------- Function----------
# def Hello() :
#     print("Test")
# for i in range(5):
#     Hello()
#----------- Function----------
# def add(a, b):
#     ans = a + b
#     print(ans)

# add(3, 5)
#----------- Function----------
# def introduction (name):
#     print("myname is", name)
#     tellage()

#----------- Function----------
# def tellage():
#     age = input("Enter your age : ")
#     print("You age is : ", age)
# introduction ("Poom")

#----------- Function (input) ----------
# ฟังชั่นตัวนึงที่ Spam จะรับ 1 parametter สิ่งที่ ฟังชั่นทำคือ ปริ้นท์ข้อความมา 5 ครั้ง โดยใช้ For loop
# import time
# def spam(text):
#     round = int(input("ใส่จำนวนรอบ : "))
#     for i in range(1, round+1):
#         print("จำนวนรอบ : ", i, "ข้อความ",text)
#         time.sleep(0.5)

# spam("Hi")
#----------- Function (input) ----------
# a = 1
# b = 2
# def kak(a, b):
#     return a+b
# print(kak(a, b))
#----------- List ----------
# x = ["Poom", "PP", 8, 9]
# x[1] = 3
# sum = x[2] + x[1]
# print(sum)
# x[0] = "๕๕๕"
# print(x)
# x.append(10)
# x.append()
# print(x)
#----------- List (pop) ----------
# list = ["Poom", "PP", 8, 9]
# for i in (list):
#     if i == 8:
#         print("See 8!!")
#         break
#     else:
#         print("IDK")
#----------- Dict -----------
# Dee = {
#     'Car' : 'Toyota',
#     'Mouse' : 'logitec'
# }
# Dee['Car'] = "Subaru"
# print(Dee)
# #----------- Dict -----------
data = [
    {"Name" : "Poom", "money" : 1000},
    {"Name" : "Keyes", "money" : 2000},
    {"Name" : "อุอิอา", "money" : 1000000}
]
def checkmoney(liststudent):
    for data in liststudent :
        if data["money"] > 1000:
            print(data["Name"], "รวย")
        elif data["money"] < 100000:
            print(data["Name"], "เด็ไปไอ้น้อง")
        else:
            print(data["Name"], "เรามันคนจน")
checkmoney(data)