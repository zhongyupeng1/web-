# 1.导包
from selenium import webdriver
from time import sleep
from tools.Util import Utils
from selenium.webdriver.support.select import Select

class Back_stage(Utils):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('http://127.0.0.1/iwebshop/index.php?controller=systemadmin&action=index')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        # 暂停1秒后关闭浏览器
        sleep(1)
        self.driver.quit()

    def test_case7(self):
        # 后台管理登录输入管理员正确的用户名及密码时登录功能正确性验证
        driver = self.driver
        driver.find_element_by_name('admin_name').send_keys('admin')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit').click()

    def test_case1(self):
        # 用管理员身份进入后台，点击会员，进行操作
        driver = self.driver
        #调用test_case7()函数，进行后台登录
        self.test_case7()
        driver.find_element_by_link_text('会员').click()
        driver.find_element_by_class_name('operating_btn').click()
        driver.find_element_by_name('user_name').send_keys('world')
        driver.find_element_by_name('email').send_keys('638787265@qq.com')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_name('repassword').send_keys('123456')
        driver.find_element_by_name('truename').send_keys('嗯哼')
        driver.find_element_by_name('telephone').send_keys('15897265516')
        element1 = driver.find_element_by_id('province')
        select1 = Select(element1)
        select1.select_by_visible_text('广东')
        sleep(2)
        element2 = driver.find_element_by_id('city')
        select2 = Select(element2)
        select2.select_by_visible_text('广州市')
        sleep(2)
        element3 = driver.find_element_by_id('area')
        select3 = Select(element3)
        select3.select_by_visible_text('白云区')
        driver.find_element_by_name('address').send_keys('海滨路83号')
        driver.find_element_by_name('zip').send_keys('510080')
        driver.find_element_by_name('qq').send_keys('687276127')
        driver.find_element_by_name('msn').send_keys('6767')
        driver.find_element_by_name('exp').send_keys('35')
        driver.find_element_by_name('point').send_keys('35')
        driver.find_element_by_class_name('submit').click()

    def test_case2(self):
        # 后台登录-会员-会员列表操作-回收站操作
        driver = self.driver
        self.test_case7()
        driver.find_element_by_link_text('会员').click()
        #会员列表操作
        driver.find_element_by_xpath('//*[@id="list_table"]/tbody/tr[1]/td[1]/input').click()
        driver.find_element_by_xpath('//*[@id="list_table"]/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_class_name('delete').click()
        sleep(1)
        driver.find_element_by_id('artPlusConfirmyes').click()
        driver.find_element_by_class_name('sel_all').click()
        driver.find_element_by_class_name('delete').click()
        sleep(1)
        driver.find_element_by_id('artPlusConfirmyes').click()
        #回收站
        driver.find_element_by_class_name('recycle').click()
        driver.find_element_by_class_name('sel_all').click()
        driver.find_element_by_class_name('recover').click()
        sleep(1)
        driver.find_element_by_id('artPlusConfirmyes').click()
        driver.find_element_by_class_name('sel_all').click()
        driver.find_element_by_class_name('delete').click()
        # 永久删除后刷新页面，转到会员列表
        sleep(1)
        driver.find_element_by_id('artPlusConfirmyes').click()

    def test_case3(self):
        # 用管理员身份进入后台，点击会员，筛选商品
        driver = self.driver
        self.test_case7()
        driver.find_element_by_link_text('会员').click()
        driver.find_element_by_class_name('remove').click()
        sleep(1)
        eleme1 = driver.find_element_by_name('requirement')
        sele1 = Select(eleme1)
        sele1.select_by_visible_text('用户名')
        sleep(1)
        eleme2 = driver.find_element_by_name('username_key')
        sele2 = Select(eleme2)
        sele2.select_by_visible_text('包含')
        sleep(1)
        driver.find_element_by_name('username_value').send_keys('zhong')
        sleep(1)
        driver.find_element_by_id('filteryes').click()
        text=driver.find_element_by_xpath('//*[@id="list_table"]/tbody/tr[1]/td[2]').text
        self.assert_in(driver,'zhong',text)

    def test_case4(self):
        # 用管理员身份进入后台，点击会员，根据 Email搜索商品
        driver = self.driver
        self.test_case7()
        sleep(1)
        driver.find_element_by_link_text('会员').click()
        sleep(1)
        eleme1 = driver.find_element_by_class_name('normal')
        sele1 = Select(eleme1)
        sele1.select_by_visible_text('Email')
        driver.find_element_by_class_name('small').send_keys('@163.com')
        driver.find_element_by_class_name('btn').click()
        sleep(1)
        #找出列表的所有email，进行循环判断
        emails = driver.find_elements_by_xpath('//*[@id="list_table"]/tbody/tr')
        for i in range(1, len(emails) + 1):
            email='//*[@id="list_table"]/tbody/tr['+str(i)+']/td[6]'
            email_name = driver.find_element_by_xpath(email).text
            self.assert_in(driver, '@163.com', email_name)

    def test_case5(self):
        # 用管理员身份进入后台，点击商品，筛选商品
        driver = self.driver
        self.test_case7()
        driver.find_element_by_link_text('商品').click()
        sleep(1)
        eleme1 = driver.find_element_by_name('category_id')
        sele1 = Select(eleme1)
        sele1.select_by_visible_text('平板电脑')
        sleep(1)
        eleme2 = driver.find_element_by_name('added')
        sele2 = Select(eleme2)
        sele2.select_by_visible_text('上架')
        sleep(1)
        eleme3 = driver.find_element_by_name('store_nums')
        sele3 = Select(eleme3)
        sele3.select_by_visible_text('10-100')
        sleep(1)
        eleme4 = driver.find_element_by_name('commend')
        sele4 = Select(eleme4)
        sele4.select_by_visible_text('最新商品')
        sleep(1)
        driver.find_element_by_class_name('sel').click()
        text = driver.find_element_by_xpath('//*[@id="list_table"]/tbody/tr[1]/td[3]').text
        self.assert_equal(driver, '平板电脑', text)

    def test_case6(self):
        # 用管理员身份进入后台，点击商品，添加商品
        driver = self.driver
        self.test_case7()
        driver.find_element_by_link_text('商品').click()
        sleep(1)
        driver.find_element_by_class_name('addition').click()
        driver.find_element_by_id('goods_name').send_keys('李宁跑鞋')
        sleep(1)
        driver.find_element_by_xpath('//input[@value="57"]').click()
        # 排序清空输入1
        userA = driver.find_element_by_id('sort')
        userA.clear()
        userA.send_keys('1')
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(1)
        text = driver.find_element_by_xpath('//*[@id="list_table"]/tbody/tr[1]/td[3]').text
        self.assert_equal(driver, '服饰鞋帽', text)


