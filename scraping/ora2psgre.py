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
import os

# read all source files --> overwrite all source files with the converted result
i = 0
for (path, dir, files) in os.walk("D:\\pjt_plm\\db_migration_to_pg\\sql\\postgre_NEADAM\\dml"):
    for filename in files:
        driver = webdriver.Chrome(executable_path='C:/tools/chromedriver_win32/chromedriver.exe')
        driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
        driver.get('http://www.sqlines.com/online')
        source_type = driver.find_element_by_id('source_type')
        source_select = Select(source_type)
        source_select.select_by_value('Oracle')

        target_type = driver.find_element_by_id('target_type')
        target_select = Select(target_type)
        target_select.select_by_value('PostgreSQL')

        driver.maximize_window()
        #driver.minimize_window()

        time.sleep(2)

        ext = os.path.splitext(filename)[-1]
        if ext == '.sql':
            fullpath = "%s/%s" %(path, filename)
            n = os.path.getsize(fullpath)
            if n > 500000: # bytes
                driver.close()
                continue
            else:
                f = open(fullpath, 'r', encoding='UTF-8')
                #print('fullpath:', fullpath)
                data = f.read()
                #print('data:', data)
                f.close()
                # source textarea ID: #frame_source ... #textarea
                frame_source = driver.switch_to.frame('frame_source') # ex) iframe = driver.find_element_by_xpath("//iframe[@name='Dialogue Window']")
                source_textarea = driver.find_element_by_id('textarea')
                source_textarea.clear()
                source_textarea.send_keys(data)

                # convert button: #convert_button
                driver.switch_to.parent_frame()
                button = driver.find_element_by_id('convert_button')
                button.click()

                time.sleep(8)

                # target textarea ID: #frame_target ... #textarea
                driver.switch_to.frame('frame_target')
                target_textarea = driver.find_element_by_id('textarea')
                result = target_textarea.get_attribute('value')
                result = result.replace('                ', '    ').replace('            ', '    ').replace('        ', '    ')
                #print('result:', result)
                fw = open(fullpath + ".pg", 'w', encoding='UTF-8')
                fw.write(result)
                fw.close()
                target_textarea.clear()

                driver.switch_to.parent_frame()

                i += 1
                print(i)

                time.sleep(2)
                driver.close()