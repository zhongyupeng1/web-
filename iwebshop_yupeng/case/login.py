# 1.导包
from selenium import webdriver
from time import sleep
from tools.Util import Utils
import random

class Login(Utils):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get('http://127.0.0.1/iwebshop/index.php?controller=simple&action=login')
        driver.maximize_window()
        driver.implicitly_wait(2)

    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

    def test_case1(self):
        #前台登录输入已注册过的邮箱及其密码时登录功能正确性验证
        driver = self.driver
        driver.find_element_by_name('login_info').send_keys('456456@163.com')
        driver.find_element_by_name('password').send_keys('12345678')
        driver.find_element_by_class_name('submit_login').click()
        text=driver.find_element_by_class_name('loginfo').text
        self.assert_equal(driver,text,'zhongyupen1您好，欢迎您来到iwebshop购物！[安全退出]')

    def test_case2(self):
        #前台登录输入已注册过的用户名及其密码时登录功能正确性验证
        driver=self.driver
        driver.find_element_by_name('login_info').send_keys('zhongyupen1')
        driver.find_element_by_name('password').send_keys('12345678')
        driver.find_element_by_class_name('submit_login').click()
        text=driver.find_element_by_class_name('loginfo').text
        self.assert_equal(driver,text,'zhongyupen1您好，欢迎您来到iwebshop购物！[安全退出]')

    def test_case3(self):
        #输入未注册的用户名和密码，登录失败
        driver = self.driver
        mima = str(random.random())[10:-1]
        suiji = random.randint(2, 8)
        user_name = ''
        for i in range(1, suiji + 1):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('login_info').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_class_name('submit_login').click()
        text = driver.find_element_by_class_name('prompt').text
        self.assert_equal(self.driver, text, '用户名和密码不匹配')



