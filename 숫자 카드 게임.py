"""
"문제 풀이 아이디어"
-> '각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수' 찾기

"""

# 내 풀이
N, M = map(int, input().split())  # N행, M열 입력받기

L = []

num = []

for _ in range(N):
	L.append(list(map(int, input().split())))  # L 배열에 입력받은 수 대입.

for j in range(N):  # 입력 받은 수 중 행 별로 가장 작은 수 num 배열에 저장.
	num.append(min(L[j]))

print(max(num))  # 행 별 가장 작은 수들 중 가장 큰 수 출력.


# 해설1 - min() 함수를 이용
n, m = map(int, input().split())

result = 0
#한 줄씩 입력받아 확인
for _ in range(n):
	data = list(map(int, input().split()))
	# 현재 줄에서 '가장 작은 수 찾기'
	min_value = min(data)
	# *** '가장 작은 수'들 중에서 가장 큰 수 찾기 ***
	result = max(result, min_value)

print(result) 


# 해설2 - 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split()) 

result = 0 

for _ in range(n):
	data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
		min_value = min(min_value, a) 
    # *** '가장 작은 수'들 중에서 가장 큰 수 찾기 ***
    result = max(result, min_value) 

print(result) 
