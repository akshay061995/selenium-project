from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX
import time

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://flipkart.com")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name("q").send_keys("mobile")
driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button/svg").click()
#driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/ul/li[8]/a/span").click()
#driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div[3]/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/a/div/div/div[1]").click()
#driver.back()
#driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div[3]/div[3]/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/a/div/div/img").click()
#driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div[3]/div[1]/div[2]/div/ul/li/div/button").click()
#wait=WebDriverWait(driver,10)
#element=wait.until(EX.element_to_be_clickable((By.XPATH,"//*[@id='container']/div/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]/ul/li[2]/div/div")))
#element.click()
#driver.find_element_by_name("q").send_keys("redmi mobile")
#driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div/img").click()
#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button/svg").click()