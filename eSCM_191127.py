from selenium.webdriver import jenkins
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from Prd_create_class import Product
import datetime, random, time, locale, re, string

# 테스트서버 입력
server = input('* 테스트서버 번호를 입력해주세요. >> ')[:2]

driver = webdriver.Chrome('/Users/tf-mac-059/Desktop/python/chromedriver')
browser = '/Users/tf-mac-059/Desktop/python/chromedriver'
driver = webdriver.Chrome(browser)

now = datetime.datetime.today()
print ()
print ('테스트 시작시간 ▼')
print (now)

# 상품코드 자동생성
Prd_code = 'MK'  # 상품코드 앞자리 고정
for i in range(10):
   Prd_code += random.choice(string.digits)  # 랜덤한 문자열 하나 선택 (숫자만)
print ()
print ('상품코드 ▼')
print (Prd_code)

# 대체 코드 생성
Alter_code = random.randint(100000,999999999999999)

# 전체 페이지의 텍스트를 가져오는 변수
HolePage = driver.find_element_by_xpath('/html').text

# 페이지 접근 후 타이틀명을 검증함
driver.get ('https://escm' + server + '.dev.kurly.com/escm/sign')

assert "eSCM" in driver.title

# 아이디 입력란을 찾은 후, 아이디를 입력함
driver.find_element_by_id('user_id').send_keys ('qa_md3@kurlycorp.com')
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_id('user_pwd').send_keys ('dkfn4807%%')
# 로그인 버튼을 찾은 후, 클릭
driver.find_element_by_id('login-submit').click()

# 페이지 로딩 시간을 감안하여 sleep 1초 적용
time.sleep(2)

# SKU관리 메뉴 검색 > 클릭 > 페이지 정상 노출 확인
driver.find_element_by_link_text('SKU관리').click()

# 접근한 페이지의 초기화면이 '[SK01] 상품등록관리' 페이지가 맞는지 검증
Menu1 = driver.find_elements_by_xpath('//*[@id="main_wrap01"]/div[2]/div[2]/div/div[1]/div/h4')
#Menu1 변수에 위에서 가져온 제목을 가져옴
Menu1 = Menu1[0].text

# '[SK01] 상품등록관리' 메뉴명이 맞는지 검증 (인코딩 문제로 utf-8 로 변환처리)
assert Menu1 == '[SK01] 상품등록관리'

# new eSCM메뉴로 이동
driver.find_element_by_link_text('new eSCM').click()

# 검색결과 테이블의 텍스트를 가져옴
time.sleep(5)
ListTable = driver.find_element_by_id('listTable').text
time.sleep(1)
# 검색결과가 있음을 확인
# assert "데이터가 없습니다." not in ListTable.encode('utf-8')

# 상품 추가 버튼을 클릭하여 상품등록 페이지로 이동
print ()
print ('****** 상품 등록을 시작합니다. ******')

# 상품 추가 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]').click()
time.sleep(1.5)

# 공급사 조회버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/button').click()
time.sleep(1)

# 공급사명 입력
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/input').send_keys('jy_auto_vendor')
# 검색버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/button').click()
time.sleep(1)
# 검색결과 선택
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[3]/div/div/table/tbody/tr/td[2]/a').click()
time.sleep(1)

#상품코드
driver.file_detector

P_code = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button').click()

