# 파이썬 고급 자료형
# 파이썬은 기본적으로 숫자/문자/논리 자료형을 제공
# 하지만, 이것만으로는 프로그래밍 하기에 부족함
# 이런 불편함을 해소하기 위해 '리스트, 튜플, 딕셔너리, 셋'
# 자료형을 제공함

# 리스트 자료형
# 순차적으로 데이터를 관리하는 자료형 (순서가 존재)
# => 시퀀스 자료형 : 리스트 튜플
# 중복으로 데이터를 저장할 수 있음

# 다른 언어 (C++, Java) 의 배열과는 달리
# 서로 다른 자료형의 요소를 함께 저장할 수 있음
# 리스트의 각 요소는 [] 를 사용해서 접근함

# 문자열은 기본적으로 리스트임
# 문자는 문자열의 부분집합
# 문자는 문자열의 부분집합 => 리스트로 접근가능
msg = 'Hello, World!!'
print(msg, msg[0], msg[len(msg)-1])

# 리스트 생성방법은 []를 사용함
list1 = []              # 빈 리스트
list2 = [1,2,3,4,5]     # 정수 리스트
list3 = ['a','b','c','d','e']   # 문자 리스트
list4 = [1,'a',2,'b',3,'c']     # 혼합 리스트

print(list1, list2, list3, list4)

# 리스트를 이용한 간단한 연산
# 요소 존재 여부 파악 : in/not in 연산자
print( 3 in list2 )
print( 'c' in list3 )
print( 'z' not in list4)

# 길이 연산 : len
print(len(list2))
print(len(list4))

# 요소의 특정값 참조 : [위치값]
# 파이썬의 위치값 index 는 0부터 시작
print(msg[-1])
print(list4[4])

# 주민번호가 '123456-1234567'일때
# 성별이 무엇인지 확인하는 코드를 작성하세요
jumin = '123456-1234567'
if jumin[7] == '1':
    print('남')
else:
    print('여')

# 주민번호에서 생년월일만 출력하세요
birth = jumin[:6]
print(birth)

# 특정범위 내 요소들을 추출할때는 slice 사용
# 리스트명[start:end-1step]
print(jumin[0:6])
print(jumin[:6])    # start 를 생략하면 0부터 시작

# 주민번호에서 생년월일 이후 '-'를 제외한 문자열을 출력하세요
print(jumin[7:14])
print(jumin[7:])    # end 를 생략하면 맨 마지막 문자열까지 자동 추출

# 주민번호에서 짝수/홀수 위치의 문자들을 출력하세요
# print(jumin[0:14:2])
# print(jumin[1:14:2])
print(jumin[0::2])
print(jumin[1::2])

# 주민번호를 역순으로 출력하세요 : step 을 -1 로 설정
print(jumin[0:14])      # 0:14:1
print(jumin[14:0:-1])
print(jumin[14::-1])
print(jumin[::-1])

# 리스트에서 인덱스를 초과해서 참조하는 경우 ?
print(jumin[20])   # string index out of range
print(jumin[:20])  # 인덱스 초과시 오류 x

# 리스트를 이용해서 통계함수 사용
val = [1,2,3,4,5,6,7,8,9]

print( sum(val), sum(val)/len(val), max(val), min(val))

# 리스트 조작함수
# 기존 리스트에 새로운 항목 추가 : append
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)

# 기존 리스트의 특정 위치에 항목 추가
# insert(위치, 값)
list1.insert(0,100)
print(list1)

# 기존 리스트의 특정 위치에 항목 수정
# 리스트[위치] = 수정값
list1[3] = 200   # 맨 뒤 값을 200 으로 수정
print(list1)

# 리스트의 요소 제거
# pop() : 맨 뒤 요소부터 제거
# pop(위치) : 특정 위치의 요소 제거
list1.pop()
print(list1)

list1.pop(0)
print(list1)

# 리스트의 요소 제거 : remove(값)
list1 = [200, 1, 2, 100]
# list1.remove(0)  list.remove(x): x not in list]
list1.remove(1)
print(list1)

# 리스트의 모든 요소 제거 : clear
list1.clear()
print(list1)

# 리스트의 요소를 정렬하기 : sort
list1 = [6, 3, 2, 7, 1, 0]
list1.sort()        # 오름차순
print(list1)
list1.sort(reverse=True)    # 내림차순
print(list1)

# 학생 10 명의 성적이
# 70, 65, 55, 75, 95, 90, 80, 85, 100 일 때
# 총점, 평균, 최소, 최대 점수를 구하고
# 내림차순으로 정렬해서 출력하세요
sungjuk = [70, 65, 55, 75, 95, 90, 80, 85, 100]
print( sum(sungjuk), sum(sungjuk)/len(sungjuk), max(sungjuk), min(sungjuk))
sungjuk.sort(reverse=True)
print(sungjuk)

# 튜플 자료형
# 순차적 데이터를 관리하는 자료형(순서가 존재)
# 리스트와 동일하지만, 변경 불가능한 특성을 지님
# => 생성은 가능/추가,수정/삭제는 불가능
# 튜플 객체 생성은()를 사용
msg = ('H','E','L','L','O',',',' ',
       'W','O','R','L','D','!','!')
print(msg)
print(msg[0], msg[len(msg)-1])

tuple1 = ()
tuple2 = (1,2,3,4,5)
tuple3 = ('a','b','c','d','e')
tuple4 = (1,'a',2,'b',3,'c',4,'d',5,'e')
print(tuple2, tuple4)

print(3 in tuple4)
print(3 not in tuple4)

# 튜플 추가/수정/삭제
# tuple.append(10)      'tuple' object has no attribute 'append'
# tuple4[2] = 100       'tuple' object does not support item assignment
# tuple3.pop()          'tuple' object does not support item assignment
# tuple3.remove('a')    'tuple' object has no attribute 'remove'

# 만약, 튜플의 요소를 변경해야 한다면?
# 튜플을 리스트로 변환한 후 요소를 변경하고
# 다시 리스트로 튜플로 변경하면됨
# 튜플을 리스트 변환 : list(대상)
# 리스트를 튜플로 변환 : tuple(대상)

tuple1 = list(tuple)
tuple1.append(100)
tuple1.append(200)
tuple1.append(300)
tuple1 = tuple(tuple1)
print(tuple1)

# 난수 생성하기
# random 이라는 모듈이 필요
# random()       : 0 ~ 1 사이 임의의 부동소수점 숫자 출력
# randint(x,y)   : x ~ y 사이 임의의 정수 출력
# randrange(s,e,l)   : 시작부터 끝 사이 임의의 정수 출력
import random as r

print(r.random(), r.random(), r.random())
print(r.randint(1,10), r.randint(10,100))
print(r.randrange(1,10), r.randrange(10,100))
print(r.randrange(1,100,2), r.randrange(0,100,2))

# 1 ~ 45 사이 임의의 정수 6개를 추출해서 리스트와 튜플에 저장하는 코드를 작성
print(r.randint(1,45),r.randint(1,45),r.randint(1,45),r.randint(1,45),r.randint(1,45),r.randint(1,45))







