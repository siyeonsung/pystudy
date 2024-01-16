from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

search=input("이미지를 다운받을 검색어 입력: ")
driver = webdriver.Chrome()
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+search)
time.sleep(3)
element= driver.find_element(By.XPATH,'//*[@id="footer"]/div[2]/div/span[5]/a/i')
for i in range(1,100):
    try:
        el = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[2]/div[1]/div/div/div[1]/div[{}]/div/div/div/img'.format(i))
        el_url = el.get_attribute('src') #img src 주소값을 변수에 저장
        print(el_url)
        request.urlretrieve(el_url, f"{i}.jpg")
    except:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);", element)
driver.close()