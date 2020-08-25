from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://amazon.com")

#find cookies
cookie=driver.get_cookies()
print(len(cookie))
print(cookie)

#add cookies

cook={'name':'akshay','value':'12345'}
driver.add_cookie(cook)

cookie=driver.get_cookies()
print(len(cookie))
print(cookie)

#delete cookies

driver.delete_cookie('akshay')
time.sleep(3)

cookie=driver.get_cookies()
print(len(cookie))
print(cookie)

#delete all cookies

driver.delete_all_cookies()

cookie=driver.get_cookies()
print(len(cookie))
print(cookie)
