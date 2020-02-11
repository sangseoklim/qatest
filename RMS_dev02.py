from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import subprocess, datetime, time

# 테스트서버 입력
server = '02'
rms_web_id = 'qa_auto_test'
rms_web_pw = 'kurlyqa123'

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
print ()
print ('* eSCM > 발주서 생성 결과 : Pass / ' + Pom)

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
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/div[1]/div/div[1]/div/input').send_keys (rms_web_id)
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/div[2]/div/div[1]/div/input').send_keys (rms_web_pw)
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

# 검수 리스트 검증
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
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[1]/div[1]/div/div/div[3]/div/input').send_keys("/Users/tf-mac-059/PycharmProjects/untitled1/venv/12345.png")
time.sleep(3)
# 포장불량 이슈 1개 등록
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/input').send_keys('1')
time.sleep(2)
# 저장
driver.find_element_by_css_selector('#app > div.application--wrap > main > div > div > div.flex > button').click()
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
time.sleep(2)

print ('* RMS > 검수 > 검수 확정 : Pass')

# 검품 메뉴 접근
driver.get ('https://m' + server + '.rms.dev.kurly.com')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[2]/div/div/button').click()
time.sleep(1)

# 발주 코드 입력 후 스캔 처리
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div/div/div/div[1]/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div/div/div/div[1]/div/input').send_keys(Keys.RETURN)
time.sleep(2)

print ('* RMS > 검품 > 발주코드 스캔 결과 : Pass')

E1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[3]/div/div/div/div[1]/span').text
assert '10개 / 0개 / 1개' in E1
E2 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[3]/div/div/div/div[2]').text
assert '[센터] QA자동화테스트 상품' in E2

print ('* RMS > 검품 > 발주목록 검증 결과 : Pass')

# 검품 > 상품코드 스캔
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/input').send_keys('QA1111222222')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/input').send_keys(Keys.RETURN)
time.sleep(1)

print ('* RMS > 검품 > 상품코드 스캔 결과 : Pass')

# 검품 > 이슈등록
# 이슈 관리 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div/div/div[2]/div[1]/button').click()
time.sleep(1)
# 검품 > 이슈 등록 > 사진업로드
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[1]/div[1]/div/div/div[3]/div/input').send_keys('/Users/tf-mac-059/PycharmProjects/untitled1/venv/12345.png')
# 검품 > 이슈 수량 추가 (유통기한(제조일자) 기준미달)
driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div/div[6]/div[2]/div/div[2]/div/div/div[1]/div/input').send_keys('1')
time.sleep(1)
# 이슈 수량 저장
driver.find_element_by_css_selector('#app > div.application--wrap > main > div > div > div.flex > button').click()
time.sleep(1)

print ('* RMS > 검품 > 이슈 수량/이미지 등록 결과 : Pass')

# 검품 완료 하기 버튼 클릭
driver.find_element_by_css_selector('#app > div > main > div > div > div.flex > div > div > button').click()
time.sleep(2)

# 검품 > 상품 목록에서 수량 검증
F1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[3]/div/div/div/div[1]/span').text
assert '10개 / 10개 / 2개' in F1
time.sleep(1)

# 입하 확정 조회
driver.get('https://m' + server +'.rms.dev.kurly.com/#/dashboard/receiving/receivedList')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div/div/div/div/div[1]/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div/div/div/div[1]/div/input').send_keys(Keys.RETURN)
time.sleep(1)

# 입하 확정 조회 데이터 검증
L1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[1]').text # 검수자
assert 'qa_auto_test' in L1
L2 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[2]').text # 검품자
assert 'qa_auto_test' in L2
L3 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[4]').text # 발주코드
assert Pom in L3
L4 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[5]').text # 공급자명
assert '・ jy_auto_vendor' in L4
L5 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[6]').text # 상품코드
assert 'QA1111222222' in L5
L6 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[7]').text # 대체코드
assert '・ QA888888888' in L6
L7 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[8]').text # 센터상품명
assert '[센터] QA자동화테스트 상품' in L7
L8 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/span[1]').text # 날짜
assert '유통 2030-12-31' in L8
L9 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/span[2]').text # 발주/입하/이슈 수량
assert '・ 10 ・ 10 ・ 2 ・ 확정' in L9
L10 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/span[3]').text # 확정수량
assert '8' in L10

