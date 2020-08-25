from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("hello")
time.sleep(5)
driver.quit()


