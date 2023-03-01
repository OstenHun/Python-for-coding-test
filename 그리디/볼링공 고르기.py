"""
'문제 풀이 아이디어'
-> 두 사람이 서로 무게가 다른 볼링공을 고른다. 무작위의 무게가 순서대로 주어진다. 서로 다른 N개의 볼링공 중 2개를 조합하는 갯수에서 서로 같은 무게의 볼링공을 고를 경우의 수를 구해 빼주면 두 사람이 볼링공을 고르는 경우의 수.
"""
# 내 풀이 >> 수학적 풀이; 프로그래밍적으론 좋지 않다고 판단; n, m의 값을 전혀 사용하지 않음.
from itertools import combinations

n, m = map(int, input().split())

L = list(map(int, input().split()))

L_S = set(L)	# 집합화 해 겹치는 무게의 볼링 삭제

num = len(list(combinations(L, 2)))		# n개의 서로 다른 볼링공 중 2개를 선택하는 조합의 수

result = num - (len(L) - len(L_S))	# n개 중 2개 선택하는 조합 수 - n개 중 같은 무게의 볼링공을 선택하는 조합의 수

print(result)	# 두 사람이 서로 다른 무게의 볼링공을 고르는 경우의 수


# ***해설***
n, m = map(int, input().split()) 
data = list(map(int, input().split())) 

# 1부터 10까지의 무게를 담을 수 있는 리스트 
array = [0] * 11 

for x in data:
	# 각 무게에 해당하는 볼링공의 개수 카운트
	array[x] += 1 

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
	n -= array[i] 	# 무게에 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result) 
