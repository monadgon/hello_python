# Site: http://www.sqlines.com/online
# ID: #source_type, set value = 'Oracle'
# ID: #target_type, set value = 'PostgreSQL'
# source textarea ID: #frame_source ... #textarea
# convert button: #convert_button
# target textarea ID: #frame_target ... #textarea

# 구현 참조 URL: https://www.geeksforgeeks.org/how-to-select-a-drop-down-menu-value-using-selenium-in-python/
import time 
from selenium import webdriver
from bs4 import BeautifulSoup
# Import Select class 
from selenium.webdriver.support.ui import Select 

driver = webdriver.Chrome(executable_path='C:/tools/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
driver.get('http://www.sqlines.com/online')
source_type = driver.find_element_by_id('source_type')
source_select = Select(source_type)
source_select.select_by_value('Oracle')

target_type = driver.find_element_by_id('target_type')
target_select = Select(target_type)
target_select.select_by_value('PostgreSQL')

time.sleep(1)


#driver.close()