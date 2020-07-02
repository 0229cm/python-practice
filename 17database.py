# 파이썬 데이터베이스 프로그래밍
# 데이터에 영속성을 부여하는 방법 중 하나
# 적은 양의 데이터는 파일입출력을 통해 처리 가능
# 대량의 데이터를 체계적으로 저장해서 원하는 목적에 따라
# 데이터를 처리(검색/수정/삭제) 할 수 있도록 해줌

# 한편, 독립적인 데이터베이스 서버없이 파일기반
# 데이터베이스를 이용해서 간편하게 데이터를 조작할 수도 있음
# 내장형 파일기반 데이터베이스 : splite

# splite
# 내장형 파일기반 데이터베이스
# 서버가 필요없고 복잡한 설정도 필요없으면서
# 트랜잭션이 지원되는 데이터베이스
# 하나의 파일에 데이블, 뷰, 색인, 트리거등이 저장
# 용량이 작아 메모리에 올리기도 쉽고 속도도 빠른편
# 안드로이드, IOS 에는 기본적으로 포함되어 있음
# 단, 복잡하고 용량이 큰 데이터를 저장하기에는 다소 부적절
# sqlite.org

# sqlite 설치법
# sqlite-tools-win32-x86-3320300.zip (2020.06.18 기준)
# 압축해제 후 c:/java 에 splite3.exe 를 복사해둠

# 데이터베이스 생성
# .open 데이터베이스명
# .open bigdata.db

# 회원 테이블 생성
# 회원번호, 아이디, 비번, 이메일, 이름
# create table member(
#     mno int primary key,
#     uid varchar(18) not null,
#     pwd varchar(18) not null,
#     email varchar(18) not null,
#     name varchar(18) not null
# );

# 테이블 확인
# .table
# .schema 테이블명
# pragma table_info('테이블명');

# 데이터 삽입
# 1, abc123, 987xyz, abc123@xyz.com, 수지
# insert into member values(1, 'abc123', '987xyz', 'abc123@xyz.com', '혜교');

# 데이터 조회
# select * from member;

# 출력모드 설정
# .header on
# .mode column
# select * from member;

# 데이터 타입
# integer, text, real, numeric

# sqlite 종료
# .quit

# 파이썬으로 sqlite3 다루기
import sqlite3

conn = sqlite3.connect('bigdata.db')
# 데이터베이스 파일에 연결

cur = conn.cursor()
# SQL 실행을 위해 커서 생성

sql = 'select * from member'
cur.execute(sql)
# sql 문을 생성하고 실행 후 결과를 커서에 저장

while True:
    row = cur.fetchone()
    # 커서로부터 한 행을 읽은 후
    if row == None: break
    # 읽은 행에 내용이 없으면 반복문 종료
    mno = row[0]
    uid = row[1]
    pwd = row[2]
    email = row[3]
    name = row[4]
        # 읽은 행에서 각 열의 값을 추출해서 변수에 저장
    print(f'{mno} {uid} {pwd} {email} {name}')

cur.close()
    # 사용한 데이터베이스 자원 종료


import sqlite3

conn = sqlite3.connect('bigdata.db')

cur = conn.cursor()

sql = 'select * from productTable'
cur.execute(sql)

while Ture:
    rew = cur.fetchone()
    if row == None: break;
    pcode = row[0]
    pname = row[1]
    price = row[2]
    amount = row[3]
    print(f'{pcode} {pname} {price} {amount}')

cur.close()

# 파이썬으로 mysql/mariadb 데이터베이스 다루기
# pymysql 패키지 설치 : pip install pymysql

import pymysql

url = 'min.cxm33cuzkkko.ap-northeast-2.rds.amazonaws.com'
uid = 'bigdata'
pwd = 'bigdata2020'
db = 'bigdata'
charset = 'utf8'

conn = pymysql.connect(host=url, db=db, user=uid,
                       password=pwd, charset=charset)

# mariadb 서버에 연결하고 conn 변수에 저장

sql = 'select name, userid, email from member'
cursor = conn.cursor(pymysql.cursors.DictCursor)
# SQL 문을 생성하고 딕셔너리 커서 생성

cursor.execute(sql)
# SQL 문을 실행하고 결과를 커서에 저장

rows = cursor.fetchall()
# 커서에 저장된 결과를 list 객체에 저장

for row in rows:
    print(f"{row['name']} {row['userid']} {row['email']}")

cursor.close()
conn.close()




