from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint


dr = webdriver.Chrome('./chromedriver_win32/chromedriver.exe') # target page 접근
dr.get("https://www.starbucks.co.kr/menu/drink_list.do") # html sourc
# e 추출
html_source = dr.page_source # BS로 html parsing
soup = BeautifulSoup(html_source, 'html.parser') # 원하는 항목의 데이터만 추출
products = soup.select('.product_list dd a') # 결과 확인

pprint(products)
