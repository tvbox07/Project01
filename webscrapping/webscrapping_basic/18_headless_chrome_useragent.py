from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium import *

#장치사용안함 지우기
options = webdriver.ChromeOptions()
options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
options.add_argument("window-size=1920x1080") #검색창 크기 설정
# headlesschrome 로 나오는 것을 user-agent 설정 바꾸어 Chrome로 나오게 만들기
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)

# browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
# url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=Cj0KCQiA0p2QBhDvARIsAACSOOPXfqdoVyO0lh3e3oIbLAibCjCxPsnRNAs2Mz9oyazkjRjYbBiJK3AaAhq-EALw_wcB&gclsrc=aw.ds"
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
# id = "detected_value"
detected_value = browser.find_element(By.ID, "detected_value")
# detected_value = browser.find_element_by_id("detected_value")

print(detected_value.text)
browser.quit()

