menu = [
    {"id": 1, "fav": "Classic", "price": 30},
    {"id": 2, "fav": "Chocolate", "price": 45},
    {"id": 3, "fav": "Strawberry", "price": 50}
]

fav = []

print("Welcome to LungPond Square - Favor list\n---------------------------------------")
for menus in menu:
    print(menus["id"], menus["fav"], menus["price"])

def orders():
    order = int(input("สั่งไรดีครับ: "))
    if order == 1:
        return "Classic  30 Bath"
    if order == 2:
        return "Chocolate  45 Bath"
    if order == 3:
        return "Strawberry  50 Bath"
def main(): #takaa
    while True:
        fav.append(orders())
        add = str(input("สั่งเพิ่มไหม [y/N]"))
        if add == 'N':
            break
        
    print("Odered list\n------------------------------")
    for i in fav:
        print(i)

main()


        