print ('* RMS > 입하 확정 조회 검증 결과 : Pass')

# 검품 완료 조회
driver.get('https://m' + server +'.rms.dev.kurly.com/#/dashboard/inspection/inspectedList')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div/div/div/div/div[1]/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[1]/div/div/div/div/div[1]/div/input').send_keys(Keys.RETURN)
time.sleep(1)

# 검품 완료 데이터 검증
M1 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[1]').text # 검수자
assert 'qa_auto_test' in M1
M2 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[2]').text # 검품자
assert 'qa_auto_test' in M2
M3 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[4]').text # 발주코드
assert Pom in M3
M4 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[5]').text # 공급사명
assert '・ jy_auto_vendor' in M4
M5 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[6]').text # 상품코드
assert 'QA1111222222' in M5
M6 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[7]').text # 대체코드
assert '・ QA888888888' in M6
M7 = driver.find_element_by_xpath('//html/body/div/div/main/div/div/div[2]/div[2]/div/div[1]/span[8]').text # 센터상품
assert '[센터] QA자동화테스트 상품' in M7
L8 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/span[1]').text # 날짜
assert '유통 2030-12-31' in L8
M9 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/span[2]').text # 발주/입하/이슈 수량
assert '・ 10 ・ 10 ・ 2 ・ 확정' in M9
M10 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/span[3]').text # 확정수량
assert '8' in M10
M11 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/div[1]/div/span[1]').text # 이슈문구1
assert '패키지_오염' in M11
M12 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/div[1]/div/span[2]').text # 이슈수량
assert '1' in M12
M13 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[1]').text # 이슈문구2
assert '유통기한(제조일자)_유통기한(제조일자) 기준미달' in M13
M14 = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[2]').text # 이슈수
assert '1' in M14

print ('* RMS > 검품 완료 조회 검증 결과 : Pass')

# --------------- RMS 어드민 검증 시작 --------------------

# 입하관리 페이지 이동
driver.get ('https://web' + server + '.rms.dev.kurly.com/#/receiving/list')

# 입하관리 로그인
driver.find_element_by_id('inputEmail').send_keys(rms_web_id)
driver.find_element_by_id('inputPassword').send_keys(rms_web_pw)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/form/div/button').click()
time.sleep(2)

# 데이터가 조회되지 않아 페이지 새로고침
driver.get ('https://web' + server + '.rms.dev.kurly.com/#/receiving/list')

# 발주코드 입력 후 검색
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
time.sleep(1)

# 검색결과 목록 데이터 검증 (귀찮아서 통으로)
G1 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[2]/div').text #입하상태
assert '입하완료' in G1
G2 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[5]/div').text #판매방법
assert '후판매' in G2
G3 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[7]').text #센터상품명
assert '[센터] QA자동화테스트 상품' in G3
G4 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[8]').text #발주수량
assert '10' in G4
G5 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[9]').text #입하수량
assert '10' in G5
G6 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[10]').text #이슈수량
assert '2' in G6
G7 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[11]').text #입하확
assert '8' in G7
time.sleep(1)

print ('* RMS입하관리 > 입하내역 조회 결과 : Pass')

# 입하 작업 내역 보정 처리 하기
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[2]/div/ul/li[2]/a').click()
time.sleep(1)

# 발주코드 조회
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
time.sleep(1)

# 보정 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[16]/button').click()
time.sleep(2)

# 입하 결과 보정 팝업 검증 (placeholder을 text로 가져오지 못해 보류)
"""""
H1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div').text #판매기한 검증
print (H1)
# assert '유통기한: 2030-12-31 / 센터 판매 마감 2030-12-21' in H1
H2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[5]/div[2]/input').text # 입하 수량 검증
assert '발주: 10 / 입하: 10 / 입하 이슈: 2 / 입하 확정: 8 / 자사 귀책: 0' in H2
H3 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[6]/div[2]/textarea').text # 입하 이슈 검증
assert '패키지_오염 : 1 / 유통기한(제조일자)_유통기한(제조일자) 기준미달 : 1' in H3
H4 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[7]/div[2]/input').text # 작업자 검증
assert '검수자: qa_auto_test / 검품자: qa_auto_test' in H4

print ('* RMS입하관리 > 입하 결과 보정 팝업 검증 : Pass')
"""

