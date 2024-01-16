from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib import request

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/joonggonara/994948311')
time.sleep(3)

# 아이디를 사용하여 전환
driver.switch_to.frame('cafe_main')

el= driver.find_elements(By.TAG_NAME, 'img') #태그네임으로 검색
for i,j in enumerate(el):
    el_url = j.get_attribute('src') #img src 주소값을 변수에 저장
    print(el_url)
    request.urlretrieve(el_url, f"{i}.jpg")
driver.close()