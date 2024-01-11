from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import re

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def wait():
    driver.implicitly_wait(8)


def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh").click()
    driver.implicitly_wait(3)


def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 본문 내용
    try:
        content = soup.select('div._a9zs')[0].text
    except:
        content = ''
    # 해시태그
    tags = re.findall(r'#[^\s#,\\]+', content)

    data = [content, tags]

    return data

# ID, PW, 검색어, 검색할 개수
id = ''
pw = ''
find = '충무로역'
target = 10

# 로그인 부분
driver = webdriver.Chrome(options=chrome_options)
driver.get(f"https://www.instagram.com/explore/tags/{find}")

wait()
enter = driver.find_element(By.CSS_SELECTOR,'._aagw').click()
wait()
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(id)
driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(pw)
wait()
driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(Keys.ENTER)
wait()
# 로그인 정보 저장 물음
driver.find_element(By.CSS_SELECTOR, 'div._ac8f').click()
wait()

# 첫 번째 사진 클릭
enter = driver.find_element(By.CSS_SELECTOR, '._aagw').click()
wait()

results = []
# target 가지의 게시물의 태그 추출
for i in range(target):
    data = get_content(driver)
    results.append(data)
    move_next(driver)
    
# 태그 출력    
print(results)
