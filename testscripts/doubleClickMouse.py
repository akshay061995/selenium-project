from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()


element=driver.find_elements_by_xpath("//*[@id='HTML10']/div[1]/button")


action=ActionChains(driver)             #object of Actionchains class

action.double_click(element).perform()     #performs double click