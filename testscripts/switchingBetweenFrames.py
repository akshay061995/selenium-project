from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://google.com")

driver.switch_to.frame("frame1 name or id")
driver.find_element_by_link_text().click()
time.sleep(5)

driver.switch_to.default_content()

driver.switch_to.frame("frame2 name or id")
driver.find_element_by_link_text().click()
time.sleep(5)

driver.switch_to.default_content()

driver.switch_to.frame("frame3 name or id")
driver.find_element_by_link_text().click()
time.sleep(5)

driver.switch_to.default_content()

