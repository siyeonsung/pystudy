# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("https://search.naver.com/search.naver?sm=tab_sug.top&where=image&query=%EB%8F%99%EA%B5%AD%EB%8C%80+&oquery=%EB%8F%99%EA%B5%AD%EB%8C%80+%EC%9D%B4%EB%AF%B8%EC%A7%80&tqi=iMK%2F%2FsprvmsssOknhU8ssssstgl-431089&acq=%EB%8F%99%EA%B5%AD%EB%8C%80+&acr=1&qdt=0#imgId=image_sas%3Ablog101634302%7C12%7C223120228374_929140564")
time.sleep(3)
el = driver.find_element(
    By.XPATH, '//*[@id="main_pack"]/section[2]/div[1]/div/div/div[1]/div[1]/div/div/div/img')
el_url = el.get_attribute('src') #img src 주소값을 변수에 저장
print(el_url)
request.urlretrieve(el_url, "dongguk.jpg") #현재 폴더에 dongguk.jpg라는 이름으로 파일 생성, 이미지 데이터 저장
driver.close()