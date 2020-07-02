# 파일 입출력
# 지금까지 값을 입력받을때는
# 사용자가 직접 키보드로 입력하는 방식을 사용했고
# 값을 출력할때는 모니터 화면에 표시하는 방식을 사용했음

# 하지만, 값을 입력받거나 출력하는 방법은 이게 다가 아님
# 파일을 통해 값을 입력/출력할 수 있고
# 네트워크를 통해 값을 입력/출력할 수 있음

# 프로그램 실행 중 생성된 데이터들은
# 주로 메모리 내에 존재하는데
# 프로그램 종료시 같이 소멸됨
# 데이터의 영속성persistence을 부여하기 위해서는
# 데이터르 저장장치에 보관해서
# 데이터가 소멸되지 않도록 하는 것이 중요!

# 파일쓰기 : 데이터를 파일에 기록
# 파일객체변수 = open(경로,모드)      # py2
# with open(경로,모드) as 파일객체변수# py3

# 파일모드 : 파일작업 종류
# w(쓰기),a(추가쓰기),t(텍스트파일 쓰기),b(바이너리파일 쓰기)

# 파일쓰기 작업이 끝나면 반드시 close 해줘야 함
# 단, with문을 사용하는 경우 close 생략 가능
import os
from turtledemo.chaos import line

os.chdir('c:/java')
with open('sayHello.dat','w') as f:
    f.write('Hello,World!') # 파일에 텍스트 쓰기

# 사용자로부터 단을 입력받아 그 단을 파일에
# 저장하는 코드를 작성하세요
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ...
# 3 x 9 = 27
# (파일명 : gugudan01.dat)
import os
dan = int(input('단을 입력하세요'))
with open('gugudan01.dat','w') as f:
    for i in range(1, 9 + 1):
        # print('%d x %d = %d' % (dan, i, dan * i))
        gugu = f'{dan}x{i}={dan*i}\n'
        f.write(gugu)

# Q 학생으로부터 이름,국어,영어,수학 점수를 입력받아
# 총점,평균,학점을 계산하고 입력값과 결과들을
# 파일에 저장하세요 (파일명 : sungjuk.dat)
# 단, 점수는 임의로 입력하고,, 이름은 혜교,지현,수지로
# 입력하고 파일에 저장하는 형식은
# "이름,국어,영어,수학,총점,평균,학점" 순으로 작성함
# => 혜교,99,98,99,297,99.5,수

# 성적데이터 입력부분
name = input('이름을 입력하세요')
kor = int(input('국어점수를 입력하세요'))
eng = int(input('영어점수를 입력하세요'))
mat = int(input('수학점수를 입력하세요'))

# 총점 평균 학점 계산
tot = kor + eng + mat
avg = tot/3
if avg >= 90: grd = '수'
elif avg >= 80:grd = '우'
elif avg >= 70:grd = '미'
elif avg >= 60:grd = '양'
else:grd = '가'

# 파일에 저장하기
sj = f'{name},{kor},{eng},{mat},{tot},{avg:.1f},{grd}\n'
# with open('sungjuk.dat','w') as f:
#     f.write(sungjuk)

# 3명의 설적데이터를 입력하는 경우
# 실질적으로 파일에는 맨 마지막 학생 데이터만 저장됨
# 파일모드를 w 로 설정하면
# 매번 새로운 파일을 생성해서 데이터를 저장함
# 따라서, 파일을 쓸때 기존에 저장한 파일을 이용하려면
# 파일모드를 a(추가)로 설정해야 함
with open('sungjuk.dat','a') as f:
    f.write(sj)

# 파일 읽기 : 파일에 저장된 데이터를 읽어 처리하기
# 변수 = open(경로, 모드)     # py2
# with open(경로,모드)       # py3
# 파일모드 : r(읽기,생략가능), t(텍스트 읽기), b(바이타리 읽기)

# 구구단 파일(gugudan01.dat)읽기
with open('gugudan01.dat') as f:
    lines = f.read()    # 파일의 모든 내용을 문자열로 읽음
    print(lines)

# 구구단 파일(gugudan01.dat)읽기(2)
with open('gugudan01.dat') as f:
    lines = f.readlines()     # 파일 내용을 행 단위로 읽어서 리스트에 저장
#   print(lines)
    for line in lines:
        print(lines)

# 위 예제에서 생성한 sungjuk.dat 를 읽어서
# 다음과 같은 형식으로 출력하세요
# 이름 : xxx
# 국어 : xx, 영어 : xx, 수학 : xx
# 총점 : xx, 평균 : xx, 학점 : xx
# =====================
with open('sungjuk.dat') as f:
    lines = f.readlines()     # 성적데이터를 행단위로 읽어서 리스트에 저장
    for line in lines:        # 리스트에서 1행씩 읽어서
       sjs = line.split(',')    # 콤마로 분리
       sj = f'이름:{sjs[0]}\n' \
            f'국어 : {sjs[1]}, 영어 : {sjs[2]}, 수학 : {sjs[3]}\n'\
            f'총점 : {sjs[4]}, 평균 : {float(sjs[5]):.1f}, 학점 : {sjs[6]}\n' \
            f'========================================\n'
       print(sj)































