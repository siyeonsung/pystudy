from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from selenium.webdriver import ActionChains # 일련의 작업들을(ex.아이디 입력, 비밀번호 입력, 로그인 버튼 클릭...) 연속적으로 실행할 수 있게 하기 위해
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.support.ui import WebDriverWait # 브라우저의 응답을 기다릴 수 있게 하기 위해
from selenium.webdriver.support import expected_conditions as EC # html요소의 상태를 체크할 수 있게 하기 위해
# 이 외에도 필요한 모듈이 있다면 따로 호출해준다.
import time

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome() #크롬 열기
driver.get('http://capszzang.gq/') # 해당 웹사이트로 접속
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[6]/a').click() #로그인 창 클릭
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('test1234') #아이디 입력
driver.find_element(By.XPATH, '//*[@id="password"]').ㅅsend_keys('12345678') #패스워드 입력
driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div/form/div[3]/button').click()  # 로그인 버튼 클릭
time.sleep(5)
try: #예외처리
    result = driver.switch_to.alert #alert창으로 전환
    result.accept() #alert 확인 버튼 클릭
except:
    pass
time.sleep(2)
nickname = driver.find_element(By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[6]/a').text #닉네임 정보 알아오기
print(nickname)
search=input('검색어 입력: ')
driver.get('http://capszzang.gq/wiki/')
infile=open('결과값.txt','w',encoding='UTF-8')
driver.find_element(By.XPATH, "//*[@id='search']").send_keys(search)
driver.find_element(By.XPATH, "//*[@id='search']").send_keys(Keys.ENTER)
wiki=driver.find_element(By.XPATH, '/html/body/section[3]/div').text #wiki가 리스트..?라서 .text 안 되는 줄 알았는데 됨 왜지
for wikis in wiki:
    infile.write(wikis)
infile.close()
# #캡스 집행부원 출력
driver.get('http://capszzang.gq/about/executive/')
time.sleep(1)
name=driver.find_elements(By.XPATH, '/html/body/section[2]/div/ul/li/a[2]')
#리스트니까 .text가 안 됨 프린트할 때 써야함
for names in name:
    print(names.text)
