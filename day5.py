# WebDriver는 창과 탭을 구분하지 않음.
# Selenium에서 창 핸들의 고유 식별자를 사용하여 구분하여 사용 가능.
driver.current_window_handle

# 새 창 또는 탭 만들기 및 전환
driver.switch_to.new_window('tab')    # 새 탭 열어 포커스 전환 (탭: 현재 화면에 추가)
driver.switch_to.new_window('window')    # 새 창 열어 포커스 전환 (창: 아예 새 창)

# 현재 창 또는 탭 닫기 (닫은 후에는 반드시 이전 창으로 전환해 작업을 이어가야 함)
driver.close()
driver.switch_to.window(original_window)