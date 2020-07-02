# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드의 집합체
# 보통 반복적으로 사용하는 코드들을 하나로 묶고
# 그것에 이름을 붙인 것을 함수라 함

# 즉, 반복적으로 사용할 가치가 있는 코드들을 한 뭉치로 묶고
# (어떤 값을 입력하면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움
# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈

# 커피 서빙 - 함수를 사용하지 않은 경우
coffee = 0

coffee = int(input('어떤 커피를 드시겠어요?'
                   '1:보통, 2:설탕, 3:블랙'))

print('\n1. 뜨거운 물을 준비한다.')
print('\n2. 예쁜 커피잔을 준비한다.')

msg = ''
if coffee == 1:
    msg = '\n3. 보통 커피를 탄다.'
elif coffee == 2:
    msg = '\n3. 설탕 커피를 탄다.'
elif coffee == 3:
    msg = '\n3. 블랙 커피를 탄다.'
print(msg)

print('\n4. 물을 붓는다.')
print('\n5. 스푼으로 젖는다.')
print('\n6. 손님에게 커피를 드린다.')

# 커피 서빙 코드를 3번 반복한다면?
# 코드가 길어서 실행하기 다소 불편함
# 또한, 프로그램 작동원리를 파악하기가 어려움
# 코드에 수정사항이 생기면 수정하기에도 번거로움
# => 함수로 만들면 코드를 효율적으로 관리할 수 있음

# 함수 생성방법
# def 함수명(매개변수):
#     함수몸체
#     return 반환값

def coffeeMakerV1():
    coffee = 0

    coffee = int(input('어떤 커피를 드시겠어요?'
                       '1:보통, 2:설탕, 3:블랙'))

    print('\n1. 뜨거운 물을 준비한다.')
    print('\n2. 예쁜 커피잔을 준비한다.')

    msg = ''
    if coffee == 1:
        msg = '\n3. 보통 커피를 탄다.'
    elif coffee == 2:
        msg = '\n3. 설탕 커피를 탄다.'
    elif coffee == 3:
        msg = '\n3. 블랙 커피를 탄다.'
    print(msg)

    print('\n4. 물을 붓는다.')
    print('\n5. 스푼으로 젖는다.')
    print('\n6. 손님에게 커피를 드린다.')

# 함수 호출 : 함수명()
coffeeMakerV1()



# 기존 코드는 커피 주문을 받는 부분과
# 실제 커피를 만드는 부분이 같이 존재
# solid 원칙에 따라 주문 받는 부분과 만드는 부분을 분리함
# 커피 만드는 부분 : coffeeMakerV2

def coffeeMakerV2():
    print('\n1. 뜨거운 물을 준비한다.')
    print('\n2. 예쁜 커피잔을 준비한다.')
    msg = ''
    if coffee == 1:
        msg = '\n3. 보통 커피를 탄다.'
    elif coffee == 2:
        msg = '\n3. 설탕 커피를 탄다.'
    elif coffee == 3:
        msg = '\n3. 블랙 커피를 탄다.'
    print(msg)

    print('\n4. 물을 붓는다.')
    print('\n5. 스푼으로 젖는다.')
    print('\n6. 손님에게 커피를 드린다.')

# 함수실행하기
coffee = 0

coffee = int(input('어떤 커피를 드시겠어요?'
                   '1:보통, 2:설탕, 3:블랙'))

coffeeMakerV2()


# 함수의 필요성
print('Hello, World!!') # 단순출력

print('Hello, World!!') # 반복출력
print('Hello, World!!')
print('Hello, World!!')

for _ in range(3):          # 개선된 반복 출력
        print('Hello,World!')

# 만약 'World' 대신 'Python'을 사용해야 한다면?
# 이러한 반복문을 여러번 사용해야 한다면?
# 여러번 사용했을 경우 혹시 수정해야 한다면?
# 이렇게 작성한 코드를 다른 사람과 공유하고 싶다면?
# => 함수를 이요하면 됨

# 함수 정의
def saymsg():
    for _ in range(3):  # 개선된 반복 출력
        print('Hello,World!')

# 함수 호출
saymsg()

# 만약, 'World'대신 'Python'을 사용해야 한다면?
# 바꾸고 싶은 문자열을 함수의 매개변수로 입력받아 처리
def saymsg2(msg):       # 매개변수(입력값)이 있는 함수 정의
    for _ in range(3):  # 개선된 반복 출력
        print(f'Hello,{msg}!!')

saymsg2('Python')

# 두 정수를 입력받아서
# 그것을 더한 후 결과를 출력하는 함수 정의 : add
def add(num1, num2):
    print(f'{num1} + {num2} = {num1+num2}')

add(2,4)

# 한편, solid 원칙에 따라
# add 함수는 입력값을 받아 단지 더하기만 할뿐
# 자체적으로 출력하는 기능은 제외하는 것이 좋음

# 반환값이 있는 함수 정의 : return

# def 함수명(매개변수):
#     함수몸체
#     return결과값

# 두 정수를 입력받아서
# 그것을 곱한 후 결과를 반환하는 함수 정의 : mul

def mul(num3,num4):
    return num3*num4
print(mul(3,4))

