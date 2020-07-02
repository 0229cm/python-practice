# 컴프리헨션comprehension - 반복문 축약
# 다양한 데이터 객체에 사용되는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능

# 파이썬에는 4가지 종류의 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약법
# 1~10까지의 정수를 리스트에 저장하는 경우1
nums1 = []
for i in range(1,10+1):
    nums1.append(i)

print(nums1)

# 1~10까지의 정수를 리스트에 저장하는 경우 2
# [표현식 for 항목 in 반복가능객체]
nums2 = [i for i in range(1, 10+1)]
print(nums2)

# 0~20 사이 짝수를 리스트로 생성하는 축약문을 작성하세요
evens = [i for i in range(2,10+1,2)]
print(evens)

evens2 = [i*2 for i in range(1,10+1)]
print(evens2)

# 1~10까지 제곱값을 리스트로 생성하는 축약문을 작성하세요
# squares = []
# for i in range(1,10+1):
#     squares.append(i**2)
# print(squares)

squares = [i*i for i in range(1,10+1)]
print(squares)

# 다음 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1,2,3,4,5]
val2 = [1,2,'A',False,9,100]

sq1 = [v **2 for v in val1]
print(sq1)
sq2 = [v **2 for v in val2]
# => TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# 당연히 문자나 bool형은 산술연산 불가!
print(sq2)

# 조건문을 이용한 산술 연산
# 변수의 유형을 알아보려면 type함수 사용
sq2 = []
for v in val2:
    if type(v) == int:
        sq2.append(v**2)
print(sq2)

# for if 축약문
# [표현식 for 항목 in 반복가능객체 if 조건]
sq3 = [v**2 for v in val2 if type(v) == int]
print(sq3)

# 1~60 사이의 홀수만 골라서 리스트로 생성하세요
odds = [i for i in range(1,60+1) if i % 2 != 0]
print(odds)
# 1~100 사이의 7의 배수만 골라서 리스트로 생성하세요
nums7 = [i for i in range(1,100+1) if i % 7 == 0]
print(nums7)

# 1~100 사이의 정수 중 끝자리가 7인 수만
# 골라서 리스트로 생성하세요
nums8 = [i for i in range(1,100+1) if i % 10 == 7]
print(nums8)

# for 다중 if 축약문
# [표현식1 if 조건1 else 표현식2
#          for 항목 in 반복가능객체]

# 1~100 사이의 정수 중 임의의 정수가 짝수면 even,
# 홀수면 odd 라고 구분해서 리스트에 저장하세요
evens = ['even'+str(i) for i in range(1,100+1) if i % 2 == 0]
odds = ['odd'+str(i) for i in range(1,100+1) if i % 2 != 0]
print(evens)
print(odds)

evenodd = ['even'+str(i)  if i % 2 == 0 else 'odd'+str(i)
           for i in range(1,100+1)]
print(evenodd)

# for 중첩 if 축약문
# [표현식 for 항목 in 반복가능객체
#         if 조건1 if 조건2 ]

# 1~50 사이의 정수 중 2의 배수이면서 5의 배수인 정수를
# 리스트에 저장하세요
num25 = [i for i in range(1,50+1)
         if i % 2 == 0 if i % 5 == 0]
print(num25)

# 구구단 중 7단, 8단 출력해서 리스트에 저장
gugu78 = []
for i in range(7,8+1):
    for j in range(1,9+1):
        gugu78.append(f'{i} x {j} = {i*j}')
print(gugu78)

# 중첩 for 문을 사용하는 축약문
# [표현식 for 항목1 in 반복가능객체1
#        for 항목2 in 반복가능객체2]

gugu78 = [f'{i} x {j} = {i*j}'
          for i in range(7,8+1)
           for j in range(1, 9+1)]

print(gugu78)

# name, grd 리스트의 값들을 각각 키와 값으로
# 딕셔너리에 저장하세요
name = ['혜교', '지현', '수지']
grd = ['우','미','수']

# 단순하게 생성
sj = {}
sj[name[0]] = grd[0]        # '혜교' : '우'
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

print(sj)

# 반복문을 사용해서 생성
sj2 = {}
for i in range(3):
    sj2[name[i]]=grd[i]

print(sj2)

# 딕셔너리 for 축약문
# {키값표현식 for key, val in zip(반복객체1, 반복객체2)}
# zip : 동일한 갯수의 시퀀스 자료형을 하나로
# 묶어주는 역할을 수행
# ex) zip([1,2,3],['a','b','c'])
# =>[(1,'a'),(2,'b'),(3,'c')]
sj3 = {key:val for key, val in zip(name, grd)}
print(sj3)

# 1~10사이의 정수 중 각 정수를 키로 하고
# 정수의 제곱을 값으로 하는 딕서너리를 작성하세요
intkey = [1,2,3,4,5]
intval = [1,4,9,16,25]

nums1 = { k:v for k, v in zip(intkey, intval) }
print(nums1)

nums2 = {}
for i in range(1,5+1):
    nums2[str(i)] = i**2

print(nums2)

# 리스트가 없는 경우2 : 축약형
nums3 = { str(i):i**2 for i in range(1,5+1)}
print(nums3)

# 학생과 성적 평균점수에 대한 리스트가 있을때
# '학생'은 키로, 값은 '합격여부'로 하는 딕셔너리를 생성하세요
# 단, 평균점수가 85점이상인 경우 '합격',
# 그 외는 '불합격'이라고 출력함

std = ['철수', '영희', '길동', '꺽정']
avg = [80,85,91,74]

sj = { k:'합격' if v >= 85 else '불합격'
            for k, v in zip(std, avg)}
print(sj)





