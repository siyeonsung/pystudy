from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(3)
element = driver.find_element(By.XPATH,'//*[@id="footer"]/div/div[2]/div/a') 
driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);", element)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)