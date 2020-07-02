# BeautifulSoup
# www.crummy.com/software/BeautifulSoup
# 유명한 스크래핑/크롤링 패키지
# 이름의 유래는 이상한 나라의 엘리스에 나오는 시에서 따옴
# 주로 HTML/XML 파일에서 데이터 추출시 사용
# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests

url = 'https://www.hanbit.co.kr/store/store_submain.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# 크롤링시 requests 가 웹브라우저처럼 보이게 가짜 요청헤더 생성

res =requests.get(url, headers=headers)

# html = BeautifulSoup(res.text, 'html.parser')
html = BeautifulSoup(res.text, 'lxml')
# requests 로 응답받은 html 소스를
# BeautifulSoup 패지키지의 html.parser 나 lxml 로
# DOM 계층구조로 변환

print(html) # 변환된 소스 출력
print(html.prettify()) # 변환된 소스 예쁘게 출력

print(html.title)   # 소스중에서 title 요소 출력
print(html.title.string)    # 소스중에서 title 요소의 문자열 출력

print(html.p)   # 소스중에서 p 요소 출력
print(html.find_all('p'))   # 소스중에서 모든 p 요소 출력

# 소스중에서 모든 도서제목 출력
for title in html.select('p.book_tit a'):
    # print(title.text)
# 소스중에서 모든 도서제목 출력(화면제어문자 출력)
    print(title.text.strip())

# 도서 이미지 추출
for photo in html.select('img.thumb'):
    print(photo.get('src'))

# 도서 저자 추출
for author in html.select('p.book_writer'):
    print(author.text.strip())

# 도서 가격 추출
for price in html.select('span.price'):
    print(price.text.strip())

# 네이버 증권 : 환전고시환율, 국제시장환율
url = 'https://finance.naver.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

res =requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')

erate1 = []
erate2 = []

for erate in html.select('div.section1 div.group1 table tbody tr'):
    erate = erate.text.replace('\n', '|')
    erate = erate[1:]   # 첫번째 | 제거
    erate = erate[:len(erate)-1]    # 마지막 | 제거
    erate1.append(erate)

for erate in html.select('div.section1 div.group2 table tbody tr'):
    erate = erate.text.replace('\n', '|')
    erate = erate[1:]   # 첫번째 | 제거
    erate = erate[:len(erate)-1]    # 마지막 | 제거
    erate2.append(erate)

for erate in erate1:
    e = erate.split('|')
    print(f'{e[0]} {e[1]} {e[2]}')

for erate in erate2:
    e = erate.split('|')
    print(f'{e[0]} {e[1]} {e[2]}')

# 다음 증권 : 오늘의 증시(코스피/코스닥 지수), 환율조회
url ='https://finance.daum.net/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

res =requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')

for stock in html.select('div.stock'):
    print(stock.text)
# => 내용이 보이지 않음

url = 'https://finance.daum.net/exchanges'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

res =requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')

# for ex in html.select('div.tableB div div table tbody tr'):
for ex in html.select('div.tableB'):
    print(ex.text)
# => 내용이 보이지 않음

# 간혹 특정 웹사이트의 경우
# 실시간으로 내용이 동적으로 바뀌기 때문에
# 정적 페이지 내용만 크롤링하는 requests 패키지로는
# 처리할 수 없음 => 브라우저기반 크롤링 도구인 selenium 이용




