MonstorA = 50

Gun = 30
Knife = 20
Missile = 100

while True:
    Home = int(input("ต่อสู้กับมอนเตอร์กด 1 กด 2 เพื่อออก : "))
    if Home == 1:
        times = int(input("จำนวนการตีมอตเตอร์ : "))
        for i in range(times):
            print("เลือกอาวุธ")
            select_tools = input("1. ปืน 2.มืด, 3. มิดซายด์ : ")
            if select_tools == "1" :
                MonstorA -= Gun
            elif select_tools == "2" :
                MonstorA -= Knife
            elif select_tools == "3" :
                MonstorA -= Missile
            else:
                print("คุณไม่เลือกอาวุธ")
            if MonstorA == 0:
                print("มอนเตอร์ตาย")
                break
            elif MonstorA < 0  :
                MonstorA = 20
                print("มอนเตอร์ได้รับเลือดเพิ่ม", MonstorA)
        if MonstorA > 0:
            print("END GAME ผู้เล่นตาย")  
            break 
        break
    elif Home == 2:
        break
    else:
        print("กรุณาใส่ตัวเลขอีกรอบ")