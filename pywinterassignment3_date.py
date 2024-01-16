from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://naver.com/')
time.sleep(3)
element = driver.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[1]/a/span[2]')
driver.execute_script("var date= new Date(); arguments[0].innerText= `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`", element)
#변수를 문자열 안에 입력하는 거라서 ${}
time.sleep(5)