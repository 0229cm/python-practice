# while
# 특정조건을 만족하면 반복을 실행
# 변수 = 초기값
# while 조건식:
#       반복할문장
#       변수증가/감소

# Hello, World!! 문장을 3번 반복 출력해봄
cnt = 1     # 반복 횟수를 기억하는 변수 정의
while (cnt < 4):
    print('Hello, World!!')
    cnt += 1

# 1 ~ 10 까지 모든 정수들을 출력하는 반복문을 작성하세요
num = 1
while num <= 10:
    print(num, end='')
    num += 1

# 1 ~ 50 까지 모든 정수 중 홀수만 출력하는 반복문을 작성하세요
num = 1
while num <= 50:
    if (num % 2 != 0):
        print(num, end=' ')
    num += 1

# 1~ 100까지 모든 정수들의 곱을 출력하는 반복문을 작성하세요
num = 1
sum = 1

while num <= 100:
    sum = num * sum
    num += 1

print(sum)

# 무한 반복
# while 문의 조건식을 True 라고 작성하면
# 끝나지 않는 반복을 실행하는 반복문이 됨
while True:
    print('Hello, World!!')

# 반복문 임의 중단 : break
# 계속 반복하는 코드를 임의의 시점에서
# 중단하고자 할 때 사용

# 사용자가 입력한 문자열을 그대로 출력하는
# 앵무새 프로그램을 작성
# 단, '끝' 이라고 입력하면 프로그램 실행을 중단한다
say = input('아무거나 입력해보세요')
print(say)

while True:
    say = input('아무거나 입력해보세요')
    if say == '끝': break
    print(say)

# 1~ 무한대 범위의 정수 합을 구하세요
# 단, 이것의 총합이 20200623 보다 크면
# 계산을 자동준단하세요
sum = 0
i = 1

while True:
    if sum > 20200623: break
    sum = sum + i
    i = i + 1

# print(i, sum)
print(f'{i}, {sum:,}')

# 반복실행시 일부코드를 건너뛰기 : continue
# 반복실행 중 특정 조건을 만족하는 경우
# 일부코드는 실행하지 않고 조건식으로 제어를 넘김

# 1 ~ 100 까지의 모든 정수의 합을 구하되
# 3 의 배수, 7 의 배수는 제외하는 반복문으로 작성하세요
i = 0
sum = 0

while (i < 100):
    i += 1
    if i % 3 == 0 or i % 7 == 0: continue
    sum += i
    # print(i, sum) 확인용 코드

print(sum)

# 숫자 n을 하나 입력받아 1 ~ n 사이의 홀수만 출력
n = int(input('숫자입력'))
i = 0
while (i < n):
    i += 1
    if (i % 2 == 0): continue
    print(i)

# 1 ~ 100 사이 정수 중 3으로 끝나는 숫자만 출력하세요

# n = 7 => 7 % 10 == 3 ?
# n = 24 => 24 % 10 == 3 ?
i = 0
while i < 100:
    i += 1
    if i % 10 != 3: continue
    print(i)

# 두 수를 입력받아 이 범위 내의 숫자들 중
# 7로 끝나지 않는 숫자를 출력하세요
x = int(input('첫번째 숫자입력하세요'))
y = int(input('두번째 숫자입력하세요'))

i = x - 1
while i < y:
    i += 1
    if i % 10 == 7: continue
    print(i)

# 파이썬에는 switch 문이 지원되지 않음




