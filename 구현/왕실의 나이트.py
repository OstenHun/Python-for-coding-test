"""
문제 풀이 아이디어
-> 8 x 8 체스판에서 각 칸 별로 나이트가 갈 수 있는 경우의 수를 모두 구했다.
"""
# 내 풀이 -> 그다지 좋은 풀이는 아니라고 생각한다.
L = str(input())

if (L[0] == 'c' or L[0] == 'd' or L[0] == 'e' or L[0]
    == 'f') and (L[1] == '3' or L[1] == '4' or L[1] == '5' or L[1] == '6'):
	print(8)

elif (L[0] == 'b' or L[0] == 'g') and (L[1] == '3' or L[1] == '4'
                                       or L[1] == '5' or L[1] == '6'):
	print(6)

elif (L[1] == '2' or L[1] == '7') and L[0] == ('c' or L[0] == 'd'
                                               or L[0] == 'e' or L[0] == 'f'):
	print(6)

elif (L[0] == 'a' or L[0] == 'h') and L[1] == '3' or (L[1] == '4' or L[1]
                                                      == '5' or L[1] == '6'):
	print(4)

elif (L[1] == '1' or L[1] == '8') and (L[0] == 'c' or L[0] == 'd'
                                       or L[0] == 'e' or L[0] == 'f'):
	print(4)

elif L == 'b2' or L == 'b7' or L == 'g2' or L == 'g7':
	print(4)

elif L == 'a1' or L == 'h1' or L == 'a8' or L == 'h8':
	print(2)

else:
	print(3)

# 해설
# -> 나이트의 이동 경로를 steps 변수에 넣어 steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] 에서 출발
# 나이트가 이동할 수 있는 경로를 steps 변수에 하나씩 담고 이 8가지 경우의 수를 반복문을 이용해 하나씩 검사한다. cnt += 1

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
	# 이동하고자 하는 위치 확인
	next_row = row + step[0]
	next_column = column + step[1]
	# 해당 위치로 이동이 가능하다면 카운트 증가
	if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
		result += 1
		
print(result)
