from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By

#주식 재무

#장치사용안함 지우기
options = webdriver.ChromeOptions()
# options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome( options=options)

    #금리 조회 : 한국신용평가
url = "https://www.kisrating.com/ratingsStatistics/statics_spread.do"
browser.get(url)
# xpathselector = '//*[@id="con_tab1"]/div[2]/table/tbody/tr[11]/td[9]'
xpathselector = '/html/body/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[9]'
# interest_rate = float(browser.find_element(By.XPATH, xpathselector).text)
interest_rate = 9.09
print("채권 금리(BBB- 5년) : ", interest_rate)

# url = "https://finance.naver.com/item/coinfo.naver?code=005930"
# stock_no_list = ['373220', '404990', '396690', '402340', '400760', '377300', '381970', '329180', '395400', '271940']
# stock_no = stock_no_list[1]
stock_no = "001740"
# interest_rate = interest_rate
url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={}".format(stock_no)
print("url : : ", url)
browser.get(url)

# 컴퍼니네임
try:
    xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[1]/div/table/tbody/tr[1]/td/dl/dt[1]/span"
    com_name = browser.find_element(By.XPATH, xpathselector).text
    print("회사명 : ", com_name)
except:
    print("회사명 : ", com_name)

# 자기자본총계(지배)
try:
    # xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[11]/td[3]/span"
    xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[11]/td[3]/span"
    owner_capital = browser.find_element(By.XPATH, xpathselector).text.replace(",","")
    owner_capital = float(owner_capital)*100000000
# print("자기자본총계(지배) : ", owner_capital)
except:
    print("check 자기자본총계")

# ROE 가중평균
try:
    xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[3]/span'
    # xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[4]/span'
    roe1 = browser.find_element(By.XPATH, xpathselector1).text
    print("roe1 : ", roe1)
except:
    roe1 = 0

try:
    xpathselector2 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[2]/span'
    roe2 = browser.find_element(By.XPATH, xpathselector2).text
except:
    roe2 = 0
    print("no value roe2")

try:
    xpathselector3 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[1]/span'
    roe3 = browser.find_element(By.XPATH, xpathselector3).text
except:
    roe3 = 0
    print("no value roe3")


if roe1 != 0 and roe2 != 0 and roe3 != 0:   
    roe_3yr = ((float(roe1)*3)+(float(roe2)*2)+float(roe3))/6
    print("roe_3yr")
else:
    roe_3yr = float(roe1)
    print("roe_3yr = roe1")
# print("ROE3년 가중평균 : ", roe_3yr)

#상장주식수
# url = "https://finance.naver.com/item/main.naver?code={}".format(stock_no)
# browser.get(url)
# xpathselector = '/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/table/tbody/tr[3]/td/em'
xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[7]/td"
stock_count_rate = browser.find_element(By.XPATH, xpathselector).text.replace(",","").split("주")
stock_count = float(stock_count_rate[0])
print("상장주식수 : {:,}".format(stock_count))

#현재 주가
xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/strong"
stock_current_price = browser.find_element(By.XPATH, xpathselector).text.replace(",","")
stock_current_price = float(stock_current_price)
stock_current_price = round(stock_current_price)
print("현재주가 : {:,} ".format(stock_current_price))

# EV/EVITDA 검색
try:
    xpathselector = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[7]/table/tbody/tr[4]/td[1]'
    evevitda = browser.find_element(By.XPATH, xpathselector).text.replace(",","")
    evevitda = float(evevitda)
    print("EV/EVITDA : {} ".format(evevitda))
except:
    evevitda = 0 
    print("EV/EVITDA : {} ".format(evevitda))


#적정주가 계산
stock_value_price = (owner_capital+(owner_capital*(roe_3yr-interest_rate)/interest_rate))/stock_count
print("적정주가 : {:,}".format(round(stock_value_price)))
browser.quit()
# return stock_value_price



