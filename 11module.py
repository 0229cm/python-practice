# 모듈과 패키지
# 매우 복잡하고 긴 파일을 하나의 파일에
# 모두 작성하는 것은 비효율적일 수 있음 - 유지 보수 힘듬
# 또한,여러 사람과 같이 개발하는 경우
# 업무 분담, 작업결과물 통합 역시 어려움

# 모듈 방식을 이용하면 사용용도에 따라
# 파일 별로 구분해서 작성가능
# 타인이 만들어둔 코드를 자신의 프로그램에서 활용가능
# 즉, 모듈은 변수/함수/클래스를 모아둔 파일

# 모듈 사용시 현재 디렉토리에 있는 파일 또는
# 파이썬 라이브러리 디렉토리에 있는 파일을 불러와야 함
# => 가상환경/Lib/site-packages

# 모듈 만들기
# 보통의 파이썬 파일에 함수를 작성
# 저장위치는 현재 디렉토리 또는 site-packages로 지정

# 모듈 불러오기
# 작성한 모듈울 사용하려면 해당 모듈을 메모리에 적재해야 함
# import 명령을 사용해서 모듈을 불러올 수 있음
# import 모듈명(파일명)

# 또한, 모듈내 정의된 변수/함수/클래스를 사용하려면
# 모듈명.변수, 모듈명.함수명, 모듈명.클래스명 형식으로
# 코들르 작성하면 됨

import mymodule1

mymodule1.sayHello()
print(mymodule1.today)


# mymodule2를 작성해서 site-packages에 저장해두고
# 모듈을 불러보세요
import mymodule2

mymodule2.plus(10,20)
print(mymodule2.date)
print(mymodule2.time)

# 매번 함수/변수/클래스 호출시
# 모듈명을 앞에 붙이는 것은 번거롭고 불편함
# 모듈명을 생략하고 함수/변수/클래스를 사용하고 싶다면
# 'from 모듈이름 import 모듈함수' 형식으로 정의하면 됨
from mymodule1 import sayHello

sayHello()

from mymodule2 import plus
print(plus(10,100))

# 한편, from ~ 문장을 사용해서 함수 사용시
# 모듈명응ㄹ 생략할수 있어서 편리하긴함
# 하지만, 같은 이름의 함수가 여러 모듈에 존재한다면?
# 지나친 생략은 코드 작성시 결코 이득이 될수 없음
# => 모듈에 별칭을 사용하도록 하자
# import 모듈이름 as 모듈별칭

import mymodule1 as mm1
import mymodule2 as mm2

print(mm1.today)
print(mm2.date,mm2.time)
mm1.sayHello()
print(mm2.plus(20,30))


# 패키지
# 함수, 클래스들을 용도별로 분리해서
# 작성하는 것을 모듈이라 했음

# 그런데, 이러한 모듈둘이 모여 뒤죽박죽 섞여 있으면
# 이해도, 활용도가 떨어질 수 있음

# 따라서, 모듈둘 역시 성격에 맞게 분류해서 관리해야 함
# 필요성이 대두-패키지를 이용해서 모듈둘울 관리

# 파이썬에서 패키지를 만들려면
# 1) 디렉토리 생성
# 2) __init__.py 파일 생성
# 그런데, py3 이상은 __init__.py 파일 없이도
# 자동으로 패키지 인식 => py2 와의 호환성을 위해 생성해 둠

# 패키지 내 함수를 호출하려면
# import 패키지명.모듈명 선언문 사용

import mypackage.mymodule3

print(mypackage.mymodule3.time)
print(mypackage.mymodule3.square(3))

# 아까와 마찬가지로 별칭을 이용하면
# 패키지명과 모듈명을 줄여 쓸수 있음
import mypackage.mymodule3 as mm3

print(mm3.time)
print(mm3.square(3))


# 모듈의 종류
# 표준모듈, 서드파티 모듈, 사용자 정의모듈등으로 분류
# 표준모듈: 파이썬에서 제공하는 기본 모듈
# 서드파티 모듈 : 영리/비영리 조직에서 제공하는 모듈
# 사용자 정의모듈 : 개인이나 회사에서 직접 만든 모듈

# 표준모듈 확인
import sys
print(sys.builtin_module_names)

import math     # 패키지/모듈 불러오기
dir(math)       # 모듈 내 함수 확인

import random
dir(random)





