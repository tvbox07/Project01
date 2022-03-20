# from html.parser import HTMLParser
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager    
import time
# import os
import csv

def create_interest_rate():
    #장치사용안함 지우기
    options = webdriver.ChromeOptions()
    options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
    # options.add_argument("window-size=1920x1080") #검색창 크기 설정
    # headlesschrome 로 나오는 것을 user-agent 설정 바꾸어 Chrome로 나오게 만들기
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)
    browser = webdriver.Chrome( options=options)

    #금리 조회 : 한국신용평가
    url = "https://www.kisrating.com/ratingsStatistics/statics_spread.do"
    browser.get(url)
    # xpathselector = '//*[@id="con_tab1"]/div[2]/table/tbody/tr[11]/td[9]'
    xpathselector = '/html/body/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[9]'
    interest_rate = float(browser.find_element(By.XPATH, xpathselector).text)
    print("채권 금리(BBB- 5년) : ", interest_rate)
    browser.quit()

    return interest_rate

    
def create_value_price(stock_no, interest_rate):
    #주식 재무

    #장치사용안함 지우기
    options = webdriver.ChromeOptions()
    options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome( options=options)

    # url = "https://finance.naver.com/item/coinfo.naver?code=005930"
    stock_no = stock_no
    interest_rate = interest_rate
    url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={}".format(stock_no)
    # print("url : : ", url)
    browser.get(url)

    # 자기자본총계(지배)
    try:
        xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[11]/td[3]/span"
        # xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[11]/td[4]/span"
        owner_capital = browser.find_element(By.XPATH, xpathselector).text.replace(",","")
        owner_capital = float(owner_capital)*100000000
        # print("자기자본총계(지배) : {}".format(owner_capital, ','))
    except:
        owner_capital = 0

    # ROE 가중평균
    try:
        # xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[3]/span'
        xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[3]/span'
        roe1 = browser.find_element(By.XPATH, xpathselector1).text.replace(",","")
    except : # print("roe1 : ", roe1)
        roe1 = 0

    try:
        xpathselector2 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[2]/span'
        roe2 = browser.find_element(By.XPATH, xpathselector2).text.replace(",","")
    except:
        roe2 = 0
        # print("no value roe2")

    try:
        xpathselector3 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[1]/span'
        roe3 = browser.find_element(By.XPATH, xpathselector3).text.replace(",","")
    except:
        roe3 = 0
        # print("no value roe3")


    if roe1 != 0 and roe2 != 0 and roe3 != 0:   
        roe_3yr = ((float(roe1)*3)+(float(roe2)*2)+float(roe3))/6
        # print("roe_3yr :", roe_3yr)
    elif roe1 != 0 and roe2 != 0 and roe3 == 0 :   
        roe_3yr = ((float(roe1)*2)+(float(roe2)*1))/3
        # print("roe_2yr :", roe_3yr)
    else:
        roe_3yr = float(roe1)
        # print("roe_1yr :", roe_3yr)
        # print("roe_3yr = roe1 : {}".format(roe1))
    print("ROE3년 가중평균 : {0:,}".format(roe_3yr))

    #상장주식수
    try:
        xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[7]/td"
        stock_count_rate = browser.find_element(By.XPATH, xpathselector).text.replace(",","").split("주")
        stock_count = float(stock_count_rate[0])
        # print("상장주식수 : {} ".format(stock_count,','))
    except:
        stock_count = 1

        #현재 주가
    try:
        xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/strong"
        stock_current_price = browser.find_element(By.XPATH, xpathselector).text.replace(",","")
        stock_current_price = float(stock_current_price)
        # print("현재주가 : {} ".format(stock_current_price))
    except:
        stock_current_price = 1 

    #적정주가 계산
    stock_value_price = (owner_capital+(owner_capital*(roe_3yr-interest_rate)/interest_rate))/stock_count
    # print("적정주가 : {:,}".format(stock_value_price))

    # EV/EVITDA 검색
    try:
        xpathselector = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[7]/table/tbody/tr[4]/td[1]'
        evevitda = browser.find_element(By.XPATH, xpathselector).text.replace(",","")
        evevitda = float(evevitda)
        # print("EV/EVITDA : {} ".format(evevitda))
    except:
        evevitda = 0 

    browser.quit()
    return owner_capital, roe_3yr, stock_count, round(stock_current_price), round(stock_value_price), evevitda, url


if __name__=="__main__":

    interest_rate = create_interest_rate()
    print("interest_rate : ", interest_rate)

    # 현재 작업 디렉토리를 작업디레토리로 변경
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())

    # csv 파일열어 데이터 불러오기
    # D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping
    g = open("D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01.csv", "r", encoding="utf-8-sig")
    reader = csv.reader(g)
    data = list(reader)
    # print("csv length : ", len(data))

    # csv 에 처음부터 자료 저장
    f = open("D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01_result.csv", "w", encoding="utf-8-sig", newline="") #한글이 깨지지 않게 저장하기 utf-8-sig
    # 기존 csv에 추가해서 자료 저장
    # f = open("D:\Coding\PythonWorkspace02\webscrapping\stock_scrapping\stock_list01_result.csv", "a", encoding="utf-8-sig", newline="") #한글이 깨지지 않게 저장하기 utf-8-sig
    writer = csv.writer(f)
    title = "stock_no, com_name, owner_capital, roe_3yr, stock_count, stock_current_price, stock_value_price,expected_rise_percent, evevitda, url".split(",")
    #["N", "종목명", "현재가",....] 리스트 형태로들어감
    # print(type(title))
    writer.writerow(title)

    j = 0
    # for line in data[:5]: #테스트 용 상위 5개만 출력
    for line in data: # 모든 주식 출력
    # for line in data[:4]: # 4번째까지 출력
        stock_no = "{:06d}".format(int(line[1]))
        com_name = "{}".format(line[0])
        # print(data[j])
        j += 1
        print(j, " : ", stock_no, " : ", com_name)  

        owner_capital, roe_3yr, stock_count, stock_current_price, stock_value_price, evevitda, url = create_value_price(stock_no, interest_rate)
        # print("stock_current_price : ", stock_current_price)  
        # print("stock_value_price : " , stock_value_price)  

        # (적정주가 - 현재주가)/ 현재주가 * 100 = 상승여력  
        expected_rise_percent = ((stock_value_price - stock_current_price)/stock_current_price) * 100
        alist = [stock_no, com_name, owner_capital, roe_3yr, stock_count, stock_current_price, stock_value_price,expected_rise_percent, evevitda, url]
        writer.writerow(alist)
        # for line in alist:
        #     writer.writerow(line)
        #     # print(i, " : ", line)
        # time.sleep(1) # 초 쉬었다가 다음 주식 스크롤링
   

    g.close()
    f.close()  
    
    
    # create_stock_no()
    # create_com_value()
    # create_excel_list()

# while(True):
#     pass