# 상품명 입력
R_name = str(random.randint(1000,9999))
N_name = 'jy_automated test ' + R_name
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[3]/div[1]/div/div[2]/input').send_keys(N_name)
# 분류
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/select')).select_by_visible_text('채소/과일/곡류')
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[3]/select')).select_by_visible_text('채소')
# 판매방법
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[6]/div[1]/div/div[2]/select')).select_by_visible_text('후판매')
# 출고방법
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[7]/div/div/div[2]/select')).select_by_visible_text('컬리픽업')
# 담당자 전화번호
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[3]/input').send_keys('010-4474-8480')
# 출고주소 + 상세주소 default 문구 제거 후 직접입력 (굳이 안해도 되지만 clear 함수 사용해보기 연습)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[3]/input').clear()
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[3]/input').send_keys('address')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[3]/input').clear()
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[3]/input').send_keys('address detail')
# 판매가능일수 + 판매마감일수
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[11]/div[1]/div/div[2]/div/input').send_keys('101')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[11]/div[2]/div/div[2]/div/input').send_keys('102')
# 샛별오더유형
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[13]/div[1]/div/div[2]/select')).select_by_visible_text('210(냉장합포)')
# 보관유형
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[1]/div[2]/div/div[2]/select')).select_by_visible_text('냉장(필수)')
#유통가능일수/리드타임/최소발주수량
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[1]/div/div[2]/div/input').send_keys('10')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[2]/div/div[2]/div/input').send_keys('11')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[3]/div/div/div[2]/div/input').send_keys('12')
# 중량/박스당중량
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[6]/div[1]/div/div[2]/div/input').send_keys('13')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[6]/div[1]/div/div[3]/div/input').send_keys('14')
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[5]/div[2]/div/div[2]/div/input').send_keys('15') 자동입력
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[6]/div[2]/div/div[3]/div/input').send_keys('16')
# 개당부피 길이/폭/높이
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[7]/div[1]/div/div[2]/div/input').send_keys('16')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[8]/div[1]/div/div[2]/div/input').send_keys('18')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[9]/div[1]/div/div[2]/div/input').send_keys('19')
# 박스당부피 길이/폭/높이
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[7]/div[2]/div/div[2]/div/input').send_keys('21')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[8]/div[2]/div/div[2]/div/input').send_keys('22')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[9]/div[2]/div/div[2]/div/input').send_keys('23')
# 비고
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[11]/div/div/div[2]/textarea').send_keys('by Product QA')

# 대체코드 입력 후 확인
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/input').send_keys(Alter_code)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/button').click()
# 적치존
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[3]/div/div/div[2]/select')).select_by_visible_text('NEW')
time.sleep(1)

# 소싱유형 선택
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[4]/div[2]/div/div[2]/select')).select_by_visible_text('NB')

# 등록버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[5]/button[1]').click()
time.sleep(1)

# 등록한 상품 정보 조회
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[3]/button[1]').click()

# 위에서 등록한 상품을 조회하여 데이터 확인
time.sleep(3)
result = driver.find_element_by_xpath('//*[@id="listTable"]/tbody').text
# 등록된 데이터가 정상인지 확인하고 출력
assert 'jy_automated' and '과세' and '210(냉장합포)' and '270(냉장합포)' and '280(합포)' and 'jy_auto_vendor' and 'VD3370' in result

print ('****** 상품 등록이 완료되었습니다. ******')
print ()
print (result)

# 로그아웃
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[2]/li[3]/a').click()

#### 공급사 계정으로 접근하여 견적서 추가 ###

# 페이지 접근 후 타이틀명을 검증함
driver.get ('https://front' + server + '.escm.dev.kurly.com/#/login')
assert "Kurly Partner Portal" in driver.title

# 파트너포털에서 공급자 계정으로 로그인함
driver.find_element_by_id('inputEmail').send_keys ('VD3370.01')
driver.find_element_by_id('inputPassword').send_keys ('1111')
driver.find_element_by_xpath('//*[@id="app"]/form/div/button').click()
time.sleep(1)

# 위에서 생성한 상품정보를 조회하고 상세페이지로 이동함
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/button[1]').click()
time.sleep(3)

# 조회한 상품의 상태가 '견적서대기'가 맞는지 검증
ListTable = driver.find_element_by_id('listTable').text
assert '견적서대기' in ListTable

# 상세 버튼 클릭
driver.find_element_by_xpath('//*[@id="listTable"]/tbody/tr/td[14]/button').click()
time.sleep(2)

# 견적서 추가 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[4]/div/div[2]/button').click()
time.sleep(1)

# 공급가 등록
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[3]/table/tbody/tr/td[5]/input').send_keys('7770')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/button[1]').click()

