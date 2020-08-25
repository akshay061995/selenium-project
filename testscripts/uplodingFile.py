from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_name("RESULT_FileUpload-10").send_keys("C:/Users/akshay/Downloads/AkshayKadam_Resumes/akshaykadam_resume.pdf")