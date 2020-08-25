from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(5)

source1=driver.find_element_by_id("box6")
target1=driver.find_element_by_id("box106")
source2=driver.find_element_by_id("box7")
target2=driver.find_element_by_id("box107")
action=ActionChains(driver)
action.drag_and_drop(source1,target1).drag_and_drop(source2,target2).perform()
