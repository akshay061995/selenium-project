from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

#operating the alert window

#driver.switch_to_alert().accept()  #closes the alert window by selecting ok button

driver.switch_to_alert().dismiss()  #closes the alert window by selecting cancel button