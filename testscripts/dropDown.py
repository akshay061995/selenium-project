from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(5)


#click on register link
driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()


#selection of field in dropdown
drp=driver.find_element_by_name("country")
option=Select(drp)
option.select_by_visible_text("INDIA")
