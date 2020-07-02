# 크롤링 crawling
# 웹 상에 존재하는 다양한 컨텐츠를 수집하는 행위
# html 문서를 통째로 읽어서 내용을 분석한 뒤
# 필요한 데이터만 골라서 추출하는 것이 주된 작업

# 파이썬으로 크롤링하기
# urllib/urllib2 : 사용하기 무난한 크롤링 패키지
#                코드 단순, 내장 패키지
# requests : 따로 설치, urllib 보다 고급기능 제공
# lxml : ElementTree 보다 성능 좋은 xml/html 분석기

# pip install requests
# pip install lxml
# pip install cssselect
import pymysql
import requests
import lxml.html
from lxml.cssselect import CSSSelector

# 한빛미디어 홈페이지의 베스트셀러 페이지의
# 도서정보(이미지, 도서명, 저자, 가격)를 수집하세요
# https://www.hanbit.co.kr/store/books/bestseller_list.html

url = 'https://www.hanbit.co.kr/store/books/bestseller_list.html'
res = requests.get(url)
# 지정한 url 상의 모든 html 을 가져옴
print(res.status_code, res.encoding,
      res.headers['content-type'])
# requests 패키지 실행 후 유용한 변수로 결과 확인
# http 응답코드(요청처리 여부 확인용)
# 응답받은 컨텐츠의 인코딩, 컨텐츠 유형 확인

print(res.text)     # 스크래핑한 결과를 문자형으로 출력
print(res.content)  # 스크래핑한 결과를 바이트형으로 출력

html = res.text
# 스크래핑한 결과를 분석해서 필요한 데이터를
# 추출하기 위해 따로 변수로 저장

root = lxml.html.fromstring(html)
# html 변수에 저장된 문서 내 요소들을
# 탐색하기 편하도록 계층구조로 생성

titles = []
bookimgs = []
bauthors = []
bprices = []

# 도서명 추출
for title in root.cssselect('p.book_tit a'):
    # print(title.text_content())
    titles.append(title.text_content())
    # 도서명 추출해서 titles 라는 리스트에 저장

# 도서 이미지 추출
for bookimg in root.cssselect('img.thumb'):
    # print(bookimg.get('src'))
    bookimgs.append(bookimg.get('src'))

# 도서 저자 추출
for author in root.cssselect('p.book_writer'):
    # print(author.text_content())
    bauthors.append(author.text_content())

# 도서 가격 추출
for price in root.cssselect('span.price'):
    # print(price.text_content())
    bprices.append(price.text_content())

for i in range(15):
    print(f'{titles[i]}')

for i in range(15):
    print(f'{bookimgs[i]}')

for i in range(15):
    print(f'{bauthors[i]}')

for i in range(15):
    print(f'{bprices[i]}')

# 네이버 검색
# search.naver.com/search.naver?query=검색어
# 네이버에 검색어를 입력하고 검색결과에서 데이터 추출
# 질의문자열을 이용해서 검색하고
# 그 결과에서 필요한 데이터를 추출함

# 특정 사이트는 스크래핑이나 크롤링을 막기 위한 방법으로
# 사이트에 접속하는 사용자의 useragent 를 확인함
# UA 없이 사이트 접속을 시도하면 접속권한 거부의 의미로
# 403 응답코드와 함께 접속을 금지하기도 함

query = input('네이버 검색을 위한 검색어를 입력하세요')

url = 'https://search.naver.com/search.naver'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
params = {'query': 'query'}

res = requests.get(url, headers=headers, params=params)

html = res.text
root = lxml.html.fromstring(html)

# 블로그, 웹사이트, 네이버책, 포스트 등의 제목과 링크 추출
titles = []
links = []

# 블로그 제목과 링크 추출
for blog in root.cssselect('a.sh_blog_title'):
    titles.append(blog.text_content())
    links.append(blog.get('href'))

# 웹사이트 제목과 링크 추출
for web in root.cssselect('a.title_link'):
    titles.append(web.text_content())
    links.append(web.get('href'))

# 네이버책 제목과 링크 추출
for book in root.cssselect('li.sh_book_top dl dt a'):
    titles.append(book.text_content())
    links.append(book.get('href'))

# 포스트 제목과 링크 추출
for post in root.cssselect('div.sp_post ul li dl dt a'):
    titles.append(post.text_content())
    links.append(post.get('href'))

for i in range(len(titles)):
    print(f'{titles[i]} {links[i]}')

# 검색한 결과를 데이터베이스에 저장
# naverfind 라는 테이블을 만듦

# create table naverfind (
#     no int primary key auto_increment,
#     title varchar(500),
#     link varchar(500),
#     userid varchar(18),
#     regdata datetime default current_timestamp
# );

import pymysql

url = 'min.cxm33cuzkkko.ap-northeast-2.rds.amazonaws.com'
uid = 'bigdata'
pwd = 'bigdata2020'
db = 'bigdata'
charset = 'utf8'

