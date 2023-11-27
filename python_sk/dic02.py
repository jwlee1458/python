#커피(음식) 주문 프로그램
#음식 : 가격 정해짐
#메뉴를 주문 -> 가격을 가져와야함!
#여러 메뉴를 담아 둔 후에 결제! -> list()
#돈을 입금 -> 잔금을 확인!

menus = {
    "아메리카노": 4000,
    "카페라떼": 4500,
    "카푸치노": 4800,
    "바닐라라떼": 5000,
}

print("=====메뉴=====")
for name, price in menus.items():
    print(f"{name}: {price}원")

order_list = []

while True:
    selected_menu = input("주문할 메뉴를 입력하세요")
    if selected_menu =='q':
        break
    else:
        order_list.append(selected_menu)

total_price = 0
#for menu_name in order_list:
#    total_price = total_price + menus[menu_name]

total_price = sum(menus[menu_name] for menu_name in order_list)

money = int(input(f"총 금액은 {total_price}입니다. 돈을 넣어주세요."))
print(f"거스름돈은 {money - total_price}입니다.")