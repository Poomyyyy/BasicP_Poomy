movie = [
    {'movie_name': '[1] F1', 'ticket_price': 200, 'genre': 'action', 'age_restriction': 13},
    {'movie_name': '[2] Yourname', 'ticket_price': 300, 'genre': 'romatic', 'age_restriction': 5},
    {'movie_name': '[3] top gun', 'ticket_price': 500, 'genre': 'action', 'age_restriction': 15},
    {'movie_name': '[4] Citizen Dog', 'ticket_price': 150, 'genre': 'Fantasy', 'age_restriction': 13},
    {'movie_name': '[5] sonic the hedgehog 1', 'ticket_price': 450, 'genre': 'comedy', 'age_restriction': 'G'},
]
def calculateprice(userinput, userage): #userinput = 5
    while True:
        movie_sound = int(input("เลือกพาย์ไทย [1] / Soundtrack [2] : "))
        if movie_sound == 1 :
            movie_sound = "พากย์ไทย"
            break
        elif movie_sound == 2 :
            movie_sound = "Soundtrack"
            break
    if movie[userinput - 1]["genre"] == 'Fantasy':
        Total = movie[userinput - 1]['ticket_price'] + 50
    else:
        Total = movie[userinput - 1]['ticket_price']
    print("ชื่อหนัง : " + movie[userinput - 1]['movie_name'] +  "\nราคา " + str(Total) + '\n' + movie_sound)

def buy_tick():
    show_mov()
    userinput = int(input("เลือกลำดับหนัง : "))
    userage = int(input("อายุของคุณ : "))
    checkage(userinput, userage)

def checkage(userinput, userage):
    sum_age = movie[userinput - 1]["age_restriction"]
    if sum_age == 'G' :
        calculateprice(userinput, userage)
    elif sum_age <= userage:
        calculateprice(userinput, userage)
    else:
        print("Error")
def show_mov():
    for name_mov in movie :
        print(name_mov["movie_name"])
def main():
    while True:
        print("กด 1 เพื่อ แสดงหนังทั้งหมด กด 2 เพื่อซื้อตั๋วหนัง กด 3 เพื่อยกเลิก")
        menue = input("เลือกเมนู : ")
        if menue == '1':
            show_mov()
        elif menue == '2':
            buy_tick()
            break
        elif menue == '3':
            break
        else:
            print("เมนูไม่ถูกต้อง")
main()