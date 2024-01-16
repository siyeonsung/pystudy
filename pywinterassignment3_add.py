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
element = driver.find_element(By.XPATH,'//*[@id="feature"]/div/div[2]/div[1]/div/div/h4/a')
driver.execute_script("arguments[0].innerText = '반갑습니다';", element)
time.sleep(3)