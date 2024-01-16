# #네이버 증권 xpath
# from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
# from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
# from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
# from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
# from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
# from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
# import time

# driver = webdriver.Chrome() #크롬 열기
# driver.get('https://finance.naver.com/sise/lastsearch2.naver')
# time.sleep(1)
# index = (1,2,4,6,11)
# li=[]
# row = 3
# cnt = 0
# while(row<48):
#     if cnt == 5: #다섯개마다 3칸 비어있으니까 3을 더해주는 것
#         cnt = 0
#         row+=3
#     line = [] #li라는 리스트 안에 line이라는 리스트(한 가로줄)을 넣으려는 것
#     for col in index:
#         line.append(driver.find_element(By.XPATH, f'//*[@id="contentarea"]/div[3]/table/tbody/tr[{row}]/td[{col}]').text)
#     li.append(line)
#     print(line)
#     row+=1
#     cnt+=1
# #혹은 빈칸 때문에 오류 나니까 try-except 문 써야함

#네이버 증권 css
import requests
from bs4 import BeautifulSoup

html = requests.get("https://finance.naver.com/sise/lastsearch2.naver")
soup=BeautifulSoup(html.text,'html.parser')
rank_list=[]; name_list=[]; now_list=[]; updown_list=[]; PER_list=[]
try:
    for ranks in soup.select("#contentarea > div.box_type_l > table > tr td.no"):
        rank_list.append(ranks.text)
    for names in soup.select("#contentarea > div.box_type_l > table >  tr > td:nth-child(2) > a"):
         name_list.append(names.text)
    for nows in soup.select("#contentarea > div.box_type_l > table > tr > td:nth-child(4)"):
        now_list.append(nows.text.strip())
    for updowns in soup.select("#contentarea > div.box_type_l > table > tr > td:nth-child(6)"):
        updown_list.append(updowns.text.strip())
    for PERs in soup.select("#contentarea > div.box_type_l > table >  tr > td:nth-child(11)"):
        PER_list.append(PERs.text.strip())
except:
    pass
for i in range(0,30):
     print('순위:', rank_list[i])
     print('이름:', name_list[i])
     print('현재가:',now_list[i])
     print('등락률:',updown_list[i])
     print('PER:',PER_list[i])
