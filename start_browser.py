#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# 参考：https://www.cnblogs.com/tobecrazy/p/4570494.html
driver = webdriver.Chrome()

driver.get("https://gitee.com/login")
time.sleep(5)

# 判断元素是否存在(等待加载完成后查找)
'''
# element = driver.find_element_by_id("")
locator = (By.CLASS_NAME,"element")
WebDriverWait(driver,1).until(EC.invisibility_of_element_located(locator))
'''
name = driver.find_element_by_id("user_login").send_keys('selenium_training')

#获取元素的属性的方法get_attribute，填入获取的属性名
pw = driver.find_element_by_id("user_password")
text = pw.get_attribute("placeholder")
print(text)
pw.send_keys("test123456")
# 获取输入的信息内容
print(pw.get_attribute("value"))

driver.find_element_by_css_selector("#new_user > div.session-login__body > div > div > div.two.fields > div:nth-child(1) > div").click()
driver.find_element_by_name("commit").click()




driver.close()


