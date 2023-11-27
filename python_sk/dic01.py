#커피(음식) 주문 프로그램
#음식 : 가격 정해짐
#메뉴를 주문 -> 가격을 가져와야함!
#돈을 입금 -> 잔금을 확인!

menus = {
    "아메리카노": 4000,
    "카페라떼" : 5000,
    "카푸치노" : 5000,
    "바닐라라떼" : 5500,
}

print(f"=====메뉴 리스트=====")
for name, price in menus.items():
    print(f"{name} : {price}원")

selected_menu = input("주문할 메뉴를 입력하세요.")
money = int(input("돈을 입금하세요."))

price = menus.get(selected_menu, 0)

if price == 0:
    print("잘못된 메뉴입니다.")
else:
    change = money - price
    if change >= 0:
        print(f"{selected_menu}를 구매. 거스름돈은 {change}입니다.")
    else:
        print(f"돈이 부족합니다.")