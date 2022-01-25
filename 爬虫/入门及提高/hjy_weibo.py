import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://weibo.com/u/5502931489')
time.sleep(10)
wd.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[1]/div/a[1]').click()
time.sleep(5)
wd.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[1]/div/div[2]/div/div/div[5]/a[1]').click()
time.sleep(5)
wd.find_element(By.XPATH,'//*[@id="loginname"]').send_keys('18811083955')
wd.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(',cscs741386')
time.sleep(2)
wd.find_element(By.XPATH,'//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(5)