# 변경 사유 선택
Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[1]/div[2]/div[1]/div[2]/fieldset/div/div/select')).select_by_visible_text('판매기한 오입력')
time.sleep(1)
# 사유 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[1]/div[2]/div[2]/div/textarea').send_keys('판매기한 오입력 보정 사유')
time.sleep(1)
# 일자 변경
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/div/div[2]/fieldset/div/div/div/div[1]/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/div/div[2]/fieldset/div/div/div/div[1]/input').send_keys('2030-12-30')
time.sleep(1)
# 센터판매마감일 적용 검증
I1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/div/div[2]/fieldset/div').text
assert '센터판매마감: 2030-12-20' in I1
# 변경 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)
# 판매기한 보정 결과 검증
I2 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[12]').text
assert '2030-12-30' in I2

print ('* RMS입하관리 > 판매기한 보정 처리 결과 : Pass')

# 보정 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[16]/button').click()
time.sleep(2)
# 변경 사유 선택
Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[1]/div[2]/div[1]/div[2]/fieldset/div/div/select')).select_by_visible_text('입하수량 오입력')
time.sleep(1)
# 사유 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[1]/div[2]/div[2]/div/textarea').send_keys('입하수량 오입력 보정 사유')
time.sleep(1)
# 입하수량 초기화 후 9 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/fieldset/div/div/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/fieldset/div/div/input').send_keys('9')
time.sleep(1)
# 변경 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)
# 데이터 갱신을 위해 검색 버튼 클릭하기
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
time.sleep(1)
# 입하수량 보정 결과 검증
I3 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[7]').text # 입하수량
assert '9' in I3
I4 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[9]').text # 입하확
assert '7' in I4

print ('* RMS입하관리 > 입하수량 보정 처리 결과 : Pass')

# 보정 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[16]/button').click()
time.sleep(2)
# 변경 사유 선택
Select(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[1]/div[2]/div[1]/div[2]/fieldset/div/div/select')).select_by_visible_text('입하이슈 오입력')
time.sleep(1)
# 사유 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[1]/div[2]/div[2]/div/textarea').send_keys('입하이슈 오입력 보정 사유')
time.sleep(1)
# 이취 수량 1 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/div[4]/div/div[12]/div[2]/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/div[4]/div/div[12]/div[2]/input').send_keys('1')
time.sleep(1)
# 이미지 등록
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[8]/div/form/div[3]/div[2]/div[7]/div[1]/input').send_keys('/Users/tf-mac-059/PycharmProjects/untitled1/venv/12345.png')
time.sleep(2)
# 변경 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)
# 데이터 갱신을 위해 검색 버튼 클릭하기
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
# 검증
I5 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[8]').text # 이슈수량
assert '3' in I5
I6 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[9]').text # 입하확정
assert '6' in I6
I7 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[15]/div').text # 입하보정
assert 'Y' in I7
time.sleep(1)

print ('* RMS입하관리 > 입하이슈 수량/이미지 보정 처리 결과 : Pass')

# 기타 이슈 처리
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[17]/button').click()
time.sleep(1)
# 사유 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[7]/div/form/div[4]/div/textarea').send_keys('기타 이슈 처리 사유')
time.sleep(1)
# 수량 등록
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[7]/div/form/div[6]/div[2]/fieldset/div/div/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[7]/div/form/div[6]/div[2]/fieldset/div/div/input').send_keys('1')
# 변경 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)
# 팝업창 확인
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)
# 데이터 갱신을 위해 검색 버튼 클릭하기
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
# 검증
I8 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[9]').text # 입하확정 (영향없는지 확인)
assert '6' in I8
I9 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[10]').text # 자사귀책
assert '1' in I9

print ('* RMS입하관리 > 기타이슈 보정 처리 결과 : Pass')

# 조회 결과 입력하여 재확인
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('Y')
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/fieldset/div/div/select')).select_by_visible_text('Y')
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[3]/fieldset/div/div/select')).select_by_visible_text('Y')
# 검색 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
time.sleep(1)
# 조회 결과 검증
I10 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[1]').text
assert Pom in I10

