import seleniumSetting
import httpCall

global driver
def initDriver():
    driver = seleniumSetting.initDriver()


def doRes(params: dict):
    initDriver()




seleniumSetting.goGetPage(driver, 'https://keyescape.co.kr/web/home.php', {'go':'rev.make'})
r = httpCall.getHttpsGetCall('https://naver.com', {})
print(r)