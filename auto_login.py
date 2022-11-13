import time
import datetime
import random
from selenium import webdriver

current =datetime.datetime.now()
current = str(datetime.datetime.strftime(current,'%Y-%m-%d-%a %H:%M:%S'))
if current[11:14] not in ('Sat','Sun'):
    if int(current[15:17])<=8:
        driver = webdriver.Chrome()
        driver.get('https://gaio.csscorp.com')
        time.sleep(1)
        input_name = driver.find_element(by='xpath',value='/html/body/div/form/input[1]')
        input_name.send_keys('tian.luan@csscorp.com')
        time.sleep(1)
        input_pwd = driver.find_element(by='xpath',value='/html/body/div/form/input[2]')
        input_pwd.send_keys('GodricRen!@#300018')
        random_sleep = random.randint(2,200)
        print(random_sleep)
        time.sleep(random_sleep)
        btn_checkin = driver.find_element(by='xpath',value='/html/body/div/form/div[3]/div[1]/input')
        btn_checkin.click()      
        time.sleep(2)
        driver.quit()
        print('login successful')
    if int(current[15:17])>=17:
        driver = webdriver.Chrome()
        driver.get('https://gaio.csscorp.com')
        time.sleep(1)
        input_name = driver.find_element(by='xpath',value='/html/body/div/form/input[1]')
        input_name.send_keys('tian.luan@csscorp.com')
        time.sleep(1)
        input_pwd = driver.find_element(by='xpath',value='/html/body/div/form/input[2]')
        input_pwd.send_keys('GodricRen!@#300018')
        random_sleep = random.randint(2,200)
        print(random_sleep)
        time.sleep(random_sleep)
        btn_checkout = driver.find_element(by='xpath',value='/html/body/div/form/div[3]/div[2]/input')
        btn_checkout.click()
        time.sleep(2)
        driver.quit()
        print('logout successful')
        
else:
    print('today is weekend')



