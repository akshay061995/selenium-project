from selenium  import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")
#driver.maximize_window()
#driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

#driver.execute_script("window.scrollBy(0,1000)","")     #scroll down by the specified pixel

#flag=driver.find_element_by_xpath("//*[@id='resizable']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)        #scroll till we find the element in th page


driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")    #scroll to the end of the page