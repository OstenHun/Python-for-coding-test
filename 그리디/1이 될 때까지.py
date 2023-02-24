"""
"문제 풀이 아이디어"
-> 최소의 횟수로 N을 1로 만들어야 하므로 '최대한 많이 나누기'를 수행하면 된다.
2023.02.24
"""

# 내 풀이
n, k = map(int, input().split()) 

result = 0

while n > 1:	# n이 1이 될 때까지 반복.
	if n % k == 0:	# n이 k로 나누어 떨어질 때부터 나누기만 진행하면 '최대한 많이 나누기' 수행 가능.
		n = n // k 
		result += 1 
	
	else:	# n이 k로 나누어 떨어지기 전까지 1씩 빼주기.
		n -= 1
		result += 1 

print(result)	# 수행 횟수 출력.


#해설 1- 단순하게 푸는 답안 예시
n, k = map(int, input().split())
result = 0

#N이 K 이상이라면 K로 계속 나누기
while n >= k:
	# N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
	while n % k != 0:
		n -= 1
		result += 1
	# K로 나누기
	n //= k
	result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
	n -= 1
	result += 1

print(result) 


# 해설 2
n, k = map(int, input().split()) 
result = 0

while True:
	#(N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
	target = (n // k) * k
	result += (n - target)
	n = target 
	# N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출 
	if n < k:
		break
	# K로 나누기
	result += 1
	n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result) 
