from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://google.com")
print(driver.title)
driver.get("http://facebook.com")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)
#driver.find_element_by_name("q").send_keys("mercedes cars")
#driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
#driver.close()