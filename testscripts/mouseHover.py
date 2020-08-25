from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com/")

 
driver.find_element_by_name("txtUsername").send_keys("admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()



admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermanagement=driver.find_element_by_id("menu_admin_UserManagement")
user=driver.find_element_by_id("menu_admin_viewSystemUsers")

action=ActionChains(driver)
action.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform()