a = "파이썬"
b = 15
c = str(b)

#일반적인 출력!!
print(a)
print(b)

print(type(a))
print(type(b))
print(a, "이 좋아요", b, "번 공부했어요.")
#format
print("{}이 좋아요, 그래서 {}번 공부했어요".format(a, b))

#f-string
print(f"{a}가 좋아요. 그래서 {b}번 공부했어요.")