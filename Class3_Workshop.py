MonstorA = "ไคเซน", 50

Gun = "ปืน", -30
Knife = "มีด", -20
Missile = "มิดซายด์", -100

sum = 0
while True:
    Home = int(input("ต่อสู้กับมอนเตอร์กด 1 กด 2 เพื่อออก : "))
    if Home == 1:
        print("จำนวนการตีมอนเตอร์")
        times = int(input("จำนวนการตี : "))
        for i in range(times):
            print("เลือกอาวุธ")
            select_tools = input("1. ปืน 2.มืด, 3. มิดซายด์ : ")
            if select_tools == "1" :
                sum += -30
            elif select_tools == "2" :
                sum += -20
            elif select_tools == "3" :
                sum += -100
        if sum == -50 and -100 :
            print("คุณชนะ")
        else:
            if sum >= 20:
                print("Test")
    elif Home == 2:
        break
    else:
        print("กรุณาใส่ตัวเลขอีกรอบ")