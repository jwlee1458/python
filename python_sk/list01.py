names = ["조정원", "홍길동", "김철", "정군", "박군"]

name_input = input("추가할 이름을 적으세요.")
names.append(name_input)

for i in range(len(names)):
    print(f"{i+1}번째 이름은 {names[i]}")