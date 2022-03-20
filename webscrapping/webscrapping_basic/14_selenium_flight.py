from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)
# browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"

browser.get(url)

#도착지 선택 제주
# browser.find_element_by_class_name("select_code__d6PLz").click()
# browser.find_element_by_class_name("autocomplete_Collapse__tP3pM").click()
# browser.find_element_by_link_text("CJU").click()


# 가는 날 선택 클릭
# elem = browser.find_element_by_class_name("tabContent_option__2y4c6 select_Date__1aF7Y")
# elem = browser.find_elements_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
# print("text : ",elem[0])
# elem[0].click()

# sdayselector = (By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
# elem = browser.find_element(sdayselector)
elem = browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
# elem = browser.find_element(By.LINK_TEXT, "가는 날")
# elem = browser.find_element(By.PARTIAL_LINK_TEXT, "가는 날")
elem.click()
print(elem.text)


time.sleep(2)

# 이번달 27일, 28일 선택
depatureday = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button'
elem = browser.find_element_by_xpath(depatureday)
elem.click()
ariveday = '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button'
elem = browser.find_element_by_xpath(ariveday)
elem.click()

#제주도 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()

#항공권 검색 버튼 클릭
flightsearch ='//*[@id="__next"]/div/div[1]/div[4]/div/div/button'
elem = browser.find_element_by_xpath(flightsearch)
elem.click()

# try:
#     #튜플형태 안됨
#     elem = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[1]')))
#     # time.sleep(15)
#     #성공했을때 출력
#     elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[1]')
#     print(elem.text)
#     pass
# finally:
#     browser.back()

# time.sleep(20)
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')
# print(elem.text)
time.sleep(20)
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div')
print(elem.text)


# print(elem.text)
# sday = (By.LINK_TEXT, "27")
# elem = browser.find_elements(sday)[0]
# elem = browser.find_elements(By.LINK_TEXT, "27")

# 이번달 선택
# elem = browser.find_elements(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button/b")[0]
# print(elem.text)
# elem.click()
# elem = browser.find_elements(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b")[0]
# print(elem.text)
# elem.click()

#이번달 27일 다음달 28일
# elem = browser.find_elements(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button/b")[0]
# print(elem.text)
# elem.click()
# elem = browser.find_elements(By.XPATH, "//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button/b")[0]
# print(elem.text)
# elem.click()

# elem = browser.find_elements(By.PARTIAL_LINK_TEXT, "27")  # 안됨
# element01 = "<button class='sc-crzoAE hnpClg inner'><b class='sc-dIsUp jEEywD num'>27</b><i class='sc-bqGGPW iPexDg txt'></i></button>"
# elem = ActionChains(browser).click(element01).perform()
# print("link text :  ", elem)
# elem.click()
# browser.find_elements_by_link_text('27')[0].click() # 이번달 선택
# browser.find_elements_by_link_text("28")[0].click()  # 이번달 선택

while(True):
    pass