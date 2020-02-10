# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import datetime, random, time, locale, re, string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

test_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print
print "테스트 시작시간 :", test_start_time
print

driver = webdriver.Chrome('chromedriver')
driver.get('https://www01.dev.kurly.com/shop/main/index.php')
driver.implicitly_wait(3)

driver.maximize_window()

# kurlymall dev01 로그인 하기
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/a').click()
time.sleep(1)
driver.find_element_by_name('m_id').send_keys('qatest01')
driver.find_element_by_name('password').send_keys('wldnsgks1@')
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div/form/button/span').click()
time.sleep(1)

# 오로라생연어 검색
driver.find_element_by_id('sword').clear()
driver.find_element_by_id('sword').send_keys(u'오로라생연어')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[4]/div/div/div[1]/div[1]/form/input[8]').click()

# 상품상세 접근
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/ul/li[1]/div/a/span[1]').click()
time.sleep(5)

# 상품선택
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/div/ul/li[1]/a/span').click()

# 장바구니 담기
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/span/button').click()

# 장바구니 접근
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[4]/div/div/div[1]/div[2]/div[1]/a/img').click()
time.sleep(5)

# 주문하기
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div[3]/button').click()
time.sleep(5)

# 공동현관 출입 방법
driver.find_element_by_xpath('//*[@id="dataDelivery"]/table/tbody/tr[9]/td/label[6]').click()

# 적립금 사용
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[1]/form/div[5]/div/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/label').click()
time.sleep(3)

# 이용동의
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[1]/form/table/tbody/tr/td/div[2]/label').click()

# 결제하기 버튼 입력
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[1]/form/div[8]/input').click()

driver.switch_to.alert.accept()
time.sleep(3)
driver.find_element_by_link_text('주문내역 상세보기').click()

order = driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div[2]/h3').text
code = order[5:18]

print "01. 컬리몰 주문번호 :", (code)

driver.close()

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 10)
driver.get('https://www01.dev.kurly.com/shop/admin/login/login.php')

driver.maximize_window()

# cms dev01 로그인 하기
driver.find_element_by_name('m_id').send_keys('jiun.han@kurlycorp.com')
driver.find_element_by_name('password').send_keys('wldnsgks1!!')
driver.find_element_by_xpath('/html/body/form/div[2]/div/table/tbody/tr/td[2]/input').click()

# 주문 페이지로 이동
driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/ul/li[4]/a/img').click()

# 주문번호 입력
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[1]/table/tbody/tr[1]/td[2]/input').send_keys(code)

