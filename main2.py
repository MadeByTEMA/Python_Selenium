import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.starbucks.co.kr/menu/drink_list.do')
html_source = response.text
print(html_source)

soup = BeautifulSoup(html_source, 'html.parser')
result = soup.select('.proudct_list')

print(result)
