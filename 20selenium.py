# 셀레니엄 selenium
# 동적으로 생성되는 페이지에서 특정 컨텐츠를 추출하거나
# 로그인등의 작업 후 특정 정보를 추출하거나
# 반복적인 작업을 통해 정보를 추출하거나
# 마우스 클릭 등 특정 작업을 무인 자동으로 해야하는 경우
# 브라우져 자동화 프로그램인 selenium을 이용하면 처리 가능
# www.selenium.dev

# 실습에는 크롬드라이버를 사용함
# 사용중인 크롬브라우저와 버전을 일치시켜야함

# 파이썬용 셀레니엄 패키지 설치
# pip install selenium

# requests, bs4 로 스크래핑할 수 없는
# 동적 데이터를 포함하는 웹페이지를
# 원격 조작이 가능한 특수한 웹브라우저를 이용해서 처리

from selenium import webdriver
from bs4 import BeautifulSoup

# 다음 증권 : 오늘의 증시(코스피/코스닥 지수), 환율조회
url ='https://finance.daum.net/'

# 크롬 드라이버 실행
chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 지정한 url 로 접속
chrome.get(url)

# 응답으로 받은 웹페이지 소스 출력
print(chrome.page_source)
res = chrome.page_source

# 작업 종료시 브라우져를 닫음
chrome.close()

# bs4 로 DOM 계층구조 생성

html = BeautifulSoup(res, 'lxml')

# 오늘의 증시(코스피/코스닥 지수) 알아내기
for stock in html.select('div.stock div span.num'):
    stock = stock.text.replace('\n', '|')
    stock = stock[1:]
    stock = stock[:len(stock)-1]
    print(stock)

# 환율조회 알아내기
url = 'https://finance.daum.net/exchanges'
chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
chrome.get(url)
print(chrome.page_source)
res = chrome.page_source
chrome.close()
html = BeautifulSoup(res, 'lxml')

for stock1 in html.select('div.tableB div div table tbody tr'):
    stock1 = stock1.text.strip().replace(' ', '')
    stock1 = stock1.replace('\n\n\n', '|')
    stock1 = stock1.replace('\n\n', '|')
    stock1 = stock1.replace('\n', '|')
    print(stock1)

# 코레일 로그인
import time
url ='http://korail.go.kr'
userid = '2071955155'
passwd = 'tjckdals0229!'

chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')


chrome.get(url)
main_page = chrome.current_window_handle    # 팝업 제어용

time.sleep(2)   # 페이지가 간혹 늦게 뜨는 경우
                # 웹페이지 소스를 다 못 불러오는 경우 방지

# 팝업창 찾기
for handle in chrome.window_handles:
    # 크롬을 통해 띄운 창들을 조사해서
    if handle != main_page:
        # 조사한 창이 main_page 가 아니면 
        popwin = handle
        # 팝업창으로 인지함
time.sleep(1)

# 셀레니움 제어를 팝업창으로 옮김
chrome.switch_to.window(popwin)
time.sleep(1)

# 팝업창의 확인 버튼을 찾아 닫음
closebtn = chrome.find_element_by_css_selector("a[title='확인']")
closebtn.click()
time.sleep(1)

# 셀레니엄 제어를 메인으로 옮김
chrome.switch_to.window(main_page)
time.sleep(1)

# 로그인 버튼을 클릭해서 로그인 페이지로 이동
link = 'ul.gnb_list > li:nth-child(2) > a'
loginbtn = chrome.find_element_by_css_selector(link)

mouse = webdriver.ActionChains(chrome)
# 셀레니움에서 마우스를 이용한 작업을 초기화함
mouse.move_to_element(loginbtn).click().perform()
# 마우스를 특정 요소로 옮겨서 클릭 이벤트 발생
time.sleep(2)

# 로그인 정보 입력하고 로그인
uid = chrome.find_element_by_id('txtMember')
pwd = chrome.find_element_by_id('txtPwd')

