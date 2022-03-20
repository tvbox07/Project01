
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import chromedriver_autoinstaller as AutoChrome
import sys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# import shutil

# #chrome://version
# #chromedriver를 download 버전이 일치해야함.

# browser.get("http://daum.net")
# browser = webdriver.chrome("./chromedriver.exe") # "./chromedriver.exe"

# 시스템에 부착된 장치가 작동하지 않습니다. (0x1F) 에러를 없애기 위한 옵션 지성
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# DeprecationWarning: executable_path has been deprecated 해결방법
# def set_chrome_driver():
#     chrome_options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     return driver

# browser = set_chrome_driver().get("https://naver.com")

# sys.exit()

#webdriver 경로 찾기
chrome_ver = AutoChrome.get_chrome_version().split('.')[0]
print(str(chrome_ver))

# path =  os.path.join(os.getcwd())
path =  os.path.join(os.getcwd(), chrome_ver)
path = os.path.join(path,'chromedriver.exe')
print(path)

# 프로그램 중간에 종료
# sys.exit()

URL = 'https://naver.com'

# browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)
browser = webdriver.Chrome(str(path), options=options)
# 1. 네이버 이동
# browser.get("http://naver.com")
browser.get(url=URL)


# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# browser.implicitly_wait(10) 
while(True):
    pass


