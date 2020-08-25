from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromeOpton=Options()
#chromeOpton.add_experimental_option("prefs",{"download.default_directory",:"C:\Users\akshay\Downloads\pycharm download files"})

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver",chrome_options=chromeOpton)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("testing")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()