from selenium import webdriver

url = 'http://172.20.4.253/index.php?m=my&f=index'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(15)
driver.maximize_window()
usr = 'madongmei'
psw = 'Chz2tdm!XNvbN*9p'
driver.find_element_by_id('account').send_keys(usr)
driver.find_element_by_name( 'password').send_keys(psw)
driver.find_element_by_id('submit').click()

