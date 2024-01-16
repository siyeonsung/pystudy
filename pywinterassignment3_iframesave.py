from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/joonggonara/994948311')
time.sleep(3)

# 아이디를 사용하여 전환
driver.switch_to.frame('cafe_main')
a=driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]')
for content in a:
    infile=open('중고나라.txt','a', encoding='utf-8')
    infile.write(content.text)
    infile.close()


# iFrame 나가 기본 콘텐츠로 돌아가기
driver.switch_to.default_content()