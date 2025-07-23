MonstorA = "ไคเซน", 50

Gun = "ปืน", -30
Knife = "มีด", -20
Missile = "มิดซายด์", -100

sum = 0
while True:
    Home = int(input("ต่อสู้กับมอนเตอร์กด 1 กด 2 เพื่อออก : "))
    if Home == 1:
        print("จำนวนการตีมอนเตอร์")
        times = int(input("จำนวนการตี"))
        for i in range(times):
            print("เลือกอาวุธ")
            select_tools = int(input("1. ปืน 2.มืด, 3. มิดซายด์ : "))
            if select_tools == "ปืน" :
                sum += Gun
            elif select_tools == "มีด" :
                sum += Knife
            elif select_tools == "มิตซายด์" :
                sum += Missile
    elif Home == 2:
        break
    else:
        print("กรุณาใส่ตัวเลขอีกรอบ")
