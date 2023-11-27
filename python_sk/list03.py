#성적 입력 프로그램 제작
#학생 5명의 성적을 입력
#성적 합, 최고점수, 최저점수, 평균값
#80점 이상 사용자 수치 (count)

STUDENTS = 5
scores = []
count = 0

for i in range(STUDENTS):
    value = int(input(f"{i+1}번째 성적을 입력하세요."))
    scores.append(value)
    if value >= 80:
        count = count + 1

print(f"합 {sum(scores)}")
print(f"최고점수 {max(scores)}")
print(f"최소점수 {min(scores)}")
print(f"평균값 {sum(scores)/len(scores)}")
print(f"80점 점수 이상 = {count}명")