# 처리일자 시간 조정
Select(driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[1]/table/tbody/tr[7]/td[2]/select[1]')).select_by_visible_text('00시')

# 주문검색
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[1]/div/input').click()

# 주문 선택 및 상품준비중으로 변경 처리
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[2]/table[2]/tbody/tr[4]/td[1]/input').click()
Select(driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[2]/table[1]/tbody/tr[1]/td[1]/select')).select_by_visible_text('상품준비중 처리')
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[2]/div[2]/a[1]/img').click()

order_state = driver.find_element_by_xpath('//*[@id="frmList"]/table[2]/tbody/tr[4]/td[11]').text
print
print "02. CMS 주문 처리상태 :", (order_state)

order_time1 = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[2]/table[2]/tbody/tr[4]/td[4]/span').text
order_time2 = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td/form[2]/table[2]/tbody/tr[4]/td[3]/span').text
print
print "03. CMS 주문 결제시간 :", (order_time1)

driver.close()

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 10)
driver.get('https://escm01.dev.kurly.com/escm/sign')

driver.maximize_window()

# eSCM dev01 로그인 하기
driver.find_element_by_id('user_id').send_keys('qa_md1@kurlycorp.com')
driver.find_element_by_id('user_pwd').send_keys('kurly123!@#')
driver.find_element_by_class_name('btn-login').click()

# 출고오더관리 이동
driver.find_element_by_link_text('출고오더관리').click()
driver.find_element_by_link_text('[DD01] 컬리 오더생성(DB)').click()

# 컬리몰 주문 전송처리
driver.find_element_by_id('paidStartDate1').send_keys(Keys.DELETE)
driver.find_element_by_name('from_order_date').send_keys(order_time1)
driver.find_element_by_id('paidStartDate2').send_keys(Keys.DELETE)
driver.find_element_by_name('to_order_date').send_keys(order_time1)
driver.find_element_by_id('getGodoOrder').click()
time.sleep(7)
driver.find_element_by_id('modalClose').click()
time.sleep(1)

# 컬리 출고오더 리스트 확인
driver.find_element_by_link_text('[DL01] 컬리 출고오더 리스트').click()
driver.find_element_by_name('order_code').send_keys(code)
driver.find_element_by_id('orderSearch').click()

result = driver.find_element_by_xpath('//*[@id="orderTable"]/tbody/tr/td[4]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result
print
print "04. eSCM 주문번호 데이터 체크 완료 :", (result)
print
print '05. eSCM 에서 WMS로 주문전송 완료'

driver.close()

# wms 로그인
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 10)
driver.get('https://wms02.dev.kurly.com/')

driver.maximize_window()

# wms_02 로그인 하기
driver.find_element_by_id('USERID').send_keys('jiun.han')
driver.find_element_by_id('PASSWD').send_keys('wldnsgks1@@')
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/input').click()
time.sleep(2)

# wms 메인
wms_main = driver.window_handles[0]
# wms 팝업
wms_popup = driver.window_handles[1]

# wms 메인 종료
driver.switch_to.window(wms_main)
driver.close()

# wms 팝업
driver.switch_to.window(wms_popup)
time.sleep(2)

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL12] 컬리 오더 생성
driver.find_element_by_link_text('출하관리').click()
driver.find_element_by_link_text('출고오더').click()
driver.find_element_by_link_text('[DL12] 컬리 오더 생성').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

Select(driver.find_element_by_xpath('//*[@id="BWART"]')).select_by_visible_text('[210]통합오더')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/div[2]/table/tbody/tr[3]/td/input[2]').send_keys(code)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/p/button').click()

result1 = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[24]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result1

driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[2]/input').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[1]').click()
time.sleep(1)

driver.switch_to.alert.accept()
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)

print
print '06. WMS에서 컬리 오더 생성 완료'

driver.switch_to.parent_frame()
driver.switch_to.frame("nav")
driver.find_element_by_xpath('//*[@id="allClose"]/img').click()
driver.switch_to.parent_frame()

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL22] 컬리 오더 할당
driver.find_element_by_link_text('할당').click()
driver.find_element_by_link_text('[DL22] 컬리 오더 할당').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

Select(driver.find_element_by_xpath('//*[@id="BWART"]')).select_by_visible_text('[210]통합오더')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr[3]/td/input[2]').send_keys(code)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/p/button').click()
result2 = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[27]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result2

driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[2]/input').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[2]').click()
time.sleep(1)

driver.switch_to.alert.accept()
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()

print
print '07. WMS에서 컬리 오더 할당 완료'

driver.switch_to.parent_frame()
driver.switch_to.frame("nav")
driver.find_element_by_xpath('//*[@id="allClose"]/img').click()
driver.switch_to.parent_frame()

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL31] 피킹 완료
driver.find_element_by_link_text('피킹').click()
driver.find_element_by_link_text('[DL31] 피킹 완료').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

Select(driver.find_element_by_xpath('//*[@id="searchArea"]/table/tbody/tr[3]/td/select')).select_by_visible_text('[210]통합오더')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/div[2]/table/tbody/tr[1]/td/input[2]').send_keys(code)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/p/button').click()
result3 = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[8]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result3

# 송장번호 발췌
eshpky = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[14]').text

driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[2]/input').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[2]').click()
time.sleep(1)

driver.switch_to.alert.accept()
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()

print
print '08. WMS에서 컬리 오더 피킹 완료'
print '송장번호 :', (eshpky)

