# Quiz) 부동산 매물() 정보를 스크래핑 하는 프로그램을 만드시오
# [조회 조건]
# 1. http://daum.net 접속
# 2. "" 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# =========== 매물 1 ==========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000(만원)
# 동 : 214동
# 층 : 고/23

# =========== 매물 2 ============
# ....

# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(
    "D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)

# browser = webdriver.Chrome()
browser.maximize_window()

url = "http://daum.net"
browser.get(url)
search_word = "보문 아이파크 아파트"
browser.find_element(By.CLASS_NAME, "tf_keyword").send_keys(
    [search_word, Keys.ENTER])
# browser.find_element(By.CLASS_NAME, "ico_pctop btn_search").send_keys(Keys.ENTER)
soup = BeautifulSoup(browser.page_source, "lxml")
data_rows = soup.find("div", attrs={"class": "wrap_basicinfo"})
# print(info)
with open("quiz.html", "w", encoding="utf-8") as f:
    f.write(data_rows.prettify())
# get all tags

data01 = data_rows.find("div", attrs={"class":"info_place clear type_longtit4"}).find_all("dl")
# print(data01)

for index, row in enumerate(data01):
    columns01 = row.find_all(["dt"])
    columns02 = row.find_all(["dd"])
    try:
        print((index+1))
        print(columns01[0].get_text())
        print(columns02[0].get_text())
    except Exception as e:
        pass
    # print(f"="*10," 매물 {index} ", "="*10)
    # print(columns[0], " ", columns[1])

# tags = {tag.name for tag in data_rows.find_all()}
# print(tags)
  
# # breakpoint()

# # class list set
# class_list = set()

# class_dict = {}
# # print(type(class_dict))
# count = 0
# # iterate all tags
# for tag in tags:
#     # count += 1
#     # print(count, " : ", tag)

#     # find all element of tag
#     for i in data_rows.find_all(tag):
#         # print(count, " : ", i)
#         # if tag has attribute of class
#         if i.has_attr("class"):
#             # print(count, " : ", i)
#             if len( i['class'] ) != 0:
#                 # count += 1
#                 # print(count, " : ", i['class'])
#                 class_list.add(" ".join( i['class']))
            
#                 class_key = i['class'][0]
#                 # print(class_key)
#                 class_val = browser.find_element(By.CLASS_NAME, class_key).text
#                 # print(class_val)
#                 add_dict = {class_key: class_val}
#                 class_dict.update(add_dict)

# print(class_list)
# # for i in class_list:
# #     print(class_list[i])
# # class_val = set()

# # for i in class_list:
# #     print(i)
# #     info = browser.find_element(By.CLASS_NAME, str(i)).get_text()
# #     class_val.add(" ".join(info ))

# # print(class_val)

# # print(class_dict)

while(True):
    pass
