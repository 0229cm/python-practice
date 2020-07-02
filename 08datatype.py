# 딕셔너리
# 이름key과 값value으로 구성된 연관배열의 일종
# 자료구조 만들때 {}를 사용하고
# 이름과 값은 : 으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 데이터분석시 주로 사용하는 자료 구조 : mongodb
# 키를 통해 자료를 찾는 해쉬테이블을 이용하므로
# 검색속도가 빠름

person = { 'name' : '혜교',
           'userid' : 'abc123',
           'passwd' : '987xyz',
           'email' : 'abc123@987xyz.com',
           'sungjuk' : [99,98,95.5] }
print(person)

# 딕셔너리 다루기
# 새로운 항목 추가 : 변수명 [새로운 키] = 새로운값
person['zipcode'] = '12345'
person['addr'] = '서울시 종로구'
print(person)

# 기존값 변경 : 변수명[기존키] = 변경값
person['zipcode'] = '98765'
print(person)

# 딕셔너리 값 조회 : 변수명[키], 변수명.get(키)
print(person['name'])
print(person.get('userid'))
print(person['sungjuk'])        # 리스트로 출력
print(person['sungjuk'][1])     # 영어만 출력

sj = person['sungjuk']
print(sj[1])

# 기존 값 삭제 : del(변수명[기존키])
del(person['addr'])
print(person)

# 만일, 존재하지 않는 키를 참조한다면?
print(person['gender'])
# =>KeyError: 'gender'

print(person.get['gender'])
# none

# 딕셔너리의 모든 키 출력 : keys 함수
print(person.keys())    # dict_keys 형식
print(list(person.keys()))

for key in list(person.keys()):
    print(key, end=' ')

# 딕셔너리의 모든 값 출력 : values 함수
print(person.values())
print(list(person.values()))

for value in list(person.values()):
    print(value, end=' ')

# 딕서너리의 키, 값을 묶어서 pair 출력 : items 출력
print(person.items()) # 튜플형태
print(list(person.items()))

for item in list(person.items()):
    print(item)

# # 딕셔너리 변환하기
# 리스트 속에 리스트나 튜플의 값을,
# 튜플 속에 리스트나 튜플의 값을
# key와 value로 나란히 입력하면,
# dict 함수로 딕서너리로 변환할 수 있음
sj1 = [['혜교', '수'], ['지현','미'],['수지','우']]
sj1 = dict(sj1)
print(sj1)

sj2 = [('혜교', '수'), ('지현','미'),('수지','우')]
sj2 = dict(sj2)
print(sj2)

sj3 = (('혜교', '수'), ('지현','미'),('수지','우'))
sj3 = dict(sj3)
print(sj3)

sj4 = (['혜교', '수'], ['지현','미'],['수지','우'])
sj4 = dict(sj4)
print(sj4)

# employees 데이터를 딕셔너리 emp로 생성
# EMPLOYEES.csv 파일을 이용함
empkey = ['empid', 'fname', 'lname', 'email', 'phone',
          'hdate', 'jobid','sal','comm','mgrid','deptid']
emplist = []

with open('c:/java/datasets/EMPLOYEES.csv') as lines:
    # EMPLOYEES.csv을 읽어서 lines에 저장
    for line in lines :
        # lines에 저장된 데이터를 한 행씩 읽은 후
        cols = line.split(',')
        # ,을 기준으로 각 열을 분리해서 col 리스트에 저장
        emp = {}
        for i in range(len(empkey)):
            emp[empkey[i]] = cols[i]
            # 각 키와 관련있는 값을 dict형식으로 저장

        emplist.append(emp)
print(emplist)

# departments 데이터를 딕셔너리 dept로 생성
# DEPARTMENTS.csv 파일을 이용함
deptkey = ['deptid', 'dname', 'mgrid','locid']
deptlist= []

with open('c:/java/datasets/DEPARTMENTS.csv') as lines:
    for line in lines :
        cols = line.split(',')
        dept = {}
        for i in range(len(deptkey)):
            dept[deptkey[i]] = cols[i]
        deptlist.append(dept)
print(deptlist)
