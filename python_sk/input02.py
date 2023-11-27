name = input("이름을 입력하세요.")
phone = input("전화번호를 입력하세요.")
age = int(input("나이를 입력하세요."))


#일반적인 출력
print(name, "의 전화번호는", phone, "이고 나이는", age, "입니다.")

#formant
print("{}의 전화번호는 {}이고, 나이는 {}입니다.".format(name, phone, age))

#f-string
print(f"{name}의 전화번호는 {phone}이고, 나이는 {age}입니다.")