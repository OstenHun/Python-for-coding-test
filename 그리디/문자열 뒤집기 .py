# 내 풀이 -> 답지 보고 아이디어를 공부한 후 며칠 뒤에 다시 풀어봄
s = str(input())

cnt_0to1 = 0
cnt_1to0 = 0

if s[0] == '0':
	cnt_0to1 += 1

else:
	cnt_1to0 += 1

for i in range(len(s) - 1):
	if s[i] != s[i + 1]:
		if s[i] == '0':
			cnt_1to0 += 1
		else:
			cnt_0to1 += 1

print(min(cnt_0to1, cnt_1to0))

# 해설
data = input()
cnt0 = 0  # 전부 0으로 바꾸는 경우
cnt1 = 0  # 전부 1로 바꾸는 경우

if data[0] == '1':
	cnt0 += 1
else:
	cnt1 += 1

for i in range(len(data) - 1):
	if data[i] != data[i + 1]:
		# 다음 수에서 1로 바뀌는 경우
		if data[i + 1] == '1':
			cnt0 += 1
		# 다음 수에서 0으로 바뀌는 경우
		else:
			cnt1 += 1
print(min(cnt0, cnt1))

# ******* 생각도 못한 훨씬 좋은 알고리즘 *******
a = input()
print(max(a.count('01'), a.count('10')))

"""
-> 시간 초과 예상으로 파기
"""
"""
from collections import Counter
from bisect import bisect_left, bisect_right

s = str(input())

Z_cnt = Counter(s)['0']
O_cnt = Counter(s)['1']

result = 0

if Z_cnt <= O_cnt:
	F_ID = bisect_left(s, Z_cnt)
	L_ID = bisect_right(s, Z_cnt) - 1
	for i in range(F_ID, L_ID + 1):
		if s[i] == '0':
			s[i] = '1'
		else:
			s[i] = '0'
		result += 1

"""

#틀린 풀이.
"""
"문제 풀이 아이디어"
-> 0에서 1로 바꾸는 경우, 1에서 0으로 만드는 경우를 정할 때 
문자열 속에서 0, 1의 갯수를 비교하여 
더 적은 숫자를 다른 숫자로 바꾸게 되면 적은 횟수로 뒤집을 수 있다. 
"""
"""
s = str(input())

Z_cnt = s.count('0')
F_cnt = s.count('1')

stack_cnt = 0
change_cnt = 0

if Z_cnt <= F_cnt:
	for i in range(len(s)):
		if i == len(s) - 1:
			break
		if int(s[i]) == int(s[i + 1]) == 0:
			stack_cnt += 1
	for i in range(len(s)):
		if int(s[i]) == 0:
			change_cnt += 1

else:
	for i in range(len(s)):
		if i == len(s) - 1:
			break
		if int(s[i]) == int(s[i + 1]) == 1:
			stack_cnt += 1
	for i in range(len(s)):
		if int(s[i]) == 1:
			change_cnt += 1

answer = change_cnt - stack_cnt
print(answer)
"""
