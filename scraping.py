from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import shutil

# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
driver.get('https://quotefancy.com/quote/792409/Deepak-Chopra-The-more-boundless-your-vision-the-more-real-you-are')
html = driver.page_source
#soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
soup = BeautifulSoup(html, 'lxml') # BeautifulSoup사용하기
links = soup.select('.dl-wrapper > a[href]') # dl-wrapper 클래스 하위에 있는 a 테그 중 href 속성을 가지고 있는 요소
for link in links:
    #print(link['href'])
    img_url = link['href'] # link의 href 속성 값을 추출
    file_name = img_url.split("/")[-1]
    file_name = "D:/YOU/Deepak Chopra/themoreboundless/" + file_name
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            print('Image successfully downloaded: ', file_name)
    else:
        print('Image could not be retrived.')
driver.close()