# 결혼여부와 연봉을 입력받아 세금을 계산하는
# ComputeTax 함수를 작성하세요
# 미혼 0 : 3000이하면 0.15, 3000 초과면 0.3 적용
# 기혼 1 : 6000이하면 0.1, 6000초과면 0.25 적용
def computeTax(isMarr,sal):
    tax = 0
    if isMarr == 0:
        if sal <= 3000: tax = sal*0.15
        else: tax = sal*0.3
    elif isMarr == 1:
        if sal <= 6000: tax = sal * 0.1
        else: tax = sal * 0.25
    return tax

# 메인부분
isMarr = int(input('결혼여부는? 0:미혼, 1:기혼'))
sal = int(input('연봉은?'))
print(f'{isMarr}이고,' 
      f'연봉이 {sal}일때, ' 
      f'세금은 {computeTax(isMarr,sal)}입니다')

# 함수의 결과값은 하나이다!
# 자바에서는 하나의 return문에 하나의 값만을 넘길 수 있음
# 반면에, 파이썬에서는 여러개의 값을 넘길 수 있음
# 단, return할 여러개의 값을 튜플로 변환되어 넘어감
# 하지만, 여러개의 return문으로 결과값을 넘길순 없음

# 두 정수를 입력받아
# 사칙연산 후 결과를 반환하는 compute4Int함수 정의

def compute4Int(a,b) :
    sum = a + b
    min = a - b
    mul = a * b
    div = a / b

    return sum, min, mul, div

# 함수 호출
compute4Int(2,3)

# return문의 또 다른 용도
# 함수 내 특정코드의 실행 중지를 위해 사용할 수 있음

# 숫자 2개를 입력받아 첫번째 숫자 a를 이용해서
# 1~a 까지 정수를 출력하는 함수를 작성하세요
# 단, b 숫자에 도달하면 함수실행을 중단하도록 한다
# ex) functionStop(10,7) =>
# 1 2 3 4 5 6 7 (10까지 출력해야 하지만 7까지만 출력)

def functionStopV1(a,b):
    for i in range(1, a+1):
        print(i, end=' ')
        if i == b:
            return  # 함수실행을 중단
    print('이글이 보이나요?')

functionStopV1(10,7)

# 입력한 정수에 대해 짝수/홀수 여부를
# 판별해주는 함수 checkEvenOdd를 작성하세요
def checkEvenOdd(num):
    result = '홀수입니다'
    if num % 2 == 0: result = '짝수입니다'

    return result
checkEvenOdd(3)

# 주민번호를 입력받아 유효성을 검사하는 checkjumin 함수를 작성하세요
# 1. 주민번호 13자리 중 12자리의 각자리를 2,3,4,5,6,7,8,9, 2,3,4,5 가중치로 곱함
# 2. 곱한 결과를 각각 모두 더함
# 3. 더한 값을 11로 나눠 나머지를 구함
# 4. 11에서 나머지를 뺀 결과와 주민번호 맨 마지막 자리와의 일치여부 검사
# 5. 11에서 나머지를 뺀 결과가 2자리라면 맨 끝자리와 비교함
# ex) 111111-1111118

jumin = '111111-1111118'    # 6자리 + 7자리
sum = 0

# 2,3,4,5,6,7,8,9,2,3,4,5 가중치로 곱함
sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[7]) * 8
sum += int(jumin[8]) * 9
sum += int(jumin[9]) * 2
sum += int(jumin[10]) * 3
sum += int(jumin[11]) * 4
sum += int(jumin[12]) * 5

# 11 로 나눠 나머지를 구함
mod = sum % 11

# 11을 나머지로 뺀 결과 계산
checker = 11 - mod

# 주민번호 맨 마지막 자리와의 일치여부 검사
if checker == int(jumin[13]):
    print('주민번호 일치!')
else:
    print('주민번호 불일치!')



def checkjumin(jumin):
    sum=0
    sum = 0

    # 2,3,4,5,6,7,8,9,2,3,4,5 가중치로 곱함
    sum += int(jumin[0]) * 2
    sum += int(jumin[1]) * 3
    sum += int(jumin[2]) * 4
    sum += int(jumin[3]) * 5
    sum += int(jumin[4]) * 6
    sum += int(jumin[5]) * 7
    sum += int(jumin[7]) * 8
    sum += int(jumin[8]) * 9
    sum += int(jumin[9]) * 2
    sum += int(jumin[10]) * 3
    sum += int(jumin[11]) * 4
    sum += int(jumin[12]) * 5

    # 11 로 나눠 나머지를 구함
    mod = sum % 11

    # 11을 나머지로 뺀 결과 계산
    checker = 11 - mod

    # 주민번호 맨 마지막 자리와의 일치여부 검사
    if checker == int(jumin[13]):
        print('주민번호 일치!')
    else:
        print('주민번호 불일치!')

checkjumin('111111-1111118')

# 주민번호 검사 개선 버전
jumin = '123456-1234567'

def checkjumin2():
    sum = 0
    weight = [2,3,4,5,6,7, 8,9,2,3,4,5]
    pos = [0,1,2,3,4,5, 7,8,9,10,11,12]

    for i in range(len(pos)):
        sum += int(jumin[pos[i]]) * weight[i]
    checker = (11 - sum % 11) % 10

    if (checker == int(jumin[13])):
        print('주민번호 일치!')
    else:
        print('주민번호 불일치!')

checkjumin2()

