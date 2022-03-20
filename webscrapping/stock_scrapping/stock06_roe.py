from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager    
import time
# import os
import csv

    #장치사용안함 지우기
options = webdriver.ChromeOptions()
options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome( options=options)

# url = "https://finance.naver.com/item/coinfo.naver?code=005930"
stock_no = '365900'

url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={}".format(stock_no)
# print("url : : ", url)
browser.get(url)



# ROE 가중평균
try:
    # xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[3]/span'
    xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[3]/span'
    roe1 = browser.find_element(By.XPATH, xpathselector1).text.replace(",","")
    print("roe1 : ", roe1)
except : 
    roe1 = 0

try:
    xpathselector2 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[2]/span'
    roe2 = browser.find_element(By.XPATH, xpathselector2).text.replace(",","")
    print("roe2 : ", roe2)

except:
    roe2 = 0
    print("no value roe2")

try:
    xpathselector3 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[1]/span'
    roe3 = browser.find_element(By.XPATH, xpathselector3).text.replace(",","")
    print("roe3 : ", roe3)

except:
    roe3 = 0
    print("no value roe3")


if roe1 != 0 and roe2 != 0 and roe3 != 0:   
    roe_3yr = ((float(roe1)*3)+(float(roe2)*2)+float(roe3))/6
    print("roe_3yr :", roe_3yr)
elif roe1 != 0 and roe2 != 0 and roe3 == 0 :   
    roe_3yr = ((float(roe1)*2)+(float(roe2)*1))/3
    print("roe_2yr :", roe_3yr)
else:
    roe_3yr = float(roe1)
    print("roe_1yr :", roe_3yr)
    # print("roe_3yr = roe1 : {}".format(roe1))
print("ROE3년 가중평균 : {0:,}".format(roe_3yr))