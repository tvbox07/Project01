from selenium import webdriver
import time

# browser = webdriver.Chorme()
# 시스템에 부착된 장치가 작동하지 않습니다. (0x1F) 에러를 없애기 위한 옵션 지성
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)

# 1. 네이버로 이동

browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3 id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()


# time.sleep(3)
# 5. 아이디 새로 입력
browser.find_element_by_id("id").clear() #기존 쓴 아이디를 지움
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.close() # 현재 탭만 종료
# browser.quit() # 전체 브라우저 종료



# 브라우저 닫힘을 방지 ctrl+c로 닫음
while(True):
    pass
