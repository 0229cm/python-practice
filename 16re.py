# 정규표현식 regular expression
# 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
# 복잡한 문자열 속에서 특정규칙으로 된 문자열을 검색한 뒤
# 추출하거나 다른 문자열을 바꿀때 주로 사용
# 또한, 문자열이 정해진 규칙에 맞는지 판단할때도 사용

# 파이썬에서 정규표현식을 쓸려면 re 패키지를 import 해야함

import re

# 문자열 판단하기 : match
# 문자열 속에 특정문자열의 포함 여부 확인
# match('패턴', 문자열)

str = 'Hello, World'

print(re.match('Hello', str))  # Hello 라는 문자열 포함 여부
# span = (0, 5) 위치에 포함됨을 출력

re.match('Python', str)  # Python 라는 문자열 포함 여부

# 문자열이 맨 앞/뒤에 있는지 확인
# ^문자열 : 문자열이 맨 앞에 있는지 확인
# 문자열$ : 문자열이 맨 뒤에 있는지 확인

re.match('^Hello', str)
re.match('World$', str)
# 패턴을 맨 앞을 기준으로 찾기 때문에 결과가 제대로 나오지 않음
# => search 함수로 대체

re.search('^Hello', str)
re.search('World$', str)

# 지정한 문자열이 하나라도 존재하는지 확인 : [|]

re.search('Hello | World', str)

str = '123xyz987abc'
# 다음 문자열에 987 이나 357이 포함되어 있는지 확인

re.search('987|357', str)

# 숫자가 포함되어 있느지 확인 : [시작-끝]

re.search('0|1|2|3|4|5|6|7|8|9]', str)
re.search('[0-9]', str)

# 알파벳 소문자가 포함되어 있는지 확인
re.search('[a-z]',str)
# 알파벳 대문자가 포함되어 있는지 확인
re.search('[A-Z]',str)
# 알파벳과 숫자가 포함되어 있는지 확인
re.search('[0-9]|[a-z]|[A-Z]', str)

# 문자열이 하나이상 포함여부 확인 : *, + (수량한정자)
# * : 특정 문자열이 0개 이상 포함 여부
# + : 특정 문자열이 1개 이상 포함 여부
# *, + 는 greedy 하게 동작 : 가능한 많은 수의 패턴을
# 일치시킨 후 다음 패턴을 찾는다는 의미


str = '12345abcde'

re.search('[0-9][0-9][0-9]', str)
# 3개의 숫자로 구성된 문자열 존재 여부

re.search('[0-9]*', str)
# 0개 이상의 숫자로 구성된 문자열 존재 여부

str = 'bananas'

re.search('an', str)        # 'an' 존재 여부
re.search('an*', str)       # a 다음 n이 0 이상 존재 여부
re.search('an+', str)       # a 다음 n이 1 이상 존재 여부
re.search('[an]*', str)     # an 이 0개 이상 존재 여부
re.search('[an]+', str)     # an 이 1개 이상 존재 여부

re.search('a*b', 'b')       # a 가 0개 이상 존재 : O
re.search('a+b', 'b')       # a 가 1개 이상 존재 : X
re.search('a*b', 'aab')     # a 가 0개 이상 존재 : O
re.search('a+b', 'aab')     # a 가 1개 이상 존재 : O

# 문자열이 0,1 포함여부 확인 : ? (수량한정자)
re.search('[an]?', str)
re.search('an?', str)

re.search('abc?d', 'abd')       # c가 0, 1
re.search('abc?d', 'abxd')      # c가 0, 1
re.search('ab[0-9]?d', 'abxd')  # 0-9가 0,1
re.search('ab.d', 'abxd')       # 0-9가 0,1
re.search('ab.d', 'abxd')       # .은 아무문자 포함 여부

# 문자 패턴 반복 여부 : {n, m}
# 문자 {갯수}
# 숫자 {최소갯수, 최대갯수}

re.search('(hello){3}', 'hellohellohello')
re.search('(hello){4}', 'hellohellohello')

# 전화번호 패턴 파악 : 010-1234-9876
re.search('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1234-9876')

re.search('[0-9]{3}-[0-9]{3,4}-[0-9]{4}','010-123-987')

# 한글 포함 여부 : 가 ~ 힣
re.search('[가-힣]+', '홍길동')

# 특정 문자가 포함되어 있지 않은지 확인 : [^]
re.search('[A-Z]', 'Hello')
re.search('[^A-Z]+', 'Hello')
re.search('^[A-Z]+', 'Hello')   # 특정 문자 시작 여부

# 특수문자 존재 여부 : *?!()%$
re.search('\*+', '1 ** 2')
re.search('[$()]+', '$(document')

# 공백처리하기
re.search('[ ]+', 'abc      xyz')

# 단일 메타문자 : \d, \D, \w, \W, \s, \S
# \d : 모든 숫자 ([0-9])
# \D : 모든 숫자 제외 ([^0-9)]
# \w : 모든 영대소문자, 숫자, 밑줄(_)
# \W : 모든 영대소문자, 숫자, 밑줄문자(_) 제외
# \s : 모든 화면제어문자 (\t\r\n)
# \S : 모든 화면제어문자 제외

re.search('\d+', 'hello,1234 xyz987')
re.search('\w+', 'hello,1234 xyz987')
re.search('\s+', 'hello,1234 xyz987')

# 로그문자열이 GSE 로 시작하고 숫자로 끝나는지 확인
# ex) GSE1234567
import re
str = 'GSE1234567'
re.search('GSE[0-9]{7}', str)
re.search('GSE\d{7}', str)
re.search('GSE\d+', str)


# jumin 이라는 변수가 주민등록번호 형식에 맞는지 확인
# 단, 성별코드는 1 ~ 4 이어야함
# ex) 123456-1234567
str = '123456-1234567'

re.search('[0-9]{6}-[0-9]{7}', str)
re.search('\d{6}-\d{7}', str)
re.search('\d{6}-[1-4]\d{6}' , str)

# fname 이라는 변수가 이미지 파일 형식에 맞는지 확인
# 확장자는 jpg, png, gif, bmp 중에 하나임
str = 'abcde.gif'

re.search('[0-9a-zA-Z]+.[jpg|png|gif|bmp]+', str)
re.search('\w+.jpg|png|gif|bmp', str)

# color 변수는 html 16 진수 색상코드 형식에 맞는지 확인
# '#00AABC', '#EFEFEF', '#0000FF'
str = '#00AABC', '#EFEFEF', '#0000FF'








