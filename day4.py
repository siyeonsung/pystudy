'''
element = driver.find_element(By.XPATH,"//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3")
driver.execute_script("arguments[0].innerText = '반갑습니다';", element)

# 아이프레임을 대상으로 드라이버 전환하여 상호작용
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
driver.switch_to.frame(iframe) #안 하면 오류남
driver.find_element(By.TAG_NAME, 'button').click()

# 이름 또는 ID를 사용하여 전환
driver.switch_to.frame('buttonframe')

# 인덱스를 사용하여 전환
iframe = driver.find_elements(By.TAG_NAME,'iframe')[1]
driver.switch_to.frame(iframe)

# iFrame 나가 기본 콘텐츠로 돌아가기
driver.switch_to.default_content()
'''