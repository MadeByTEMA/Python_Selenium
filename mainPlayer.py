import seleniumSetting
import httpCall

driver = seleniumSetting.initDriver()
r = httpCall.getHttpsGetCall('https://keyescape.co.kr/web/home.php', {'go':'rev.make'})
print(r)