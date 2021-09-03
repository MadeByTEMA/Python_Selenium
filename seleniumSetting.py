from seleniumrequests import Chrome
from selenium import webdriver

def initDriver():
    driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
    return driver

def goGetPage(driver: webdriver, url: str, params: dict):
    str: str = ''
    for key in params.keys():
        value = params.get(key)
        if (str == ''):
            str += '?' + key + '=' + value
        else:
            str = '&' + key + '=' + value
    driver.get(url + str)

