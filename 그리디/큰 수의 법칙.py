"""
"문제 풀이 아이디어"
-> 가장 큰 수와 두 번째로 큰 수만 저장 후 '가장 큰 수를 K번 더한 후 두 번째로 큰 수를 한 번 더하는 연산' 반복.

"""

# N, M, K를 공백으로 구분해 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분해 입력받기
Num = list(map(int, input().split()))
#입력 받은 수 내림차순으로 정렬하기
Num_S = sorted(Num)

result = 0

while True:
	for i in range(K):  # 가장 큰 수를 K번 더하기
		result += Num_S[N - 1]
		M -= 1  # 더할 때마다 1씩 빼기
		if M == 0:  # M이 0이라면 반복문 탈출
			break
	if M == 0:
		break
	result += Num_S[N - 2]  # 두 번째로 큰 수를 한 번 더하기
	M -= 1
	if M == 0:
		break

print(result)

#해설1 - 단순히 풀기
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
	for i in range(k):
		if m == 0:
			break
		result += first
		m -= 1
	if m == 0:
		break
	result += second
	m -= 1

print(result)

#해설2 - 귀납적으로 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1) * k)
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
