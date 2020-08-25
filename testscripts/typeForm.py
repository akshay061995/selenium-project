from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

#termsAndCondition=driver.find_element_by_id("terms").is_selected()
#print(termsAndCondition)
#driver.implicitly_wait(5)
#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div/button")
#driver.find_elements_by_id("consents").click()
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()
driver.implicitly_wait(8)
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()
element=driver.find_element_by_name("country")
drp=Select(element)
print(len(drp.options))

drp.select_by_visible_text("INDIA")