uid.send_keys(userid)
time.sleep(2)
pwd.send_keys(passwd)
time.sleep(2)

# 로그인 버튼 클릭
loginbtn = chrome.find_element_by_css_selector("img[alt='확인']")
mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(loginbtn).click().perform()
time.sleep(2)

# 로그인한 후 메인 페이지에서
# 승차권 예매 버튼 클릭
link = '#res_cont_tab01 > form > div > fieldset > p > a > img'
loginbtn = chrome.find_element_by_css_selector(link)
mouse = webdriver.ActionChains(chrome)

# 셀레니엄에서 마우스를 이용한 작업을 준비함
mouse.move_to_element(loginbtn).click().perform()

# 마우스를 특징 요소로 옮겨서 클릭 이벤트 발생
time.sleep(2)

# 크롬 드라이버 종료
chrome.close()

# 구글 로그인 후 메일/쪽지 수 체크
import time
url ='https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Drm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
userid = '0229cm@gmail.com'
passwd = ''

chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

chrome.get(url)
time.sleep(2)   # 페이지가 간혹 늦게 뜨는 경우
                # 웹페이지 소스를 다 못 불러오는 경우 방지

# 로그인 버튼을 클릭해서 로그인 페이지로 이동
link = '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div.d2CFce.cDSmF > div > div.aCsJod.oJeWuf > div > div.Xb9hP'
loginbtn = chrome.find_element_by_css_selector(link)

mouse = webdriver.ActionChains(chrome)
# 셀레니움에서 마우스를 이용한 작업을 초기화함
mouse.move_to_element(loginbtn).click().perform()
# 마우스를 특정 요소로 옮겨서 클릭 이벤트 발생
time.sleep(2)

# 로그인 정보 입력하고 로그인
uid = chrome.find_element_by_id('identifierId')

uid.send_keys(userid)
time.sleep(2)


# 로그인 버튼 클릭
loginbtn = chrome.find_element_by_css_selector("div[span='다음']")
mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(loginbtn).click().perform()
time.sleep(2)

# 크롬 드라이버 종료
chrome.close()




# 네이버 로그인 후 메일/쪽지 수 체크
url = 'https://naver.com'

chrome = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
chrome.get(url)
time.sleep(2)

# 로그인 버튼을 찾아 클릭
loginbtn = chrome.find_element_by_class_name('link_login')
loginbtn.click()
time.sleep(1)

# id, pw를 입력할 곳을 찾음
id = chrome.find_element_by_name('id')
pw = chrome.find_element_by_name('pw')
id.clear()  # input 요소에 입력된 내용을 지울 수 있음
pw.clear()  # input 요소에 입력된 내용을 지울 수 있음

# id, pw 를 입력함 (1) - 보안상의 이유로 captcha 가 표시됨
# id.send_keys('abc123')
# time.sleep(1)
# pw.send_keys('987xyz')
# time.sleep(1)

# id, pw 를 입력함 (2) - pyperclip 패키지 이용
# pip install pyperclip
# 아이디/비번을 클립보드를 통해 입력함
import pyperclip
from selenium.webdriver.common.keys import Keys

id.click()
pyperclip.copy('abc123')
id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pw.click()
pyperclip.copy('123456')
pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
loginbtn = chrome.find_element_by_id('log.login')
loginbtn.click()


# 크롬 드라이버 종료
chrome.close()

# headless selenium
# 브라우저를 띄우지 않고 지정한 웹사이트의 내용을 추출
from selenium.webdriver.chrome.options import Options

url = 'https://www.hanbit.co.kr/store/store_submain.html'
executable = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

# headless 를 위한 설정
options = Options()
options.add_argument('--headless')

chrome = webdriver.Chrome(executable_path=executable, options=options)

chrome.get(url)
res = chrome.page_source
html = BeautifulSoup(res, 'lxml')

for title in html.select('p.book_tit a'):
    print(title.text)

chrome.close()

# k-apt.go.kr

# instagram









