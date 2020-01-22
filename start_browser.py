#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random
import string
from itertools import product

# 参考：https://www.cnblogs.com/tobecrazy/p/4570494.html
driver = webdriver.Chrome()

driver.get("https://gitee.com/login")
time.sleep(5)

# 基础方法
#获取邮箱方法:namenum(邮箱名字的位数)，mailcount(邮箱的个数)
def make_email(namenum,mailcount):
    email = []
    data = string.ascii_letters+string.digits #字母和数字,特殊字符 string.ascii_lowercase、string.punctuation、string.ascii_uppercase
    email_type = random.choice(('@163.com', '@qq.com', '@sina.com', '@126.com'))
    for i in range(mailcount):
        data = random.sample(data, namenum)
        email_start = ''.join(data)
        email.append(email_start+email_type)
    return email

make_email(5,3)

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


