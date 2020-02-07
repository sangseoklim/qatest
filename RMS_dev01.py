from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import subprocess, datetime, time

# 테스트서버 입력
server = '01'

driver = webdriver.Chrome('/Users/tf-mac-059/Desktop/python/chromedriver')
driver.implicitly_wait(10)
browser = '/Users/tf-mac-059/Desktop/python/chromedriver'
driver = webdriver.Chrome(browser)

now = datetime.datetime.today()
print ()
print ('테스트 시작시간 ▼')
print (now)

# 발주서 생성
# eSCM md 로그인
driver.get ('https://escm' + server + '.dev.kurly.com/escm/sign')
# 아이디 입력란을 찾은 후, 아이디를 입력함
driver.find_element_by_id('user_id').send_keys ('qa_md3@kurlycorp.com')
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_id('user_pwd').send_keys ('dkfn4807%%')
# 로그인 버튼을 찾은 후, 클릭
driver.find_element_by_id('login-submit').click()
time.sleep(1)

# GNB > new eSCM > 발주관리 메뉴 이동
driver.find_element_by_partial_link_text('new eSCM').click()
time.sleep(1)
driver.find_element_by_partial_link_text('발주관리').click()
time.sleep(1)

# 상품코드 검색
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys('QA1111222222')
time.sleep(1)
# 검색버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/button[1]').click()
time.sleep(1)

# 검색결과 체크박스 선택
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[1]/div').click()
# 발주그룹 생성 버튼 클릭
driver.find_element_by_id('viewPurchaseOrder').click()
time.sleep(1)

# 발주그룹 생성 상세페이지 접근
# 수량 입력
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[8]/input').send_keys('10')
# 긴급발주 설정
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[10]/select')).select_by_visible_text('긴급발주')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/button[2]').click()
time.sleep(2)

# 발주서 등록완료 팝업 닫기
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/header/button').click()
time.sleep(5)

# 로그아웃
driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[2]/li[3]/a').click()

print ()
print ('* eSCM > 발주서 생성 결과 : Pass')

# 공급사 계정으로 발주확정 하기
driver.get ('https://front' + server + '.escm.dev.kurly.com/#/login')
driver.find_element_by_id('inputEmail').send_keys ('VD3370.01')
driver.find_element_by_id('inputPassword').send_keys ('1111')
driver.find_element_by_xpath('//*[@id="app"]/form/div/button').click()
time.sleep(1)

driver.find_element_by_partial_link_text('발주관리').click()
time.sleep(1)

# 상품코드 검색
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys('QA1111222222')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[3]/fieldset/div/button[1]').click()
time.sleep(2)

# 발주코드 가져오기
Pom = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[2]').text
print ('* eSCM > 발주코드 : ' + Pom)

# 상세 버튼 클릭하여 발주 상세 페이지 접근
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[15]/button').click()
time.sleep(1)

# 유통기한 입력 후 확정처리
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[14]/div[2]/div[1]/input').send_keys('2030/12/31')
time.sleep(1)

# 확인 창 닫기
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button').click()
time.sleep(2)

# 동의 체크박스 설정
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/fieldset/div/div').click()
time.sleep(1)
# 발주확정
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div[2]/button[1]').click()
time.sleep(1)
# 확인 팝업창
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()

print ('* eSCM > 발주서 확정 결과 : Pass')

# -------------- RMS start ---------------
# 페이지 접근 후 타이틀명을 검증함
driver.get ('https://m' + server + '.rms.dev.kurly.com')
assert "RMS" in driver.title

# 아이디 입력란을 찾은 후, 아이디를 입력함
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/div[1]/div/div[1]/div/input').send_keys ('qa_auto_test')
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/div[2]/div/div[1]/div/input').send_keys ('kurlyqa123')
# 로그인 버튼을 찾은 후, 클릭
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()
time.sleep(1)

print ('* RMS > 로그인 테스트 결과 : Pass')

# 검수 하기 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/div/div/button').click()
# 발주 코드 입력 후 스캔 처리
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div/div/div/div[1]/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div/div/div/div[1]/div/input').send_keys(Keys.RETURN)
time.sleep(2)

# 상품 리스트 검증 코드 작성 필요
# 검품대상 여부 딱지 노출 확인
A1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div/div/div[1]/span[1]').text
assert '검품대상' in A1
print ('* RMS > 검수 > 발주코드 스캔 결과 : Pass')
A2 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div/div/div[1]/span[2]').text
assert '10개 / 0개 / 0개' in A2
A3 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div/div/div[2]').text
assert '[센터] QA자동화테스트 상품' in A3

