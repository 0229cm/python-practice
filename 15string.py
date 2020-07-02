# 문자열 다루기
# 문자, 단어로 구성된 문자들의 집합을 의미
# 보통 문자들은 '', ""(한줄) 나 """"""(여러줄) 등으로 만듦
# 문자는 문자열의 부분집합이고
# 따라서, 문자열은 리스트단위의 문자로 분리/접근 가능

# 문자열 연산 : +(연결), *(반복)

a = 'Hello '
b = 'World '
c = ' !'

print(a + b + c)
print(a + b + (c * 3))

# 문자열 길이 : len
d = a + b + (c * 3)
print(len(d))

# 문자열 인덱싱 : 문자단위로 리스트처럼 접근 가능
# 인덱스 -면 문자열 끝에서부터 찾음
print(d[0], d[1], d[len(d)-1], d[-1])

# 변수 d에서 Hello 를 출력하는 문자열 인덱싱을 작성
# 문자열 슬라이싱
# 인덱싱보다 좀 더 효율적으로 문자에 접근하는 방법
# 변수명[시작:끝-1:간격]
print(d[0:5], d[: 5])

# 변수 d에서 World 를 출력하는 문자열 슬라이싱
print(d[6:11], d[:11])

# Hello, World!!! 라는 문자열을 역순으로 출력
# 간격을 -1 로 설정하면 역순으로 출력할 수 있음
print(d[::-1])

# Hello 라는 문자열을 역순으로 출력
print(d[4::-1])

# World 라는 문자열을 역순으로 출력
print(d[10:4:-1])

# 문자열 포맷팅 : %d, %f, %s
# f문자열 : python3.6 부터 지원시작
name = '혜교'
kor = 95.4
sal = 35500

print(f'{name}의 국어점수는 {kor}이다')
print(f'{name}의 급여는 10000이나 올랐다' \
      f'따라서, 인상된 급여는 {sal+10000}이다')

# 문자는 자동으로 왼쪽정렬, 숫자는 자동으로 오른쪽정렬
print(f'{name:10}의 국어점수는 {kor:10}이다')

print(f'{name:>10}의 국어점수는 {kor:<10}이다')
# 정렬방식을 바꾸려면 >,< 를 사용함

print(f'{name:^10}의 국어점수는 {kor:^10}이다')
# 가운데 정렬시 ^를 사용

print(f'{name:=>10}의 국어점수는 {kor:@>10}이다')
# 공간이 남을 경우 채움 문자 역시 지정 가능

sj = {'name':'지현', 'eng':85.49 }
print(f'{sj["name"]}의 영어점수는 {sj["eng"]:.1f}이다')

# 문자열 함수 : 대소문자 변환
str = 'hello, world!!'

print(str.upper())
print(str.upper().lower())
print(str.swapcase())       # 자동변환
print(str.capitalize())     # 문장의 첫글자만 대문자
print(str.title())          # 단어의 첫글자만 대문자

# 문자열 검색 : count, find, startwith, endswith
str = 'abcdE ABCDe abcde ABCDE'

str.count('a')      # 특정문자의 출현빈도
str.count('cd')

str.find('a')       # 특정문자의 존재 위치
str.find('ABCD')
str.find('X')       # 문자가 존재하지 않으면 -1로 출력
str.rfind('ABCD')   # 뒤에서 찾은 문자 위치
str.rfind('a')

str.startswith('abc')
str.startswith('xyz')
str.endswith()('CDE')   # 특정문자 종료여부
str.endswith()('xyz')

# 파이썬은 재미있습니다. 물론 공부가 다 재미있지는 않습니다 라는 문장에서
# 1) '재미' 라는 단어는 몇번 나왔는가?
# 2) '재미' 라는 단어 처음 나온 위치는?
# 3) '재미' 라는 단어 마지막으로 나온 위치는?
str = '파이썬은 재미있습니다. 물론 공부가 다 재미있지는 않습니다'

print(str.count('재미'))
print(str.find('재미'))
print(str.rfind('재미'))

# 문자열 공백 : strip
str = '    abc    '

print('|' + str + '|')
print('|' + str.lstrip() + '|')     # 왼쪽 공백 제거
print('|' + str.rstrip() + '|')     # 오른쪽 공백 제거
print('|' + str.strip() + '|')      # 양쪽 공백 제거

str = '====<====^>?^?>^?'

print(str.strip('='))   # 양 끝 = 문자제거
print(str.strip('?'))   # 양 끝 ? 문자제거
print(str.strip('^'))   # ^ 문자제거
print(str.strip('^?'))  #

# 특정 문자열 제거 : replace
# replace('바꿀문자', '새 문자')

print(str.replace('=', ''))     # = 문자 제거

# 'abc123xyz987' 문자열에서
# abc를 찾아서 대문자로 바꾸고,
# 987을 357로 바꾸세요
str = 'abc123xyz987'
print(str.find('abc'))
print(str.replace('abc', 'ABC'))
print(str.replace('987', '357'))

# 'Hello\t\n World\r\n' 문자열에서
# 탭, 줄바꿈 문자를 찾아서 제거하세요
str = 'Hello\t\n World\r\n'
print(str.replace('\t', ''))
print(str.replace('\n', ''))
print(str.replace('\r', ''))

# 문자열 분리 : split(구분자)
# 구분자로 문자열을 문자로 분리한 결과는 리스트임
str = '123,abc,987,xyz'

print(str.split(','))   # 콤마로 문자열을 분리
for s in str.split(','):
    print(s)

str = '123 abc 987 xyz'

print(str.split(' '))
for s in str.split(' '):
    print(s)

str = '123 abc 987 xyz'
# print(str.split(' '))
for s in str.split(' '):
    print(s)

print(str.split(' ', 1)) # 나눌 갯수 지정
print(str.split(' ', 2))
print(str.split(' ', 3))

docs = '''abc
123
xyz
987'''

print(docs)
print(docs.splitlines())    # 줄단위로 문자열을 나눔

# 문자열 집합 : A.join(B)
# B 의 각 문자열을 A 문자에 결합함
# 리스트를 join 하면 결과는 문자열로 변환함
times = ['15', '04', '41']
str = ":"   # 15:04:41

print(str.join(times))

# 현재년도를 join 과 리스트를 이용해서 출력하세요
date = ['2020', '06', '29']
str = "-"

print(str.join(date))

# 문자열 유형 판별
print('123'.isdigit())  # 숫자 여부
print('123'.isalpha())  # 문자 여부
print('123'.isalnum())  # 숫자, 문자 여부
print('   '.isspace())  # 공백 여부
print('Hello'.istitle())    # 첫글자 대문자 여부

# a:b:c:d 를 a#b#c#d 로 바꿔 출력하세요
str = 'a:b:c:d'

txt = str.split(':')
print('#'.join(txt))

test = ['a', 'b', 'c', 'd']
str = "#"
print(str.join(test))

# 입력받은 리스트에 대한 총합을 구하는 코드를 작성하세요
# 단, 입력값은 65,45,2,3,45,8 로 함
nums = input('임의의 숫자 6개를 ,로 구분해서 입력하세요')

sum = 0
for num in nums.split(','):
    sum+= int(num)

print(sum)

# 빈자리를 0으로 채우기 : zfill
# 대상zfill(전체자릿수)
print('35'.zfill(5))    # 총 5자리 중 0은 3 개
print(''.zfill(5))    # 총 5자리 중 0은 5 개





