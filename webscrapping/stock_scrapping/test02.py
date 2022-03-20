

# # import numpy as np
# # title01 = [1,2,3]
# # title02 = [4,5,6]
# # title03 = [13,24,25]

# # alldata =[]

# # alldata.append(title01)

# # del title02[0:2]
# # # print(title02)?alldata.append(title02)


# # # alldata = [title01, title02, title03]
# # # print(alldata)

# # title02 = [[7,8,9],[10,11,12]]
# # del title02[1][0]
# # print(title02)

# # # alldata = title01+title02

# # # title01 = list(map(list.__add__, title01, title02))
# # # print(alldata)

# # # for i in range(1, 7):
# # #     option = "option"+str(i)
# # #     print(option)

# # for i in range(36):
# #     number = i+1
# #     print(number)

# from selenium import webdriver
# from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
# # options.add_argument("window-size=1920x1080") #검색창 크기 설정
# # headlesschrome 로 나오는 것을 user-agent 설정 바꾸어 Chrome로 나오게 만들기
# options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# # browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)
# browser = webdriver.Chrome( options=options)


# # https://finance.naver.com/sise/sise_market_sum.naver?&page=1
# number = 1
# url = "https://finance.naver.com/sise/sise_market_sum.naver?&page={}".format(number)
# header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

# browser.get(url)
# #contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td.center > a
# # /html/body/div[3]/div[2]/div[2]/div[3]/table[1]/tbody/tr[2]/td[10]
# # /html/body/div[3]/div[2]/div[2]/div[3]/table[1]/tbody/tr[2]/td[10]/a
# # link = "/html/body/div[3]/div[2]/div[2]/div[3]/table[1]/tbody/tr[2]/td[10]"
# path = browser.find_element(By.CLASS_NAME, "type_2").find_element(By.CSS_SELECTOR, "tbody").find_element(By.CSS_SELECTOR, "a")
# print(path.get_attribute("href"))
# # print(path.get_property())

import time
from datetime import datetime
number = 2
if number==1:
    print("a")
else:
    pass

print("pass")
print(time.time())
print(datetime.now().strftime("%Y%m%d"))