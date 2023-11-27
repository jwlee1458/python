menus = {
    "아메리카노": 4000,
    "카페라떼" : 5000,
    "카푸치노" : 5000,
    "바닐라라떼" : 5500,
}

selected_menu = input("주문할 메뉴를 입력하세요.")

if selected_menu in menus:
    price = menus[selected_menu]
    print(f"{price}")