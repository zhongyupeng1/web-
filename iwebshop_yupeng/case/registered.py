# 1.导包
from selenium import webdriver
from time import sleep
from tools.Util import Utils
import random

class Registered(Utils):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1/iwebshop/index.php?controller=simple&action=reg')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        # 暂停2秒后关闭浏览器
        sleep(2)
        self.driver.quit()

    def test_case1(self):
        #输入正确的邮箱、用户名、设置密码、确认密码及验证码时注册功能正确性验证
        driver=self.driver
        # 设置随机邮箱、用户名、密码、重复密码（邮箱@前是密码，方便好记）
        mima = str(random.random())[10:-1]
        list0 = [mima]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email = list0[0] + list1[random.randint(0, 3)] + list2[random.randint(0, 1)]
        suiji = random.randint(2, 8)
        user_name = ''
        for i in range(1, suiji + 1):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('username').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(mima)
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit_reg').click()
        text=driver.find_element_by_class_name('f14').text
        self.assert_equal(driver,text,'恭喜，操作成功！')

    def test_case2(self):
        #邮箱输入含特殊字符，其它输入正确时注册失败
        driver = self.driver
        # 设置随机用户名、密码、重复密码、万能验证码
        mima = str(random.random())[10:-1]
        suiji = random.randint(2, 8)
        user_name = ''
        for i in range(1, suiji + 1):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        yanzhengma = '123456'
        driver.find_element_by_name('email').send_keys('214*@￥#……***%￥85@qq.com')
        driver.find_element_by_name('username').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(mima)
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit_reg').click()
        text=driver.find_element_by_class_name('invalid-msg').text
        self.assert_equal(driver, text, '填写正确的邮箱格式')

    def test_case3(self):
        #用户名输入1个字符，其它输入正确时注册失败
        driver = self.driver
        # 设置随机邮箱、密码、重复密码
        mima = str(random.random())[10:-1]
        list0 = [mima]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email = list0[0] + list1[random.randint(0, 3)] + list2[random.randint(0, 1)]
        suiji = random.randint(2, 8)
        user_name = ''
        for i in range(1, suiji + 1):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('username').send_keys('q')
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(mima)
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit_reg').click()
        text = driver.find_element_by_xpath('//*[@class="form_table f_l"]/tbody/tr[2]/td/label').text
        self.assert_equal(driver, text, '填写2-20个字符，可以为字数，数字下划线和中文')

    def test_case4(self):
        #邮箱输入正确的10个字符，用户名输入正确的2个字符，设置密码输入正确的6个字符，其它输入正确时注册功能正确性验证
        driver = self.driver
        mima = str(random.random())[2:8]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email_hou = list1[random.randint(0, 3)] + list2[random.randint(0, 1)]
        str1 = str(random.random())[2:10 - len(email_hou) + 2]
        email = str1 + email_hou
        user_name = ''
        for i in range(1, 3):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('username').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(mima)
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit_reg').click()
        text=driver.find_element_by_class_name('f14').text
        self.assert_equal(driver,text,'恭喜，操作成功！')

    def test_case5(self):
        #邮箱输入正确的11个字符，用户名输入正确的3个字符，设置密码输入正确的7个字符，其它输入正确时注册功能正确性验证
        driver = self.driver
        mima = str(random.random())[2:9]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email_hou = list1[random.randint(0, 3)] + list2[random.randint(0, 1)]
        str1 = str(random.random())[2:11 - len(email_hou) + 2]
        email = str1 + email_hou
        user_name = ''
        for i in range(1, 4):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('username').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(mima)
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit_reg').click()
        text = driver.find_element_by_class_name('f14').text
        self.assert_equal(driver, text, '恭喜，操作成功！')

    def test_case6(self):
        #输入错误的密码，其他控件均正确时，注册失败
        driver = self.driver
        # 设置随机邮箱、用户名（邮箱@前是密码，方便好记）
        mima = str(random.random())[2:4]
        list0 = [mima]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email = list0[0] + list1[random.randint(0, 3)] + list2[random.randint(0, 1)]
        suiji = random.randint(2, 8)
        user_name = ''
        for i in range(1, suiji + 1):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('username').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(mima)
        driver.find_element_by_name('captcha').send_keys('123456')
        text = self.driver.find_element_by_xpath('//*[@class="form_table f_l"]/tbody/tr[3]/td/label').text
        self.assert_equal(self.driver, text, "填写6-32个字符")

    def test_case7(self):
        #确认密码与设置的密码不一致,注册失败
        driver = self.driver
        # 设置随机邮箱、用户名、密码、重复密码（邮箱@前是密码，方便好记）
        mima = str(random.random())[10:-1]
        remima = str(random.random())[10:-1]
        list0 = [mima]
        list1 = ['@qq', '@sina', '@163', '@263']
        list2 = ['.cn', '.com']
        email = list0[0] + list1[random.randint(0, 3)] + list2[random.randint(0, 1)]
        suiji = random.randint(2, 8)
        user_name = ''
        for i in range(1, suiji + 1):
            val = random.randint(0x4e00, 0x9fbf)
            user_name += chr(val)
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('username').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_name('repassword').send_keys(remima)
        driver.find_element_by_name('captcha').send_keys('123456')
        text = self.driver.find_element_by_xpath('//*[@class="form_table f_l"]/tbody/tr[4]/td/label').text
        self.assert_equal(self.driver, text, "两次输入密码不一致")

