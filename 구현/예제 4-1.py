"""
"문제 해결 아이디어"
-> x, y값이 1 or N일 때(지도에서 가장 끝 부분)는 한정적으로 움직일 수 밖에 없다.
예를 들어, x값이 1인 가장 윗 둘레에서는 'U'를 받을 시엔 지도 밖으로 나가기에 입력 받은 것을 무시해야 한다.
이 점에 주목하여 알고리즘을 작성했다.
또한 반복적인 구문(U, D, L, R)은 함수로 만들어 가독성을 높였다.
"""
# 내 풀이
N = int(input())

Move = list(map(str, input().split()))
# (1, 1)에서 시작
x = 1
y = 1


# 'U'를 입력 받으면 x값을 1 감소
def Up(i):
	if Move[i] == 'U':
		global x
		x -= 1


# 'D'를 입력 받으면 x값을 1 증가
def Down(i):
	if Move[i] == 'D':
		global x
		x += 1


# 'L'을 입력 받으면 y값을 1 감소
def Left(i):
	if Move[i] == 'L':
		global y
		y -= 1


# 'R'을 입력 받으면 y값을 1 증가
def Right(i):
	if Move[i] == 'R':
		global y
		y += 1


## x, y 값이 N값을 벗어나는 경우 N을 넘어가지 않게끔 설정.
def Fin():
	global x, y, N
	if x == N + 1:
		x -= 1
	elif y == N + 1:
		y -= 1
	elif x == 0:
		x += 1
	elif y == 0:
		y += 1


for i in range(len(Move)):
	Up(i)
	Down(i)
	Left(i)
	Right(i)
	Fin()
print(x, y)
# 이 전에 사용한 알고리즘. 이보다 더 간결한 알고리즘을 찾음.
"""
## 가장 먼저 받는 문자가 'R', 'D', '그 외('U, L')'로 구분하여 구성
if Move[0] == 'R':
	y += 1
	# 두 번째 문자부터 끝 문자까지 확인하여 그 상황에 맞게 x or y 값을 수정하게끔 설정
	for i in range(1, len(Move)):
		if x != 1:
			Up(i)
			Down(i)
			Left(i)
			Right(i)
			Fin()
		
		# 두 번째 경우에 위로 가는걸 막기 위해 조건문을 이렇게 작성함. 만약 U를 입력 받으면 
		else:
			continue

elif Move[0] == 'D':
	x += 1
	for i in range(1, len(Move)):
		if Move[i] != 'L':
			Down(i)
			Right(i)
			Up(i)
			Fin()
			if x == N:
				Up(i)
				Right(i)
				Fin()
		else:
			continue

else:
	for i in range(1, len(Move)):
		if Move[i] == 'R':
			Right(i)
			Fin()
		elif Move[i] == 'D':
			Down(i)
			Fin()
		else:
			continue
"""

# 해설

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# ******* 전혀 생각 못한 풀이. 조건문 사용에 대한 활용능력을 기를 필요가 있다고 판단. ******** #
# 이동 계획을 하나씩 확인
for plan in plans:
	# 이동 후 좌표 구하기
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]
	# 공간을 벗어나는 경우 무시
	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	# 이동 수행
	x, y = nx, ny
print(x, y)