# 이모지 emoji 저장시 유의사항
# 일반적인 유니코드 문자는 3바이트 이내의 문자를 의미함
# 하지만, 이모지는 4바이트로 표현하는 문자이기 때문에
# 일반적인 방법으로는 입력이 되더라도 제대로 표시되지 않을 수 있음
# 해결책은 데이터베이스 인코딩을 utf-8에서 utf8-mb4로 설정하는 것임
# 따라서, 서버와 데이터베이스와 테이블이 utf8-mb4로 설정되면
# 이모지도 정상적으로 저장되고 표현할 수 있음

conn = pymysql.connect(host=url, db=db, user=uid,
                       password=pwd, charset=charset)

sql =' insert into naverfind (title,link,userid) ' \
     ' values (%s, %s, %s) '

cursor = conn.cursor(pymysql.cursors.DictCursor)

for i in range(len(titles)):
    param = (titles[i], links[i], 'zzyzzy')
    cursor.execute(sql, param)
    conn.commit()

cursor.close()
conn.close()

# 뉴스 사이트를 크롤링해서 데이터베이스에 저장
# mbc   : imnews.imbc.com/
# jtbc  : news.jtbc.joins.com
# naver : news.naver.com

# jtbc 뉴스 사이트에서 사진, 제목, 기사미리보기, 뉴스범주 등을 크롤링해서
# jtbcnews 테이블에 저장

url = 'http://news.jtbc.joins.com/section/list.aspx'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


res = requests.get(url, headers=headers)

html = res.text
root = lxml.html.fromstring(html)

npics = []
titles = []
previews = []
ntypes = []

# 사진 npic 추출
for photo in root.cssselect('dd.photo a img'):
    npics.append(photo.get('src'))

# 제목 title 추출
for title in root.cssselect('dt.title_cr'):
    title = title.text_content().replace('\t', '')
    title = title.replace('\r\n', '')
    title = title.replace(' ', '')
    titles.append(title)

# 기사 미리보기 preview 추출
for preview in root.cssselect('dd.read_cr'):
    preview = preview.text_content().replace('\t', '')
    preview = preview.replace('\r\n', '')
    preview = preview.replace(' ', '')
    previews.append(preview)

# 범주 ntype 추출
for ntype in root.cssselect('span.location'):
    ntype = ntype.text_content().replace('\t', '')
    ntype = ntype.replace('\r\n', '')
    ntype = ntype.replace(' ', '')
    ntype = ntype.split('>')[1]

    ntypes.append(ntype[:len(ntype)-1])

# 참고 : 간혹 기사중에 사진이 없는 경우가 존재함
# 추출 결과를 테이블에 저장
# create table jtbcnews (
#   no int primary key auto increment,
#   title varchar(200),
#   preview varchar(1500),
#   ntype varchar(10),
#   npic varchar(100),
#   regdata datetime default current_timestamp
# );

url = 'min.cxm33cuzkkko.ap-northeast-2.rds.amazonaws.com'
uid = 'bigdata'
pwd = 'bigdata2020'
db = 'bigdata'
charset = 'utf8'

conn = pymysql.connect(host=url, db=db, user=uid,
                       password=pwd, charset=charset)
cursor = conn.cursor()

sql = "insert into jtbcnews (title,preview,ntype,npic) values (%s,%s,%s,%s)"

for i in range(len(npics)):
    param = (titles[i], preview[i], ntypes[i], npics[i])
    cursor.execute(sql, param)
    conn.commit()

cursor.close()
conn.close()

# 사진이 빠진 기사 수집
url = 'http://news.jtbc.joins.com/section/list.aspx?pdate=20200630&scode=&copyright=&pgi=3'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

res = requests.get(url, headers=headers)
html = res.text
root = lxml.html.fromstring(html)

npics = []
titles = []
previews = []
ntypes = []

for dl in root.cssselect('#section_list li dl'):
    # 현재 페이지에서 id 가 section_list 이고
    # 자식 요소가 li 밑의 모든 dl 요소들을 가져옴
    try:
        img = dl.cssselect('dd.photo')[0]
        # dl 요소의 자식 요소들 중
        # class 가 photo인 dd 요소들 중
        # 첫번째 dd 요소를 가져옴
        img = img.cssselect('img')[0].get('src')
        npics.append(img)
    except:
        npics.append('-')

    title = dl.cssselect('dt.title_cr a')[0]
    title = title.text_content()
    titles.append(title)

    preview = dl.cssselect('dd.read_cr a')[0]
    preview = preview.text_content()
    previews.append(preview)

    ntype = dl.cssselect('dd.info span')[0]
    ntype = ntype.text_content().replace('\t', '')
    ntype = ntype.replace('\r\n', '')
    ntype = ntype.replace(' ', '')
    ntype = ntype.split('>')[1]
    ntypes.append(ntype[:len(ntype)-1])