print ('* RMS > 검수 > 상품 리스트 검증 결과 : Pass')

# 상품 코드 스캔
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/input').send_keys('QA1111222222')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div/input').send_keys(Keys.RETURN)
time.sleep(1)

print ('* RMS > 검수 > 상품코드 스캔 결과 : Pass')

# 상품 상세 결과 검증 코드 작성 필요
B1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/div[1]').text
assert '[센터] QA자동화테스트 상품' in B1 # 센터상품명 노출 검증
B2 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/div[2]').text
assert 'QA1111222222' in B2 # 상품코드 노출 검증
B3 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/div[3]').text
assert 'QA888888888' in B3 # 대체코드 노출 검증
B4 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/div[4]/div[1]/div[2]').text
assert '10 개' in B4 # 발주 수량 검증
B5 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/div[4]/div[2]/div[2]').text
assert '0 개' in B5 # 검수완료 수량 검증
B6 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/div[4]/div[3]/div[2]').text
assert '0 개' in B6 # 이슈 수량 검증
B7 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div/div/div[2]/div[2]/button/div').text
assert '입하확정 0개' in B7 # 입하확정 수량 검증

print ('* RMS > 검수 > 상품 상세정보 검증 결과 : Pass')

# 입하 수량 등록
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div').click()
time.sleep(1)

# 입하 수량 등록 페이지 데이터 검증
C1 = driver.find_element_by_xpath('/html/body/div/div[7]/main/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div').text
assert '유통기한' in C1 # 발주서상의 유통기한 설정값 일 검증
C2 = driver.find_element_by_xpath('/html/body/div/div[7]/main/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div').text
assert '2030' in C2 # 발주서상의 유통기한 설정값 년 검증
C3 = driver.find_element_by_xpath('/html/body/div/div[7]/main/div/div/div[2]/div[4]/div/div/div[1]/div[1]/div[1]/div').text
assert '12' in C3 # 발주서상의 유통기한 설정값 월 검증
C4 = driver.find_element_by_xpath('/html/body/div/div[7]/main/div/div/div[2]/div[5]/div/div/div[1]/div[1]/div[1]/div').text
assert '31' in C4 # 발주서상의 유통기한 설정값 일 검증

# 입하수량 10 입력 및 저장
driver.find_element_by_xpath('/html/body/div/div[7]/main/div/div/div[2]/div[7]/div/div[2]/div[1]/div/input').send_keys('10')
driver.find_element_by_xpath('/html/body/div/div[7]/main/div/div/div[2]/div[9]/button[2]').click()
time.sleep(1)

print ('* RMS > 검수 > 입하 수량 등록 결과 : Pass')

# 이슈 관리
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div/div/div[2]/div[1]/button').click()
time.sleep(1)
# 파일 선택
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[1]/div[1]/div/div/div[3]/div/input').send_keys("/Users/tf-mac-059/Desktop/python/12345.png")
time.sleep(3)
# 포장불량 이슈 1개 등록
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/input').send_keys('1')
time.sleep(100)
# 저장
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[6]/button').click()
time.sleep(1)

# 입하/이슈/확정 수량 검증
D1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div/div/div[1]/div[1]/p[2]').text
assert '센터 판매 마감: 2030-12-21' in D1 # 센터 판매 마감일 검증
D2 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div').text
assert '1개' in D2 # 이슈수량 검증
D3 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div/div/div[2]/div[2]/button/div').text
assert '입하확정 9개' in D3 # 입하확정 수량 검증

print ('* RMS > 검수 > 이슈 수량/이미지 등록 결과 : Pass')

# 검수 완료 하기
driver.find_element_by_xpath('/html/body/div/div/main/div/div/button/div').click()
time.sleep(1)

print ('* RMS > 검수 > 검수 완료 : Pass')

# 검수 확정 하기
driver.find_element_by_xpath('/html/body/div/div/main/div/div/button[2]').click()
time.sleep(1)
# 검수 담당자 싸인
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div[2]/div/canvas').click()
# 공급사 담당자 싸인
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div/div[2]/div/canvas').click()
# 확인
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[4]/button[1]').click()
time.sleep(1)

print ('* RMS > 검수 > 검수 확정 : Pass')

# 현재 브라우저를 종료함
# driver.close()

# 모든 테스트 코드가 수행완료되면 아래의 메시지를 노출함
now = datetime.datetime.today()
print ()
print ('* RMS UI 자동화 테스트 수행완료')
print ()
print ('테스트 종료시간 ▼')
print (now)