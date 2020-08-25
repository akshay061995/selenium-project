from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://flpkart.com")
driver.maximize_window()

#screenshot 1 command
#driver.save_screenshot("C:\pycharm\screenshot\homepage.png")

# 2 command
driver.get_screenshot_as_file("C:\pycharm\screenshot\homepage2.png")
driver.quit()