print ('* RMS입하관리 > 이슈/보정여부값 업데이트 검증 결과 : Pass')

# 입하 내역 상세 팝업 검증하러 가기
# 입하 내역 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[2]/div/ul/li[1]/a/span').click()
time.sleep(1)
# 발주코드 입력 후 검색
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
time.sleep(1)

# 상세 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[14]/button').click()
time.sleep(1)

J1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/div/div[2]/span[1]').text # 입하상태
assert '[부분입하]' in J1
J2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/div/div[2]/span[2]').text # 요약 전체 수량
assert '입하 수량: 9 | 이슈 수량: 3 | 입하 확정 수량: 6 | 자사 귀책: 1 | 최종 입하 수량: 5' in J2
J3 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr/td[4]').text # 입하정보 > 유통기한
assert '2030-12-30' in J3
J4 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr/td[5]').text # 입하정보 > 센터 판매 마감일
assert '2030-12-20' in J4
J5 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr/td[6]').text # 입하정보 > 입하 수량
assert '9' in J5
J6 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr/td[7]').text # 입하정보 > 이슈 수량
assert '3' in J6
J7 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr/td[8]').text # 입하정보 > 검수자
assert 'qa_auto_test' in J7
J8 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr/td[10]').text # 입하정보 > 검품
assert 'qa_auto_test' in J8

J9 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[3]/div/table/tbody/tr[1]/td[4]').text # 입하 이슈 정보 > 사유1
assert '오염' in J9
J10 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[3]/div/table/tbody/tr[2]/td[4]').text # 입하 이슈 정보 > 사유2
assert '유통기한(제조일자) 기준미달' in J10
J11 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[3]/div/table/tbody/tr[3]/td[4]').text # 입하 이슈 정보 > 사유3
assert '이취' in J11

J12 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[4]/div/table/tbody/tr/td[5]').text # 기타 이슈 정보 > 사유
assert '파손' in J12

J13 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[5]/div/table/tbody/tr[1]/td[5]').text # 입하 작업 보정 정보1
assert '판매기한 오입력 보정 사유' in J13
J14 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[5]/div/table/tbody/tr[2]/td[5]').text # 입하 작업 보정 정보2
assert '입하수량 오입력 보정 사유' in J14
J15 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[5]/div/table/tbody/tr[3]/td[5]').text # 입하 작업 보정 정보3
assert '입하이슈 오입력 보정 사유' in J15

# 이미지 업로드 확인 (3번째 이미지만)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[6]/div/div/div/div[3]/img').click()
time.sleep(1)
# 이미지 팝업창 닫기
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/footer/div/button[3]').click()
time.sleep(1)

# 입하 상세 내역 팝업 닫기
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button').click()
time.sleep(1)

print ('* RMS입하관리 > 입하 내역 상세 팝업 검증 결과 : Pass')

# 입고관리 메뉴 이동
driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[1]/li[2]/a').click()
time.sleep(1)

# 검색어 구분 선택
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/select')).select_by_visible_text('발주코드')
time.sleep(1)
# 발주코드 입력 후 조회
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/input').send_keys(Pom)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[5]/fieldset/div/button[1]').click()
time.sleep(1)
# 라벨 수 검증
K1 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[7]').text
assert '1' in K1
# 체크박스 선택
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[1]/div').click()
time.sleep(1)
# 라벨 수 변경
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/div/table/tbody/tr/td[7]/input').clear()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[2]/div/div/table/tbody/tr/td[7]/input').send_keys('2')
# 변경 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/div/button[1]').click()
time.sleep(1)
# 라벨 수 검증
K2 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[7]').text
assert '2' in K2

print ('* RMS입고관리 > 입고 라벨 수 변경 결과 : Pass')

# 입고 라벨 출력
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[3]/div[1]/button').click()
time.sleep(3)

print ('* RMS입고관리 > 입고 라벨 출력 결과 : Pass')

# 현재 브라우저를 종료함
driver.close()

# 모든 테스트 코드가 수행완료되면 아래의 메시지를 노출함
now = datetime.datetime.today()
print ()
print ('* RMS UI 자동화 테스트 수행완료')
print ()
print ('테스트 종료시간 ▼')
print (now)