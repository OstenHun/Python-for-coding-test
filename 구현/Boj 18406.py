"""
"문제 풀이 아이디어"
-> 중간을 기준으로 왼쪽의 합, 오른쪽의 합을 비교한다.
문자열로 입력받은 후 정수형으로 변환하여 계산
"""
# 내 풀이
n = str(input())
R_sum = 0
L_sum = 0
LEN = len(n)
for i in range(LEN // 2):
	L_sum += int(n[i])

for j in range(LEN // 2, LEN):
	R_sum += int(n[j])

if L_sum == R_sum:
	print("LUCKY")

else:
	print("READY")

# 해설
n = input()
length = len(n)	# 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
	summary += int(n[i])

for j in range(length // 2, length):
	summary -= int(n[j])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
	print("LUCKY")

else:
	print("READY")