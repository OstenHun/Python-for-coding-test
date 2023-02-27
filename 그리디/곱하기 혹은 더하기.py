"""
"문제 풀이 아이디어"
-> 숫자로 구성된 문자열 사이에 '+' or 'x'를 대입하여 만들 수 있는 가장 큰 수를 만들기 위해서는 'x'를 많이 사용해야 한다. 하지만 문자열에 '0'이 포함될 경우 곱하면 '0'이 되기에 이때는 더하기 연산을 해 '0'을 없애준다.
"""

#								***잘못된 접근 및 코드***
#-> 곱하는 모든 경우가 더 크다고 간과함.
#-> 1이 포함된 경우 더하는 것이 곱하는 경우보다 크다 e.g.) 12 -> 1*2=2, 1+2=3

s = str(input())  #숫자 문자열 입력

result = 1  #초기 값을 1로 설정해 곱할 때 결과값 손실 방지, '0'이 더해져도 문제X 이후 곱하기 연산 함.

for i in range(len(s)):  #문자열 속 숫자 갯수만큼 연산 반복.
	if int(s[i]) == 0:  #숫자가 '0'일 경우 '1'에 더해서 '0' 처리.
		result += int(s[i])
	else:  #문자열 숫자가 '0'이 아닐 경우 모두 곱하기 연산
		result *= int(s[i])

print(result)
"""
"문제 풀이 아이디어"
-> 위와 동일하지만 '곱하기' 연산의 모든 경우가 크지 않음. '1'일 경우 곱하지 말고 '더하기' 연산 수행할 것.
"""

s = str(input())

result = int(s[0])

for i in range(1, len(s)):  #					***잘못된 접근 및 코드***
	if s[i] > 1:  # -> 여기서도 오류 존재. s[0]이 1또는 0일 경우 곱하면 최댓값 불가.
		result *= int(s[i])
	else:
		result += int(s[i])

print(result)

#해설1

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
	# 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
	num = int(data[i])
	if num <= 1 or result <= 1:
		result += num
	else:
		result *= num

print(result)