# 로그아웃
driver.find_element_by_xpath('//*[@id="nav_collapse"]/ul[2]/li[3]/a').click()
print ()
print ('****** 견적서 등록이 완료되었습니다. ******')

# 견적서 승인하기 프로세스 시작

# md계정으로 로그인함
driver.get ('https://escm' + server + '.dev.kurly.com/escm/sign')
driver.find_element_by_id('user_id').send_keys ('qa_md3@kurlycorp.com')
driver.find_element_by_id('user_pwd').send_keys ('dkfn4807%%')
driver.find_element_by_id('login-submit').click()
time.sleep(1)

driver.find_element_by_link_text('new eSCM').click()
time.sleep(2)
driver.find_element_by_link_text('상품리').click()
time.sleep(2)

Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[2]/div[2]/button[1]').click()
time.sleep(3)

# 조회한 상품의 상태가 'MD승인대기'가 맞는지 검증
ListTable = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody').text
assert 'MD승인대기' in ListTable
# 상세페이지로 이동하여 승인처리
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[11]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/button[1]').click()

# 모달 팝업에서 승인버튼을 클릭해야 하는데 견적서취소 버튼과 xpath가 동일해서 css_selector 활용
time.sleep(1)
driver.find_element_by_css_selector('body > div:nth-child(5) > div.modal.fade.show > div > div > footer > div > button.btn.btn-primary').click()
time.sleep(2)

# 확인 버튼 누르고 조회화면으로 이동함
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/button[2]').click()
time.sleep(1)

# 위에서 승인처리한 상품의 상태가 '등록완료' 인지 검증
ListTable = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody').text
assert '등록완료' in ListTable
print ('****** 견적서 승인이 완료되었습니다. ******')

