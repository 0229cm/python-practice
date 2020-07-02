# 반복문
# 특정 문장/코드를 지정한 횟수/조건에 의해
# 반복 실행하는 문장

# 어떤 문장을 한 번 출력한다면?
print('Hello, World!!')

# 어떤 문장을 여러번 출력한다면?
print('Hello, World!!')
print('Hello, World!!')
print('Hello, World!!')

# 여러번 출력한 문장의 일부를 수정해야 한다면?
print('Hello, Python!!')
print('Hello, Python!!')
print('Hello, Python!!')

# 만약, 반복문을 사용한다면?
# 반복의 용이성과 수정의 편의성이 제공
# for 변수 in range(시작값, 종료값, [증가/감소]):
# 반복할 문장들
# 단, range(x, y)의 실행횟수는 y - x 임
# ex) range (1, 10) 의 실행횟수는 9회

for i in range(1, 3+1):
    print(i, 'Hello, World!!')

# 1 ~ 10 까지 모든 정수들을 출력하는 반복문을 작성하세요
for i in range(1, 11):
    print(i, end=' ')

# 1 ~ 50 까지 모든 정수 중 짝수만 출력하는 반복문을 작성하세요
for i in range(1, 51):
   if i % 2 == 0:
    print(i, end=' ')

# 1~ 100까지 모든 정수들의 합을 출력하는 반복문을 작성하세요
sum = 0
for i in range(1, 101):
    sum = sum + i

print(f'1~100의 총합: {sum}')

# 1 ~ N 까지의 합을 구하는 공식
# => (N x (N+1)) / 2
sum = (100 * (100+1)) / 2
print(f'1~100의 총합2: {sum}')

# 반복수행시 변수가 따로 필요없는 경우
# 변수명 대신 _ 를 사용하기도함
for _ in range(1, 3+1):
    print('Hello, World!!')

# 구구단 중 특정 단을 입력받아 출력하는
# 반복문을 작성하세요
dan = int(input('단을 입력하세요'))
for i in range(1, 9+1):
    # print('%d x %d = %d' % (dan, i, dan*i))
    print(f'{dan} x {i} = {dan*i}')

# 중첩 반복문
# 두개 이상의 반복문을 이용해서 반복 실행을 할 수도 있음
# 보통 2개의 반복문을 중첩해서 사용하는 경우가 많은데,
# 이 경우, 바깥쪽 반복문은 행을,
# 안쪽 반복문은 열을 반복하는데 사용함
# 따라서, 총 반복횟수는 바깥쪽 반복문 횟수 x
# 안쪽 반복문 횟수임

# 2단부터 9단까지의 구구단을 출력하는
# 반복문을 작성하세요

# 세로로 길게 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')

# 가로로 넓게 출력
for j in range(1, 10):
    for i in range(2, 10):
        print(f'{i} x {j} = {i * j:2d}', end=' ')
    print('')

# range 함수
# range(start, end, step)
# 지정한 범위 내 숫자를 만들어냄
print( list(range(1,10)) )

# start 를 지정하지 않으면 0 부터 시작함
print( list(range(10)) )

# step 을 지정하면 step 만큼 간격을 띄워 숫자를 출력
print( list(range(1, 21,2))) # 홀수 출력
print( list(range(2, 21,2))) # 짝수 출력



