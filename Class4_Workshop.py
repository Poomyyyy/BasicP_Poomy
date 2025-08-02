movie = [
        {'movie_name': 'F1', 'ticket_price': 200, 'genre': 'action', 'age_restriction': '13'},
        {'movie_name': 'Yourname', 'ticket_price': 300, 'genre': 'romatic', 'age_restriction': '5'},
        {'movie_name': 'top gun', 'ticket_price': 500, 'genre': 'action', 'age_restriction': '15'},
        {'movie_name': 'Citizen Dog', 'ticket_price': 150, 'genre': 'romatic', 'age_restriction': '13'},
        {'movie_name': 'sonic the hedgehog 1', 'ticket_price': 450, 'genre': 'comedy', 'age_restriction': '5'},
    ]

#def checkage():

#def calculateprice():

#def buy_tick():

def main():
    print("กด 1 เพื่อ แสดงหนังทั้งหมด กด 2 เพื่อซื้อตั๋วหนัง")
    menue = input("เลือกเมนู : ")
    if menue == '1':
        show_mov()
    elif menue == '2':
        print("test")
    else:
        print("เมนูไม่ถูกต้อง")

def show_mov():
    for name_mov in movie :
        print(name_mov["movie_name"])
def buy_tick():
    show_mov()
    userinput = input("เลือกลำดับหนัง : ")
    userage = int(input("อายุของคุณ : "))
#def checkage(userage, age_restriction):
    #if userage 
main()