# 상품생성 > 견적서등록 class
class Product:
   def Prd_create(self):

      driver.get('https://front' + server + '.escm.dev.kurly.com/#/goods/list')
      time.sleep(2)

      # 상품코드 자동생성
      Prd_code2 = 'MK'  # 상품코드 앞자리 고정
      for i in range(10):
         Prd_code2 += random.choice(string.digits)  # 랜덤한 문자열 하나 선택 (숫자만)
      print ()
      print ('상품코드 ▼')
      print (Prd_code2)

      # 대체 코드 생성
      Alter_code2 = random.randint(100000,999999999999999)

      # 상품 추가 버튼을 클릭하여 상품등록 페이지로 이동
      print ()
      print ('****** 상품 등록을 시작합니다. ******')

      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]').click()
      time.sleep(1.5)
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/button').click()

      time.sleep(1)

      # 공급사조회 > 검색어 입력 후 찾기 버튼 클릭
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/input').send_keys('jy_auto_vendor')
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[1]/div/form/div/button').click()
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div/div[3]/div/div/table/tbody/tr/td[2]/a').click()
      time.sleep(1)

      # 상품코드
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/input').send_keys(Prd_code2)
      time.sleep(2)
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button').click()

      # 상품명 입력
      R2_name = str(random.randint(1000, 9999))
      N2_name = 'jy_automated cancel ' + R2_name
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[3]/div[1]/div/div[2]/input').send_keys(N2_name)
      # 분류
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/select')).select_by_visible_text('채소/과일/곡류')
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[3]/select')).select_by_visible_text('채소')
      # 판매방법
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[6]/div[1]/div/div[2]/select')).select_by_visible_text('후판매')
      # 출고방법
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[7]/div/div/div[2]/select')).select_by_visible_text('컬리픽업')
      # 담당자 전화번호
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[3]/input').send_keys('010-4474-8480')
      # 출고주소 + 상세주소 default 문구 제거 후 직접입력 (굳이 안해도 되지만 clear 함수 사용해보기 연습)
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[3]/input').clear()
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[3]/input').send_keys('address')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[3]/input').clear()
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[3]/input').send_keys('address detail')
      # 판매가능일수 + 판매마감일수
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[11]/div[1]/div/div[2]/div/input').send_keys('101')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[11]/div[2]/div/div[2]/div/input').send_keys('102')
      # 샛별오더유형
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[13]/div[1]/div/div[2]/select')).select_by_visible_text('210(냉장합포)')
      # 보관유형
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[1]/div[2]/div/div[2]/select')).select_by_visible_text('냉장(필수)')
      # 유통가능일수/리드타임/최소발주수량
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[1]/div/div[2]/div/input').send_keys('10')
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[2]/div/div[2]/div/input').send_keys('11')
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[3]/div/div/div[2]/div/input').send_keys('12')
      # 중량/박스당중량
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[6]/div[1]/div/div[2]/div/input').send_keys('13')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[6]/div[1]/div/div[3]/div/input').send_keys('14')
      # driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[5]/div[2]/div/div[2]/div/input').send_keys('15') 자동입력
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[6]/div[2]/div/div[3]/div/input').send_keys('16')
      # 개당부피 길이/폭/높이
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[7]/div[1]/div/div[2]/div/input').send_keys('16')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[8]/div[1]/div/div[2]/div/input').send_keys('18')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[9]/div[1]/div/div[2]/div/input').send_keys('19')
      # 박스당부피 길이/폭/높이
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[7]/div[2]/div/div[2]/div/input').send_keys('21')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[8]/div[2]/div/div[2]/div/input').send_keys('22')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[9]/div[2]/div/div[2]/div/input').send_keys('23')
      # 비고
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[11]/div/div/div[2]/textarea').send_keys('by Product QA')

      # 대체코드 입력 후 확인
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/input').send_keys(Alter_code2)
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/button').click()
      # 적치존
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[3]/div/div/div[2]/select')).select_by_visible_text('NEW')
      time.sleep(1)

      # 소싱유형 선택
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[4]/div[2]/div/div[2]/select')).select_by_visible_text('NB')

      # 등록버튼 클릭
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[5]/button[1]').click()
      time.sleep(6) #toast 얼럿창이랑 겹쳐 오류 발생해서 길게 잡음

      print ('****** 상품 등록이 완료되었습니다. ******')

      # 로그아웃
      driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[2]/li[3]/a').click()

      #### 공급사 계정으로 접근하여 견적서 추가 ###

      # 페이지 접근 후 타이틀명을 검증
      driver.get('https://front' + server + '.escm.dev.kurly.com/#/login')
      assert "Kurly Partner Portal" in driver.title

      # 파트너포털에서 공급자 계정으로 로그인함
      driver.find_element_by_id('inputEmail').send_keys('VD3370.01')
      driver.find_element_by_id('inputPassword').send_keys('1111')
      driver.find_element_by_xpath('//*[@id="app"]/form/div/button').click()
      time.sleep(1)

      # 위에서 생성한 상품정보를 조회
      Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code2)
      driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/button[1]').click()
      time.sleep(3)

      # 조회한 상품의 상태가 '견적서대기'가 맞는지 검증
      ListTable = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody').text
      assert '견적서대기' in ListTable

      # 상세 버튼 클릭
      driver.find_element_by_xpath('//*[@id="listTable"]/tbody/tr/td[14]/button').click()
      time.sleep(1)

      # 견적서 추가 버튼 클릭
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[4]/div/div[2]/button').click()
      time.sleep(1)

      # 공급가 등록
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[3]/table/tbody/tr/td[5]/input').send_keys('7770')
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/button[1]').click()
      time.sleep(1)

      # 로그아웃
      driver.find_element_by_xpath('//*[@id="nav_collapse"]/ul[2]/li[3]/a').click()

      print ()
      print ('****** 견적서 등록이 완료되었습니다. ******')

      # md계정으로 로그인함
      driver.get ('https://escm' + server + '.dev.kurly.com/escm/sign')
      driver.find_element_by_id('user_id').send_keys ('qa_md3@kurlycorp.com')
      driver.find_element_by_id('user_pwd').send_keys ('dkfn4807%%')
      driver.find_element_by_id('login-submit').click()
      time.sleep(1)

      driver.find_element_by_xpath('//*[@id="top-nav"]/div/div[2]/ul[1]/li[6]/a').click()
      time.sleep(2)
      driver.find_element_by_xpath('//*[@id="nav_collapse"]/ul[1]/li[2]/a').click()
      time.sleep(2)

      Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code2)
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[2]/div[2]/button[1]').click()
      time.sleep(3)

      # 조회한 상품의 상태가 'MD승인대기'가 맞는지 검증
      ListTable2 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody').text
      print (ListTable2)
      assert 'MD승인대기' in ListTable2

      # 상세페이지로 이동
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[11]/button').click()
      time.sleep(1)

      # 견적서 취소
      driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/button[2]').click()
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
      time.sleep(2)

      # 조회한 상품의 상태가 '견적서취소'가 맞는지 검증
      ListTable3 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody').text
      print (ListTable3)
      assert '견적서취소' in ListTable3
      print ('****** 견적서가 정상적으로 취소되었습니다. ******')

