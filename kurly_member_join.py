

now = datetime.datetime.today()
print
print "테스트 시작시간 ▼"
print now
print

driver = webdriver.Chrome('/Users/tf-mac-059/Desktop/python/chromedriver')
driver.implicitly_wait(4)
driver.get('https://www01.dev.kurly.com/shop/main/index.php')

# 회원가입 버튼 클릭
driver.find_element_by_class_name('link_menu').click()
time.sleep(1)

# ID 자동 발급 및 입력
# 랜덤한 문자열 생성
m_id = "kurly"  # ID 앞자리 고정
for i in range(5):
    m_id += random.choice(string.digits)  # 랜덤한 문자열 하나 선택 (숫자만)
print 'ID ▼'
print m_id
driver.find_element_by_name('m_id').send_keys(m_id)
# ID 중복확인
driver.find_element_by_xpath('//*[@id="form"]/div[2]/table/tbody/tr[1]/td[2]/a/span').click()
time.sleep(3)

# ID 중복확인 팝업 닫기 (크롬브라우저 자체 팝업)
driver.switch_to_alert().accept()

print
print '01. ID 중복확인 완료'
time.sleep(1)

# 패스워드 입력
driver.find_element_by_name('password').send_keys('qwert12345')
# 패스워드 다시 입력
driver.find_element_by_name('password2').send_keys('qwert12345')
# 이름 입력
driver.find_element_by_name('name').send_keys(u'한지운')
# 이메일 입력
driver.find_element_by_name('email').send_keys('hpblack_works1@naver.com')
# 이메일 중복확인
driver.find_element_by_xpath('//*[@id="form"]/div[2]/table/tbody/tr[5]/td[2]/a/span').click()
# 이메일 중복확인 팝업 닫기 (크롬브라우저 자체 팝업)
driver.switch_to_alert().accept()
print '02. 이메일 중복확인 완료'

# 휴대폰 번호 입력
driver.find_element_by_name('mobileInp').send_keys('01053332368')
# 휴대폰 인증번호 버튼 클릭
driver.find_element_by_xpath('//*[@id="btn_cert"]/span').click()
time.sleep(1)
# 휴대폰 인증번호 팝업 확인 버튼
driver.find_element_by_xpath('//html/body/div[1]/div[1]/div[2]/button').click()
time.sleep(1)
# 휴대폰 인증번호 입력
driver.find_element_by_name('auth_code').send_keys('1111')
time.sleep(1)
# 인증번호 확인
driver.find_element_by_xpath('//*[@id="btn_cert_confirm"]/span').click()
# 인증완료 팝업 닫기
driver.find_element_by_xpath('//html/body/div[1]/div[1]/div[2]/button').click()
print '03. 휴대폰 인증완료'
time.sleep(1)

# 주소 검색
driver.find_element_by_xpath('//*[@id="btnAddressSearch"]/span').click()
time.sleep(1)

# 마지막 창(주소입력 팝업창)을 변수에 저장
address_window = driver.window_handles[-1] # 주소 팝업
main_window = driver.window_handles[0] # 메인 윈도우

# 위에서 저장한 창으로 전환
driver.switch_to.window(window_name=address_window)

# frame 전환
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="__daum__layer_1"]/iframe')) # 상위frame
driver.switch_to.frame('__daum__viewerFrame_1') # 하위 frame

# 주소입력 후 확인버튼 클릭
driver.find_element_by_id('region_name').send_keys('kbl')
driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/div/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li/dl/dd[1]/span/button').click()
time.sleep(1)

# frame 벗어나기 (frame 2회 전환)
driver.switch_to.parent_frame()
driver.switch_to.parent_frame()

# 나머지 주소 입력
driver.find_element_by_xpath('//*[@id="road-address-confirm"]/div[4]/input').send_keys('kurly')
time.sleep(1)

# 주소입력(확인) 버튼 클릭
driver.find_element_by_xpath('//*[@id="road-address-confirm"]/div[5]/input').click()

# 메인 윈도우로 이동
driver.switch_to.window(window_name=main_window)

# 샛별배송 팝업창 확인 버튼 클릭
driver.find_element_by_xpath('//*[@id="layerDSR"]/div[2]/button').click()
time.sleep(1)





time.sleep(1)
# 메인 윈도우로 돌아오기
