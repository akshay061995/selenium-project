from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://flipkart.com")
#driver.get("http://facebook.com")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[1]/div/div[1]/div[8]/div/a/div/img[2]").click()
#driver.current_window_handle        #returns the handel of the parent window

#driver.window_handles               #returns all the handel of the windows of open browser