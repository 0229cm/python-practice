# 파이썬 표준 모듈
# sys 모듈 : 파이썬 인터프리터가 제공하는
# 여러가지 함수를 다룰수 있는 함수 제공
# exit : 스크립트 종료 함수
# path : 시스템 내 모듈의 전체 경로 출력

import sys

print(sys.path)
sys.exit() # 파이썬 콘솔 종료

# os 모듈
# 시스템 환경변수, 디렉토리, 파일들을 다루는 모듈
# environ: 시스템 환경변수 확인
# chdir : 현재 디렉토리 변경
# getcwd: 현재 디렉토리 확인
# mkdir : 디렉토리 생성
# listdir : 현재 디렉토리의 파일/하위 디렉토리 목록 출력
# rmdir : 디렉토리 삭제
# rename : 파일명 변경

import os
print(os.environ)
print(os.environ['PATH'])
print(os.environ['JAVA_HOME'])

print(os.getcwd())
os.chdir('c:/java/datasets')
print(os.getcwd())
os.mkdir('python')

os.listdir()
os.listdir('c:/java')

# 시간, 날짜 패키지
# 시간과 관련된 정보를 다루는 모듈
# time      : 현재시간을 실수형태로 출력(1970.1.1 기준)
# localtime : 실수형태로 출력된 시간을 현지 시간으로 출력
# ctime     : 현재 시간을 간단하게 출력
# strftime  : 시간/날짜 관련 형식 지정하를 이용해서 출력
# sleep     : 지정한 시간만큼 스크립트 실행을 지연시킴(초)

import time

print(time.time())
print(time.localtime())

# tm_wday : 요일 (0:월, 6:일)
# tm_yday : 경과일수

time.sleep(3)    # 3초 동안 아무것도 하지 않음

print(time.strftime('%Y-%m-%d %a', time.localtime()))
print(time.strftime('%p %I:%M:%S', time.localtime()))

# 달력 모듈
# 달력과 관련된 정보를 다루는 모듈
# calendar  : 지정한 년도의 달력 출력
# prmonth  : 지정한 월 달력 출력
# weekday   : 지정한 일자의 달력 출력(0:월)
# monthrange: 지정한 월의 첫날의 요일과 마지막날 출력
# isleap    : 윤년 여부를 출력

import calendar as cal

print(cal.calendar(2020))
print(cal.prmonth(2020,6))

print(cal.weekday(2020,6,26))
print(cal.monthrange(2020,6))

print(cal.isleap(2020))
print(cal.isleap(2019))

# 난수 생성 모듈
# 난수 생성과 표본 추출 기능을 제공
# randint : 지정한 범위내 난수 생성
# sample  : 리스트에서 무작위 지정한 n개 항목 복원 추출
# choice  : 리스트에서 무작위 항복 복원 추출

import random as r

r.seed(20200626)    # 일정한 난수가 생성되도록 초기화

r.randint(1,45)

menu = ['라면','감밥','짜장','급식','볶음밥','돈까스']
print(r.choice(menu))   # 복원추출
print(r.sample(menu,3)) #지정한 갯수만큼 표본 추출

# numpy 모듈의 choice 함수는 비복원추출 지원

def random_pop(data):   # 비복원추출 함수
    mnu = r.choice(data)
    data.remove(mnu)    #리스트에서 해당 메뉴 제거
    return mnu

random_pop(menu)

# 직렬화/역직렬화 모듈
# 메모리에 생성된 객체를 그대로 파일에 저장하고
# 불러오도록 해주는 모듈
# 데이터 분석결과 모델을 파일로 저장하거나
# 불러올때 주로 많이 사용함
# dump : 객체를 저장한 파일(직렬화)
# load : 파일에 저장된 객체를 메모리에 저장(역직렬화)
import os
import pickle

person = {'name':'혜교','addr':'서울 종로구','age':'32','email':'abc123@987xyz.com'}
print(person)

os.chdir('c:/java/datasets')
with open('person.pickle','wb') as f:
    pickle.dump(person, f)

person = {}
os.chdir('c:/java/datasets')
with open('person.pickle','rb') as f:
    person = pickle.load(f)

print(person)





