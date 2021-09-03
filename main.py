import seleniumSetting
import httpCall

driver = seleniumSetting.initDriver()
seleniumSetting.goGetPage(driver, 'https://keyescape.co.kr/web/home.php', {'go':'rev.make'})
r = httpCall.getHttpsGetCall('https://naver.com', {})
print(r)