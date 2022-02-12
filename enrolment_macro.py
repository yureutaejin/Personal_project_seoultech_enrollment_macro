# Library

from selenium import webdriver
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import time

sched = BlockingScheduler()


def click_by_id(id):
    driver.find_element_by_id(id).click()

#수강신청 로그인

url = 'https://for-s.seoultech.ac.kr/view/login.jsp'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
driver = webdriver.Chrome('/Users/jinyuntae/Desktop/development_tool/chromedriver', options=options)
driver.get(url)

# 수강신청 로그인

url = 'https://for-s.seoultech.ac.kr/view/login.jsp'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
driver = webdriver.Chrome('/Users/jinyuntae/Desktop/development_tool/chromedriver', options=options)
driver.get(url)

driver.find_element_by_name('USER_NUMB').send_keys('19102026')
driver.find_element_by_name('PWD').send_keys('sgouk5460!')
click_by_id('btn_Login')

# OCR 이용 자동 캡차 뚫기 - 미완성
# captcha_num = ""

# captcha_png = driver.find_element_by_id("img_captcha").screenshot_as_png
# with open('captcha_repository/captcha.png', 'wb') as file:
#     file.write(captcha_png)

# captcha_num = pytesseract.image_to_string(Image.open('captcha_repository/captcha.png'))
# print(captcha_num)

direct_input_captcha = input("captcha num? ")
driver.find_element_by_id("CAPTCHA").send_keys(direct_input_captcha)

driver.find_element_by_class_name("btn-layerClose").click()

driver.find_element_by_xpath('//*[@id="header"]/table/tbody/tr[2]/td/div[2]/ul/li[3]/a').click()

# 장바구니 클릭
click_by_id('jqg_grd_basket_1')

table = driver.find_element_by_id("grd_basket")

# # 1. 예약 저장
# sched.add_job(click_by_id, 'date', run_date=datetime(2022, 2, 9, 10, 0, 2, 0), args=['btn_basketSave'])
# sched.start()

# 2. 무한 로드 저장
tbody = table.find_element_by_tag_name("tbody")
tr = tbody.find_elements_by_tag_name("tr")

empty_person = False

tr_len = len(tr)
while empty_person != True:
    driver.get(driver.current_url)
    if tr_len != len(tr):
        break
    click_by_id('jqg_grd_basket_1')
    temp_list = tr[1].text.split()

    if temp_list[9] != 0:
        click_by_id(['btn_basketSave'])
        time.sleep(5)
