# -*- coding: utf-8-sig -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import csv
from bs4 import BeautifulSoup
import numpy as np
import os
from datetime import datetime

def create_list01(number):
    options = webdriver.ChromeOptions()
    # options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
    # options.add_argument("window-size=1920x1080") #검색창 크기 설정
    # headlesschrome 로 나오는 것을 user-agent 설정 바꾸어 Chrome로 나오게 만들기
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)
    browser = webdriver.Chrome( options=options)


    # https://finance.naver.com/sise/sise_market_sum.naver?&page=1
    # https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page=1  # 코스피 36페이지
    # https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page=1   #코스닥 32페이지
    url = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page={}".format(number) # 코스피
    # url = "https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page={}".format(number) # 코스닥
    header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

    browser.get(url)

    # 1번째 데이터 불러오기    

    browser.find_element(By.ID, "option2").click()
    browser.find_element(By.ID, "option7").click()
    browser.find_element(By.ID, "option8").click()
    browser.find_element(By.ID, "option13").click()
    browser.find_element(By.ID, "option19").click()
    browser.find_element(By.ID, "option4").click()
    browser.find_element(By.ID, "option6").click()
    browser.find_element(By.ID, "option12").click()
    browser.find_element(By.ID, "option15").click()
    browser.find_element(By.ID, "option21").click()
  
    xpath_submit = "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/form/div/div/div/a[1]"
    browser.find_element(By.XPATH, xpath_submit).click()

    alldata = []
    title01 = []
    alldata01 = []

    if number==1:
        ths = browser.find_element(By.CLASS_NAME, "type_2").find_elements(By.CSS_SELECTOR, "th")
        for i in ths:
            title01.append(i.text)
        alldata01.append(title01)
    else:
        pass

    trs = browser.find_element(By.CLASS_NAME, "type_2").find_element(By.CSS_SELECTOR, "tbody").find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        if len(columns) <= 1:
            continue
        data = [column.text.strip() for column in columns]
        # print(data)
        alldata01.append(list(data))

    for i in range(len(alldata01)):
        del alldata01[i][12]
    # print("alldata01 : ", alldata01) 
        
    # 2번째 데이터 불러오기    
    # # 1~6 체크박스 해제
    # for i in range(1, 7):
    #     option = "option" + str(i)
    #     browser.find_element(By.ID, option).click()

    # # 7~12 체크박스 체크
    # for i in range(7, 13):
    #     option = "option" + str(i)
    #     browser.find_element(By.ID, option).click()
    browser.find_element(By.ID, "option1").click()
    browser.find_element(By.ID, "option2").click()
    browser.find_element(By.ID, "option7").click()
    browser.find_element(By.ID, "option8").click()
    browser.find_element(By.ID, "option13").click()
    browser.find_element(By.ID, "option19").click()

    browser.find_element(By.ID, "option14").click()
    browser.find_element(By.ID, "option20").click()
    browser.find_element(By.ID, "option3").click()
    browser.find_element(By.ID, "option9").click()
    browser.find_element(By.ID, "option15").click()
    browser.find_element(By.ID, "option21").click()

    # 적용하기버튼 클릭
    xpath_submit = "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/form/div/div/div/a[1]"
    browser.find_element(By.XPATH, xpath_submit).click()

    title02 = []
    alldata02 = []
    if number==1:
        ths = browser.find_element(By.CLASS_NAME, "type_2").find_elements(By.CSS_SELECTOR, "th")
        for i in ths:
            title02.append(i.text)
        alldata02.append(title02)
    else:
        pass

    trs = browser.find_element(By.CLASS_NAME, "type_2").find_element(By.CSS_SELECTOR, "tbody").find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        if len(columns) <= 1:
            continue
        data = [column.text.strip() for column in columns]
        # print(data)
        alldata02.append(data)
    for i in range(len(alldata02)):
        del alldata02[i][-1]
        del alldata02[i][0:6]

    alldata = list(map(list.__add__, alldata01,alldata02))
    # print("alldata : ", alldata) 


   # 3번째 데이터 불러오기    
    browser.find_element(By.ID, "option14").click()
    browser.find_element(By.ID, "option20").click()
    browser.find_element(By.ID, "option3").click()
    browser.find_element(By.ID, "option9").click()
    browser.find_element(By.ID, "option15").click()
    browser.find_element(By.ID, "option21").click()

    browser.find_element(By.ID, "option4").click()
    browser.find_element(By.ID, "option5").click()
    browser.find_element(By.ID, "option10").click()
    browser.find_element(By.ID, "option16").click()
    browser.find_element(By.ID, "option22").click()
    browser.find_element(By.ID, "option25").click()

    # 적용하기버튼 클릭
    xpath_submit = "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/form/div/div/div/a[1]"
    browser.find_element(By.XPATH, xpath_submit).click()

    title03 = []
    alldata03 = []
    if number==1:
        ths = browser.find_element(By.CLASS_NAME, "type_2").find_elements(By.CSS_SELECTOR, "th")
        for i in ths:
            title03.append(i.text)
        alldata03.append(title03)
    else:
        pass

    trs = browser.find_element(By.CLASS_NAME, "type_2").find_element(By.CSS_SELECTOR, "tbody").find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        if len(columns) <= 1:
            continue
        data = [column.text.strip() for column in columns]
        # print(data)
        alldata03.append(data)
    for i in range(len(alldata03)):
        del alldata03[i][-1]
        del alldata03[i][0:6]

    alldata = list(map(list.__add__, alldata,alldata03))
    # print("alldata : ", alldata)

    # 4번째 데이터 불러오기    
    browser.find_element(By.ID, "option4").click()
    browser.find_element(By.ID, "option5").click()
    browser.find_element(By.ID, "option10").click()
    browser.find_element(By.ID, "option16").click()
    browser.find_element(By.ID, "option22").click()
    browser.find_element(By.ID, "option25").click()

    browser.find_element(By.ID, "option11").click()
    browser.find_element(By.ID, "option17").click()
    browser.find_element(By.ID, "option23").click()
    browser.find_element(By.ID, "option26").click()
    browser.find_element(By.ID, "option6").click()
    browser.find_element(By.ID, "option12").click()

    # 적용하기버튼 클릭
    xpath_submit = "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/form/div/div/div/a[1]"
    browser.find_element(By.XPATH, xpath_submit).click()

    title04 = []
    alldata04 = []

    if number==1:
        ths = browser.find_element(By.CLASS_NAME, "type_2").find_elements(By.CSS_SELECTOR, "th")
        for i in ths:
            title04.append(i.text)
        alldata04.append(title04)
    else:
        pass

    trs = browser.find_element(By.CLASS_NAME, "type_2").find_element(By.CSS_SELECTOR, "tbody").find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        if len(columns) <= 1:
            continue
        data = [column.text.strip() for column in columns]
        # print(data)
        alldata04.append(data)
    for i in range(len(alldata04)):
        del alldata04[i][-1]
        del alldata04[i][0:6]

    alldata = list(map(list.__add__, alldata,alldata04))
    # print("alldata : ", alldata)

    # 5번째 데이터 불러오기    
    browser.find_element(By.ID, "option11").click()
    browser.find_element(By.ID, "option17").click()
    browser.find_element(By.ID, "option23").click()
    browser.find_element(By.ID, "option26").click()
    browser.find_element(By.ID, "option6").click()
    browser.find_element(By.ID, "option12").click()

    browser.find_element(By.ID, "option18").click()
    browser.find_element(By.ID, "option24").click()
    browser.find_element(By.ID, "option27").click()

    # 적용하기버튼 클릭
    xpath_submit = "/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/form/div/div/div/a[1]"
    browser.find_element(By.XPATH, xpath_submit).click()

    title05 = []
    alldata05 = []
    if number==1:
        ths = browser.find_element(By.CLASS_NAME, "type_2").find_elements(By.CSS_SELECTOR, "th")
        for i in ths:
            title05.append(i.text)
        alldata05.append(title05)
    else:
        pass

    trs = browser.find_element(By.CLASS_NAME, "type_2").find_element(By.CSS_SELECTOR, "tbody").find_elements(By.CSS_SELECTOR, "tr")
    for row in trs:
        columns = row.find_elements(By.CSS_SELECTOR, "td")
        # link = row.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        if len(columns) <= 1:
            continue
        data = [column.text.strip() for column in columns]
        # print(data)
        # data.append(link)
        alldata05.append(data)
    for i in range(len(alldata05)):
        del alldata05[i][-1]
        del alldata05[i][0:6]

        # link = "/html/body/div[3]/div[2]/div[2]/div[3]/table[1]/tbody/tr[2]/td[10]/a"
        # path = browser.find_element(By.TAG_NAME, link).text
        # print(path)

    alldata = list(map(list.__add__, alldata,alldata05))
    print("alldata : ", alldata)

    return alldata

    # while(True):
    #     pass


if __name__ == "__main__":

    # 현재 작업 디렉토리를 작업디레토리로 변경
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())
    date = datetime.now().strftime("%Y%m%d")
    filename = "./{}네이버시가총액_코스피.csv".format(date) #코스피

    # filename = "./{}네이버시가총액_코스닥.csv".format(date) #코스닥
    f = open(filename, "w", encoding="utf-8-sig", newline="")
    # f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page=1  # 코스피 36페이지
    # https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page=1   #코스닥 32페이지
    for i in range(36):  # 코스피 36페이지
    # for i in range(32):  # 코스닥 32페이지
    # for i in range(2):  # test 2페이지만
        number = i+1
        alldata = create_list01(number)
        for i in alldata:
            print(i)
            writer.writerow(i)
    
    f.close()

    