movie = [
    {'movie_name': 'F1', 'ticket_price': 200, 'genre': 'action', 'age_restriction': 13},
    {'movie_name': 'Yourname', 'ticket_price': 300, 'genre': 'romatic', 'age_restriction': 5},
    {'movie_name': 'top gun', 'ticket_price': 500, 'genre': 'action', 'age_restriction': 15},
    {'movie_name': 'Citizen Dog', 'ticket_price': 150, 'genre': 'romatic', 'age_restriction': 13},
    {'movie_name': 'sonic the hedgehog 1', 'ticket_price': 450, 'genre': 'comedy', 'age_restriction': 'G'},
]
#def calculateprice():

def buy_tick():
    show_mov()
    userinput = int(input("เลือกลำดับหนัง"))
    userage = int(input("อายุของคุณ : "))
    checkage(userinput, userage)

def checkage(userinput, userage):
    sum_age = movie[userinput - 1]["age_restriction"]
    if sum_age == 'G' :
        calclateprice()
    elif sum_age >= userage:
        calculateprice()
    else:
        print("Error")
def show_mov():
    for name_mov in movie :
        print(name_mov["movie_name"])
def main():
    while True:
        print("กด 1 เพื่อ แสดงหนังทั้งหมด กด 2 เพื่อซื้อตั๋วหนัง")
        menue = input("เลือกเมนู : ")
        if menue == '1':
            show_mov()
        elif menue == '2':
            buy_tick()
        else:
            print("เมนูไม่ถูกต้อง")
main()
