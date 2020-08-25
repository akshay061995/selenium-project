from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)


rows=len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr"))
print(driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td[1]"))

print(rows)
#print(clos)
