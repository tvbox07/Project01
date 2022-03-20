import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def url_xpath_value(url, xpathselector):
    # set_chrome_driver()
    #장치사용안함 지우기
    options = webdriver.ChromeOptions()
    # options.headless = True  # 크롬을 띄우지 않고 서버에서 실행할 경우
    # options.add_argument("window-size=1920x1080") #검색창 크기 설정
    # headlesschrome 로 나오는 것을 user-agent 설정 바꾸어 Chrome로 나오게 만들기
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # browser = webdriver.Chrome("D:\Coding\PythonWorkspace02\chromedriver.exe", options=options)
    browser = webdriver.Chrome( options=options)

    browser = browser.get(url)
    value = browser.find_element(By.XPATH, xpathselector)
    print("in function : " , value)
    # browser.maximize_window()
    # browser.quit()
    return value

def create_xpath(url, xpathselector):
    # try:
    #     # Python 2
    #     from urllib2 import urlopen
    # except ImportError:
    from urllib.request import urlopen
    from lxml import etree

    res = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(res, htmlparser)
    value = tree.xpath(xpathselector)
    print("value : ", value)
    return value

def create_stock_list():
    stock_list = []
    return stock_list

def calulate_srim():
    #금리 조회 : 한국신용평가
    url = "https://www.kisrating.com/ratingsStatistics/statics_spread.do"
    # xpathselector = '//*[@id="con_tab1"]/div[2]/table/tbody/tr[11]/td[9]'
    xpathselector = '/html/body/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[9]'
    # /html/body/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[9]
    # interest_rate = create_xpath(url, xpathselector)
    interest_rate = url_xpath_value(url, xpathselector)
    print("채권 금리(BBB- 5년) : ", interest_rate)

    # url = "https://finance.naver.com/item/coinfo.naver?code=005930"
    stock_no = '005930'
    url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={}".format(stock_no)
    soup = create_soup(url)

    # //*[@id="QmZIZ20rMn"]/table[2]/tbody/tr[11]/td[4]/span
    # xpathselector = '//*[@id="aFVlanREZS"]/table[2]/tbody/tr[11]/td[4]/span'
    xpathselector = "/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[11]/td[4]/span"
    owner_capital = url_xpath_value(url, xpathselector)
    # owner_capital = soup.find
    print("자기자본총계(지배) : ", owner_capital)

    # xpathselector1 = '//*[@id="aFVlanREZS"]/table[2]/tbody/tr[22]/td[4]/span'
    xpathselector1 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[4]/span'
    roe1 = url_xpath_value(url, xpathselector1)
    # xpathselector2 = '//*[@id="aFVlanREZS"]/table[2]/tbody/tr[22]/td[3]/span'
    xpathselector2 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[3]/span'

    roe2 = url_xpath_value(url, xpathselector2) 
    # xpathselector3 = '//*[@id="aFVlanREZS"]/table[2]/tbody/tr[22]/td[2]/span'
    xpathselector3 = '/html/body/div/form/div[1]/div/div[2]/div[3]/div/div/div[14]/table[2]/tbody/tr[22]/td[2]/span'

    roe3 = url_xpath_value(url, xpathselector3)
    roe_3yr = ((roe1*3)+(roe2*2)+(roe3))/6
    print("ROE : ")

    xpathselector = '//*[@id="tab_con1"]/div[1]/table/tbody/tr[3]/td/em'
    stock_number = url_xpath_value(url, xpathselector)
    print("상장주식수 : ", stock_number)

    stock_value_price = (owner_capital+(owner_capital*(roe_3yr-interest_rate)/interest_rate))/stock_number
    print("적정주가 : ", stock_value_price)
    

    while(True):
        pass

if __name__ == "__main__":
    # 1. 주식번호리스트 만들기
    # 2. S_Rim 계산(주당 적정주가 계산)
    # 3. 적정주가와 현재가의 차이가 높은 주식 고르기

    # create_stock_list()  # 1. 주식번호리스트 만들기
    calulate_srim()   # 2. S_Rim 계산(주당 적정주가 계산)
    
    

    # 3. 1년 전 적정주가-년말 주가 차이
    # 4. 현재 적정주가-현재주가 차이
    # 5. 3번과 4번의 변동폭을 비교 평가하기



