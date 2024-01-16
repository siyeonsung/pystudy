from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://everytime.kr")
original_window=driver.current_window_handle

time.sleep(3)

driver.switch_to.new_window('tab')
driver.get('https://mdrims.dongguk.edu/')
time.sleep(2)
driver.switch_to.window(original_window)
time.sleep(2)

driver.close()