movie = [
        {'movie_name': 'F1', 'ticket_price': 200, 'genre': 'action', 'age_restriction': '13'},
        {'movie_name': 'Yourname', 'ticket_price': 300, 'genre': 'romatic', 'age_restriction': '5'},
        {'movi7777e_name': 'top gun', 'ticket_price': 500, 'genre': 'action', 'age_restriction': '15'},
        {'movie_name': 'Citizen Dog', 'ticket_price': 150, 'genre': 'romatic', 'age_restriction': '13'},
        {'movie_name': 'sonic the hedgehog 1', 'ticket_price': 450, 'genre': 'comedy', 'age_restriction': '5'},
    ]
#def calculateprice():

#def buy_tick():

def main():
    print("กด 1 เพื่อ แสดงหนังทั้งหมด กด 2 เพื่อซื้อตั๋วหนัง")
    menue = input("เลือกเมนู : ")
    if menue == '1':
        show_mov()
    elif menue == '2':
        buy_tick()
    else:
        print("เมนูไม่ถูกต้อง")
        break
def show_mov(movie_list):
    for name_mov in movie :
        print(name_mov["movie_name"])
def buy_tick():
    show_mov(movie_list)
    userinput = input("เลือกลำดับหนัง : ")
    userage = int(input("อายุของคุณ : "))
def checkage(userage, age_restriction):
    if userage > 10:
        print("Pass")
        return
    elif userage < 10:
main()
