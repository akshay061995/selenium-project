from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")
driver.get("http://facebook.com")

user_name = driver.find_element_by_name("email")
print(user_name.is_enabled())
print(user_name.is_displayed())

password = driver.find_element_by_name("pass")
print(password.is_enabled())
print(password.is_displayed())

user_name.send_keys("akshu1947@gmail.com")
password.send_keys("akshay12345")

#driver.find_element_by_name("login").click()
driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]').click()

#driver.find_element_by_xpath('//div[@aria-label="Account"]').click()
driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]").click()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/div/div[1]/div[1]/div").click()