print ()
print ('****** 견적서 취소 테스트를 위해 상품 추가 생성합니다. ******')

Cancel_test = Product()
Cancel_test.Prd_create()

print ()
print ('****** 발주그룹 등록을 시작합니다. ******')

driver.get('https://front' + server + '.escm.dev.kurly.com/#/purchaseOrder/group')
time.sleep(3)

# 조회가 안되서 초기화 한번 진행
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/button[2]').click()
time.sleep(1)

Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/button[1]').click()
time.sleep(1)

# 검색결과에서 체크박스 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[1]/div').click()
# 발주그룹 생성 버튼 클릭
driver.find_element_by_xpath('//*[@id="viewPurchaseOrder"]').click()
# 발주그룹명 입력
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/input').send_keys('group_name')
# 수량 입력
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[8]/input').send_keys('1500')

# 단가 '일반-7770원' 맞는지 확인
Unit_price = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[5]').text
assert '일반-7770원' in Unit_price
# 총수량 '14' 맞는지 확인
Weight = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[6]').text
assert '14' in Weight

# [발주그룹 생성] 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/button[1]').click()
# 팝업 > [발주그룹 내역 메뉴로 이동] 버튼 클릭
time.sleep(1)
driver.find_element_by_css_selector('body > div:nth-child(5) > div.modal.fade.show > div > div > footer > div > button.btn.btn-primary').click()

print ('****** 발주그룹 생성이 완료되었습니다. ******')

# 발주그룹 내역에서 승인(등록) 처리를 하기 위해 상품코드로 검색
time.sleep(1)
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[3]/button[1]').click()
time.sleep(1)

# 발주서의 상태가 '승인대기'가 맞는지 확인
Order_status = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[2]').text
assert '승인대기' in Order_status

# 승인(등록) 처리를 하기위해 상세페이지로 이동
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[10]/button').click()
time.sleep(1)

# [발주그룹 등록] 버튼 클릭 > 발주서 등록됨
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/button[1]').click()
time.sleep(1)
# 팝업 > [발주서 내역 메뉴로 이동] 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)

# 발주서 내역에서 위에서 승인처리한 발주서의 상태가 '발주생성'이 맞는지 확인
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[4]/fieldset/div/button[1]').click()
time.sleep(3)

# '발주생성' 상태의 정보 저장
Order_comp = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody').text
time.sleep(1)
print ()
print (Order_comp)
assert '발주생성' in Order_comp

print ('****** 발주그룹 승인 후 발주서가 정상적으로 생성되었습니다. ******')

# 발주서 직접 등록
print ()
print ('****** 발주서 등록을 시작합니다. ******')
driver.get('https://front' + server + '.escm.dev.kurly.com/#/purchaseOrder/group')
time.sleep(3)

# 조회가 안되서 초기화 한번 진행
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/button[2]').click()
time.sleep(1)

Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/button[1]').click()
time.sleep(1)

# 검색결과에서 체크박스 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[1]/div').click()
# 발주그룹 생성 버튼 클릭
driver.find_element_by_xpath('//*[@id="viewPurchaseOrder"]').click()
# 발주그룹명 입력
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/input').send_keys('group_name')
# 수량 입력
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[8]/input').send_keys('5500')