driver.switch_to.parent_frame()
driver.switch_to.frame("nav")
driver.find_element_by_xpath('//*[@id="allClose"]/img').click()
driver.switch_to.parent_frame()

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL41] 패킹 완료
driver.find_element_by_link_text('패킹').click()
driver.find_element_by_link_text('[DL41] 패킹 완료').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

Select(driver.find_element_by_xpath('//*[@id="searchArea"]/table/tbody/tr[4]/td/select')).select_by_visible_text('[210]통합오더')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/div[2]/table/tbody/tr[1]/td/input[2]').send_keys(code)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/p/button').click()
result4 = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[34]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result4

driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[2]/input').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[3]').click()
time.sleep(1)

driver.switch_to.alert.accept()
driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()

print
print '09. WMS에서 컬리 오더 패킹 완료'

driver.switch_to.parent_frame()
driver.switch_to.frame("nav")
driver.find_element_by_xpath('//*[@id="allClose"]/img').click()
driver.switch_to.parent_frame()

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL54] 분류스캔
driver.find_element_by_link_text('분류').click()
driver.find_element_by_link_text('[DL54] 분류스캔').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

driver.find_element_by_xpath('//*[@id="ESHPKY"]').send_keys((eshpky), '-0001')
driver.find_element_by_xpath('//*[@id="ESHPKY"]').send_keys(Keys.ENTER)

result5 = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[5]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result5

print '10. WMS에서 분류 스캔 완료'

std_wareky = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[2]').text
std_shpoky = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[3]').text
std_shpmty = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[4]').text
std_svbeln = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[5]').text
std_eshpky = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[6]').text
std_cuname = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[7]').text
std_rcname = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[8]').text
std_addr1 = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[9]').text
std_addr2 = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[10]').text

print
print '***** 주문 생산처리 결과 *****'
print
print '센터 :', (std_wareky)
print '출하문서번호 :', (std_shpoky)
print '출하유형 :', (std_shpmty)
print '주문번호 :', (std_svbeln)
print '송장번호 :', (std_eshpky)
print '고객명 :', (std_cuname)
print '수령자 :', (std_rcname)
print '기본주소 :', (std_addr1)
print '상세주소 :', (std_addr2)

driver.switch_to.parent_frame()
driver.switch_to.frame("nav")
driver.find_element_by_xpath('//*[@id="allClose"]/img').click()
driver.switch_to.parent_frame()

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL61] 컬리출고
driver.find_element_by_link_text('출고').click()
driver.find_element_by_link_text('[DL61] 컬리출고').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

Select(driver.find_element_by_xpath('//*[@id="BWART"]')).select_by_visible_text('[210]통합오더')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/div[2]/table/tbody/tr[1]/td/input[2]').send_keys(code)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/p/button').click()
result6 = driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[26]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result6

driver.find_element_by_xpath('//*[@id="gridList"]/tr/td[2]/input').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[2]/span[2]').click()
time.sleep(1)

driver.switch_to.alert.accept()
time.sleep(1)
driver.switch_to.alert.accept()

print
print '11. WMS에서 컬리 오더 출고 완료'

driver.switch_to.parent_frame()
driver.switch_to.frame("nav")
driver.find_element_by_xpath('//*[@id="allClose"]/img').click()
driver.switch_to.parent_frame()

# wms 프레임 선택
driver.switch_to.frame("left")

# [DL14] 출하 조회
driver.find_element_by_link_text('[DL14] 출하 조회').click()
driver.switch_to.parent_frame()

# 프레임 전환
driver.switch_to.frame("body0")

driver.find_element_by_xpath('//*[@id="searchArea"]/div/div[2]/table/tbody/tr[2]/td/input[2]').send_keys(code)
driver.find_element_by_xpath('//*[@id="searchArea"]/div/p/button[1]').click()
result7 = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[11]').text

# 등록된 데이터가 정상인지 확인하고 출력
assert (code) in result7

statdo = driver.find_element_by_xpath('//*[@id="gridHeadList"]/tr/td[7]').text

print
print '문서상태 :', (statdo)