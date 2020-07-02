# 공동 주택관리 정보시스템, k-apt.go.kr
# 2020.06 서울, 강남구, 삼성동, 아이파크삼성동
# 아파트 주차대수 (지상, 지하)

from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'http://k-apt.go.kr'
executable = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

chrome = webdriver.Chrome(executable_path=executable)

# 크롬 브라우저의 창 크기를 최대로 키움
chrome.maximize_window()
time.sleep(1)

# 지정한 사이트로 이동
chrome.get(url)
time.sleep(2)

# 팝업창을 닫음
# close = chrome.find_element_by_css_selector('div close a'):
# close = chrome.find_element_by_css_selector('div.layerPopupTitle div a')
# close.click()
# time.sleep(1)

# 팝업창 닫음 2 : 자바스크립트 함수
# 팝업창에 닫기버튼에 적용된
# 자바스크립트 함수를 직접 호출해서 닫을수도 있음
# chrome.execute_script('popupClose')
chrome.execute_script('closeLyserPopup("popup_20200618")')

# 단지정보 메뉴 클릭 (1)
# chrome.find_element_by_css_selector(
#     '#lnbMenu li:nth-Child(2) a').click()
# time.sleep(2)

# 단지정보 메뉴 클릭 (2)
# chrome.find_element_by_css_selector(
#     'a[title="단지정보"]').click()
# time.sleep(2)

# 단지정보 메뉴 클릭 (3)
# xpath : xml 문서의 특정요소나 속성에 접근하기 위해
# 경로를 지정하는 언어
chrome.find_element_by_xpath(
    '//*[@id="lnbMenu"]/li[2]/a').click()
time.sleep(2)

# 단지정보 메뉴에서
# 발생월기준 : 년도, combo_YYYY
# 발생월기준 : 월, combo_MM
# 조회기준 : 광역시/도, combo_SIDO
# 조회기준 : 시구군, combo_SGG
# 조회기준 : 읍면동, combo_EMD
# 아파트 목록 : 단지명, tr[?]/td[2]

# 년 설정
chrome.find_element_by_xpath(
    '//*[@class="combo_YYYY"]/option[text()="2020"]')\
    .click()
time.sleep(1)

# 월 설정
chrome.find_element_by_xpath(
    '//*[@class="combo_MM"]/option[text()="06"]')\
    .click()
time.sleep(1)

# 시도 설정
chrome.find_element_by_xpath(
    '//*[@class="combo_SIDO"]/option[text()="서울특별시"]')\
    .click()
time.sleep(1)

# 구군 설정
chrome.find_element_by_xpath(
    '//*[@class="combo_SGG"]/option[text()="강남구"]')\
    .click()
time.sleep(1)

# 동 설정
chrome.find_element_by_xpath(
    '//*[@class="combo_EMD"]/option[text()="개포동"]')\
    .click()
time.sleep(1)

# 단지정보 설정
chrome.find_element_by_xpath('//tr[@id="15"]').click()
time.sleep(1)


chrome.close()



