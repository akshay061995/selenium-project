from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

right=driver.find_element_by_xpath("//*[@id='Wikipedia1_wikipedia-search-input']")

action=ActionChains(driver)

action.context_click(right).perform()