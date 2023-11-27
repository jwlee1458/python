scores = [10.0, 9.0, 9.5, 7.1, 5, 8.0]

print(f"제거전 {scores}")
scores.remove(max(scores))
scores.remove(min(scores))
print(f"제거후 {scores}")

print(f"합 {sum(scores)}")
print(f"평균값 {sum(scores)/len(scores)}")