from selenium import webdriver
import datetime

# 테스트서버 입력
server = '01'

driver = webdriver.Chrome('/Users/tf-mac-059/Desktop/python/chromedriver')
browser = '/Users/tf-mac-059/Desktop/python/chromedriver'
driver = webdriver.Chrome(browser)

now = datetime.datetime.today()
print ()
print ('테스트 시작시간 ▼')
print (now)

# 페이지 접근 후 타이틀명을 검증함
driver.get ('https://m' + server + '.rms.dev.kurly.com')
assert "RMS" in driver.title

# 아이디 입력란을 찾은 후, 아이디를 입력함
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/div[1]/div/div[1]/div/input').send_keys ('qa_auto_test')
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/div[2]/div/div[1]/div/input').send_keys ('kurlyqa123')
# 로그인 버튼을 찾은 후, 클릭
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/button').click()