# [발주서 등록] 버튼 클릭 > 발주서 등록됨
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/button[2]').click()
time.sleep(1)
# 팝업 > [발주서 내역 메뉴로 이동] 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(1)

# 발주서 내역에서 위에서 승인처리한 발주서의 상태가 '발주생성'이 맞는지 확인
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[4]/fieldset/div/button[1]').click()
time.sleep(3)

# '발주생성' 상태의 정보 저장
Order_comp = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]').text
time.sleep(1)
print (Order_comp)
assert '발주생성' in Order_comp
print ('****** 발주서 생성이 완료되었습니다. ******')

# 로그아웃
driver.find_element_by_xpath('//*[@id="nav_collapse"]/ul[2]/li[3]/a').click()

# '발주확정' 처리를 위한 공급사 계정 접근
driver.get ('https://front' + server + '.escm.dev.kurly.com/#/login')
assert "Kurly Partner Portal" in driver.title

# 파트너포털에서 공급자 계정으로 로그인함
driver.find_element_by_id('inputEmail').send_keys ('VD3370.01')
driver.find_element_by_id('inputPassword').send_keys ('1111')
driver.find_element_by_xpath('//*[@id="app"]/form/div/button').click()
time.sleep(2)

# 발주관리 메뉴로 이동
driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[1]/li[3]/a').click()
time.sleep(1)

# 검색에서 상품코드로 검색함
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Prd_code)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[3]/fieldset/div/button[1]').click()
time.sleep(1)

# 상세 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[15]/button').click()
time.sleep(1)
# 유통기한 입력
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[14]/div[2]/div[1]/input').send_keys('2030/10/10')
time.sleep(1)
# 안내 팝업창 닫기
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button').click()
time.sleep(1)
# 동의 체크 박스
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/fieldset/div/div').click()
# 발주 확정 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div[2]/button[1]').click()
time.sleep(1)
# 모달 팝업 확인 버튼 클릭
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(5)
# 닫기 버튼 클릭하여 메뉴화면으로 이동
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div[2]/button[3]').click()
time.sleep(1)
# 검색조건의 발주상태를 발주확정으로 변경
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[1]/fieldset/div/select')).select_by_visible_text('발주확정')
# 검색 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[3]/fieldset/div/button[1]').click()
time.sleep(1)
# 검색결과의 상품코드를 가져옴
OrderComplete = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[3]').text
assert Prd_code in OrderComplete
print ('****** 발주확정이 완료되었습니다.******')

# 공급사 로그아웃
driver.find_element_by_xpath('//*[@id="nav_collapse"]/ul[2]/li[3]/a').click()
time.sleep(1)

print ()
print ('****** 공급사 등록을 시작합니다. ******')

# 공급사등록 메뉴로 이동
driver.get ('https://escm' + server + '.dev.kurly.com/escm/sign')
time.sleep(1)

# 아이디 입력란을 찾은 후, 아이디를 입력함
driver.find_element_by_id('user_id').send_keys ('qa_md3@kurlycorp.com')
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_id('user_pwd').send_keys ('dkfn4807%%')
# 로그인 버튼을 찾은 후, 클릭
driver.find_element_by_id('login-submit').click()

# 페이지 로딩 시간을 감안하여 sleep 1초 적용
time.sleep(1)

# new eSCM 메뉴 클릭
driver.find_element_by_xpath('//*[@id="top-nav"]/div/div[2]/ul[1]/li[6]/a').click()
time.sleep(1)
# 공급사 관리 메뉴 클릭
driver.find_element_by_xpath('//*[@id="nav_collapse"]/ul[1]/li[4]/a').click()
time.sleep(1)
# 공급사 등록 버튼 클릭
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button').click()
time.sleep(1)

# 사업자번호 입력
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/input[1]').send_keys("261")
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/input[2]').send_keys("81")
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/input[3]').send_keys("23567")
time.sleep(1)
driver.find_element_by_css_selector(".btn.btn-primary,조회[type='button']").click()

