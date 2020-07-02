# 예외처리
# 프로그램을 만들다보면 수많은 에러가 발생함
# 코드를 잘못 작성하거나, 실행상의 문제로 인해
# 에러가 발생하면 프로그램 실행이 중단되기도함

# 하지만, 프로그램이 중단되는 것을 피하기 위해
# 이러한 에러는 무시하고 넘어가줬으면 하는때도 있음
# 에러에 따른 적절한 처리를 하고싶을 때도 있을것임

# 파이썬에서는 try-catch-except 구문으로
# 예외처리를 할 수 있음

# error 와 except 차이 비교
# 에러 : 프로그램 실행중 오작동이나 비정상적 종료를
# 유발하게하는 원인

# 예외 : 개발자가 완전히 조치할 수 없지만
# 어느정도 수습할 수 있는 수준의 덜 심각한 오류
# 예외처리를 통해 프로그램의 비정상 종료를 막을 수 있음

# 오류발생 예시
print("-프로그램 시작-")
print(10/5)
print("-프로그램 끝-")

print("-프로그램 시작-")
print(10/0)     # 0 으로 나눔 => 예외발생
print("-프로그램 끝-")

nums = [1, 2, 3]
print("-프로그램 시작-")
print(nums[2])
print("-프로그램 끝-")

print("-프로그램 시작-")
print(nums[10])     # 존재하지 않는 리스트 요소 참조
print("-프로그램 끝-")

# 예외처리 구문
# try:
#     오류가 발생할 구문
# except:
#     오류발생시 처리할 코드

print("-프로그램 시작-")
try:
    print(10/0) # 오류가 발생할만한 코드
except:
    print('0으로 나눌수 없어요!!')
print("-프로그램 끝-")


nums = [1, 2, 3]
print("-프로그램 시작-")
try:
    print(nums[10])  # 오류가 발생할만한 코드
except:
    print('리스트에 존재하지 않아요')
print("-프로그램 끝-")

# 발생한 오류를 특정지어 예외처리하기
# try:
#     오류가 발생할 구문
# except 발생한 오류유형:
#     오류발생시 처리할 코드

try:
    print(10 / 0)
except ZeroDivisionError:
    print('0으로 나눌수없음!!')

nums = [1, 2, 3]
print("-프로그램 시작-")
try:
    print(nums[10])
except IndexError:
    print('리스트에 존재하지 않아요')
print("-프로그램 끝-")

fname = 'EMPLOYEES.CSV'
try:
    with open(fname) as f:
        f.read()
except FileNotFoundError:
    print('파일이 존재하지 않아요!')


# 예외의 에러 메세지 받아오기
# try:
#     오류가 발생할 구문
# except 예외 as 변수:
#     오류발생시 처리할 코드

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)

try:
    print(nums[10])
except IndexError as e:
    print(e)

try:
    with open(fname) as f:
        f.read()
except FileNotFoundError as e:
    print(e)

# 복수 예외 처리하기
nums = [10, 20, 30]
try:
    idx = int(input('피젯수로 사용할 숫자의 인덱스는?'))
    x = int(input('젯수로 사용할 숫자는?'))
    print(nums[idx] / x)
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

# 여러개의 예외처리 코드를 작성하더라도
# 발생한 예외처리 순서에 의해 나머지 예외처리코드는
# 실행되지 않을 수도 있음
# 0 으로 나눈 예외 때문에 리스트 인덱스 예외는 실행x

# 예외 처리 회피하기 : pass
# 예외처리할 코드가 없다는 의미
# 따라서, 아무런 동작을 하지 않고 다음 코드를 실행함

# try:
#     코드
# except:
#     pass

try:
    print(nums[10])
except IndexError as e:
    pass

print('이 글이 보이나요')

# 예외와 상관없이 항상 코드 실행 : finally
# 주로 자원반납과 관련된 코드들에 사용

# try:
#     코드
# except:
#     예외처리
# finally:
#     예외여부와 상관없이 항상 실행할 코드

# py2 방식으로 파일읽기 코드 작성
f = open(fname)
f.read()    # 오류발생!
f.close()
# 오류가 발생해서 실행이 중단되는 경우
# f.close()는 실행되지 못함
# 한편, 작업중인 파일을 닫는 f.close()는
# 예외가 발생하든 발생하지 않든
# 언제나 실행되어야 하는 코드
# python3 에서는 with 구문을 사용하면 자동으로
# close 해주므로 직접 닫을 필요는 없음

f = open('c:/java/datasets/applewood.txt')
try:
    f.write()   # 읽기모드로 파일을 열었는데
                # 쓸려고 시도 -> 오류 발생!
except TypeError as e:
    print(e)
finally:
    f.close()   # 열었던 파일 닫음