# 공급사 이름 생성 및 입력
string_pool = string.digits  # 숫자
# 랜덤한 문자열 생성
Vendor_name = "jy_auto_"  # 공급사 앞자리 고정
for i in range(5):
    Vendor_name += random.choice(string_pool)  # 랜덤한 문자열 하나 선택 (숫자만)
print ('공급사명 ▼')
print (Vendor_name)
V_code = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/input').send_keys(Vendor_name)

# 대표자명
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/input').send_keys(u"최진영")
# 법인등록번호
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/input').send_keys("111111-1111111")
# 업태
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[4]/div[1]/div/div[2]/div/input').send_keys("abcde")
# 종목
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[4]/div[2]/div/div[2]/div/input').send_keys("abcde")
# 주요 취급품목
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[4]/div[3]/div/div[2]/div/input').send_keys("abcde")
# 주소
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/div/input').send_keys(u"서울특별시 강남구 도산대로16길 20")
# 상세주소
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[6]/div/div/div[2]/div/input').send_keys(u"이래빌딩")
# 대표번호(필수값)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[7]/div[1]/div/div[2]/div/input').send_keys("010-4474-8480")
# fax 번호
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[7]/div[2]/div/div[2]/div/input').send_keys("02-000-0000")
# 면세
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[8]/div[1]/div/div[2]/div/select')).select_by_visible_text('면세')
# 매입시 재고팀에서 등록
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div/div[2]/label').click()
# 결제조건
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[1]/select')).select_by_visible_text('20일')
# 결제은행
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[2]/input').send_keys(u"카카오뱅크")
# 결제계좌번호
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[3]/input').send_keys("1002-0000-0000")
# 결제예금주
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]/div[4]/div[2]/div[4]/input').send_keys(u"최진영")
# 담당 MD
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]/div[1]/select')).select_by_visible_text('최진영(QA_MD3)')
# 상품지원
Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/select')).select_by_visible_text('최진영(QA_MD3)')
# 담당자명
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[4]/div[1]/input').send_keys(u"최진영")
# 담당자 휴대폰
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[4]/div[2]/input').send_keys("010-4474-8480")
# 담당자 ID
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[4]/div[3]/div/input').send_keys("01")
# 이메일
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[4]/div[4]/input').send_keys("bongaru@naver.com")
# 담당자 비밀번호
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[4]/div[5]/input').send_keys("1234")
time.sleep(1)
# 출고방법
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[2]/div/div/div[2]/select')).select_by_visible_text('컬리픽업')
time.sleep(1)
# 출고주소
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[2]/input').send_keys(u"서울특별시 강남구 도산대로16길 20")
# 출고상세주소
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[4]/div[2]/div/div[2]/input').send_keys(u"이래빌딩")
# 비고
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[5]/div/div/div[2]/textarea').send_keys("abcde")
# 거래 예정일
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[6]/div[1]/div/div[2]/div/div[1]/input').send_keys("2019/08/20")
# 유통형태
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[6]/div[2]/div/div[2]/select')).select_by_visible_text('할인점')
# 월매출
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[7]/div[1]/div/div[2]/input').send_keys("abcde")
# 종업원 (숫자입력)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[7]/div[2]/div/div[2]/input').send_keys("10")
# 차량대수 (숫자입력)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[7]/div[3]/div/div[2]/input').send_keys("10")
# 월예상매입/매출액
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[8]/div[1]/div/div[2]/input').send_keys("abcde")
# 보증/담보사항
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[8]/div[2]/div/div[2]/input').send_keys("abcde")
# 저장 (등록)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/form/div[4]/button[1]').click()
time.sleep(2)
P_code = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(Vendor_name)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div/form/div[2]/div[2]/button[1]').click()
vendor = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div[4]/div/div/table/tbody/tr/td[5]').text
assert Vendor_name in vendor
print ('****** 공급사 등록이 완료되었습니다. ******')

# 현재 브라우저를 종료함
driver.close()

# 모든 테스트 코드가 수행완료되면 아래의 메시지를 노출함
now = datetime.datetime.today()
print ()
print ('****** 자동화 테스트 수행완료 (이슈없음) ******')
print ()
print ('테스트 종료시간')
print (now)