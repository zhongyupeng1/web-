# 1.导包
from selenium import webdriver
from time import sleep
from tools.Util import Utils
from selenium.webdriver.support.select import Select
import random

class Scene(Utils):

    def setUp(self) -> None:
        driver = webdriver.Firefox()
        self.driver=driver

    def tearDown(self) -> None:
        # 暂停1秒后关闭浏览器
        sleep(1)
        self.driver.quit()

    def test_case1(self):
        # 注册-登陆-首页-搜索商品-筛选商品-查看商品详情-立即购买-结算-提交订单成功-查看订单-退出
        self.driver.get('http://127.0.0.1/iwebshop/index.php?controller=simple&action=reg')
        self.driver.maximize_window()
        driver = self.driver
        self.driver.implicitly_wait(10)
        # 注册    设置随机邮箱、用户名、密码、重复密码
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
        text = driver.find_element_by_class_name('f14').text
        self.assert_equal(driver, text, '恭喜，操作成功！')
        # 退出后登陆
        driver.find_element_by_class_name('reg').click()
        driver.find_element_by_name('login_info').send_keys(user_name)
        driver.find_element_by_name('password').send_keys(mima)
        driver.find_element_by_class_name('submit_login').click()
        text = driver.find_element_by_class_name('loginfo').text
        self.assert_equal(driver, text, '%s您好，欢迎您来到iwebshop购物！[安全退出]' %user_name)
        # 首页
        driver.find_element_by_link_text('iwebshop').click()
        # 搜索商品
        driver.find_element_by_id('word').send_keys('男装')
        driver.find_element_by_class_name('btn').click()
        driver.find_element_by_xpath('//*[@class="display_list clearfix m_10"]/li/div/a').click()
        # 立即购买
        driver.find_element_by_id('buy_now').click()
        driver.find_element_by_xpath('//*[@id="4ea88dca0cb8f7aed6922cd01d25de11"]/img').click()
        sleep(1.5)
        driver.find_element_by_id('d20caec3b48a1eef164cb4ca81ba2587').click()
        sleep(1.5)
        js = "window.scrollTo(0,350)"
        driver.execute_script(js)
        sleep(1)
        driver.find_element_by_id('buy_now').click()
        # 核对订单信息
        driver.find_element_by_name('accept_name').send_keys('zhong')
        element1 = driver.find_element_by_id('province')
        select1 = Select(element1)
        select1.select_by_visible_text('广东')
        element2 = driver.find_element_by_id('city')
        select2 = Select(element2)
        select2.select_by_visible_text('广州市')
        element3 = driver.find_element_by_id('area')
        select3 = Select(element3)
        select3.select_by_visible_text('番禺区')
        driver.find_element_by_name('address').send_keys('海大路一号')
        driver.find_element_by_name('mobile').send_keys('15914901111')
        driver.find_element_by_name('zip').send_keys('213232')
        driver.find_element_by_xpath('//*[@id="address_save_button"]/input').click()
        # 配送方式（第二次不用再选）
        js = "window.scrollTo(0,500)"
        driver.execute_script(js)
        sleep(1)
        driver.find_element_by_id('delivery1').click()
        driver.find_element_by_id('delivery_save_button').click()
        driver.find_element_by_class_name('submit_order').click()
        # 提交订单成功
        text = driver.find_element_by_class_name('f14').text
        self.assert_equal(driver, text, '订单已提交')
        # 查看订单
        driver.find_element_by_class_name('f_r').click()
        sleep(1)
        js = "window.scrollTo(0,800)"
        driver.execute_script(js)
        sleep(1)
        js1 = "window.scrollTo(0,0)"
        driver.execute_script(js1)
        # 安全退出,到登录页面
        driver.find_element_by_class_name('reg').click()
        current_url = driver.current_url
        current_url = current_url.split('&')
        self.assert_equal(driver, current_url[-1], 'action=login')

    def test_case2(self):
        #登陆-首页-搜索商品-筛选商品-查看商品详情-立即购买-结算-提交订单成功-查看订单-退出
        driver=self.driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #登陆
        self.driver.get('http://127.0.0.1/iwebshop/index.php?controller=simple&action=login')
        driver.find_element_by_name('login_info').send_keys('dkasd')
        driver.find_element_by_name('password').send_keys('938475413')
        driver.find_element_by_class_name('submit_login').click()
        text=driver.find_element_by_class_name('loginfo').text
        self.assert_equal(driver,text,'dkasd您好，欢迎您来到iwebshop购物！[安全退出]')
        #首页
        driver.find_element_by_link_text('iwebshop').click()
        #搜索商品
        driver.find_element_by_id('word').send_keys('男装')
        driver.find_element_by_class_name('btn').click()
        driver.find_element_by_xpath('//*[@class="display_list clearfix m_10"]/li/div/a').click()
        #立即购买
        driver.find_element_by_id('buy_now').click()
        driver.find_element_by_xpath('//*[@id="4ea88dca0cb8f7aed6922cd01d25de11"]/img').click()
        sleep(1.5)
        driver.find_element_by_id('d20caec3b48a1eef164cb4ca81ba2587').click()
        sleep(1.5)
        driver.find_element_by_id('buy_now').click()
        #核对订单信息
        driver.find_element_by_name('accept_name').send_keys('zhong')
        element1=driver.find_element_by_id('province')
        select1=Select(element1)
        select1.select_by_visible_text('广东')
        element2=driver.find_element_by_id('city')
        select2 = Select(element2)
        select2.select_by_visible_text('广州市')
        element3 = driver.find_element_by_id('area')
        select3 = Select(element3)
        select3.select_by_visible_text('番禺区')
        driver.find_element_by_name('address').send_keys('海大路一号')
        driver.find_element_by_name('mobile').send_keys('15914901111')
        driver.find_element_by_name('zip').send_keys('213232')
        driver.find_element_by_xpath('//*[@id="address_save_button"]/input').click()
        #配送方式（第二次不用再选）
        # driver.find_element_by_id('delivery1').click()
        # driver.find_element_by_id('delivery_save_button').click()
        driver.find_element_by_class_name('submit_order').click()
        #提交订单成功
        text = driver.find_element_by_class_name('f14').text
        self.assert_equal(driver,text,'订单已提交')
        # 查看订单
        driver.find_element_by_class_name('f_r').click()
        sleep(1)
        js = "window.scrollTo(0,800)"
        driver.execute_script(js)
        sleep(1)
        js1 = "window.scrollTo(0,0)"
        driver.execute_script(js1)
        #安全退出,到登录页面
        driver.find_element_by_class_name('reg').click()
        current_url=driver.current_url
        current_url=current_url.split('&')
        self.assert_equal(driver,current_url[-1],'action=login')

    def test_case3(self):
#登录-修改账户信息-搜索商品-筛选商品-查看商品详情-加入购物车-进入购物车-结算--提交订单-取消订单-退出
        driver=self.driver
        #登陆
        self.driver.get('http://127.0.0.1/iwebshop/index.php?controller=simple&action=login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        driver.find_element_by_name('login_info').send_keys('讉凉槒昘貐')
        driver.find_element_by_name('password').send_keys('89005005')
        driver.find_element_by_class_name('submit_login').click()
        #修改账户信息：个人资料(第一次填写个人资料，第二次才修改)
        js = "window.scrollTo(0,250)"
        driver.execute_script(js)
        sleep(1)
        driver.find_element_by_link_text('个人资料').click()
        js = "window.scrollTo(0,350)"
        driver.execute_script(js)
        sleep(1)
        driver.find_element_by_name('true_name').clear()
        sleep(1)
        driver.find_element_by_name('true_name').send_keys('钟小明')
        sleep(1)
        elem1=driver.find_element_by_name('year')
        select1=Select(elem1)
        select1.select_by_visible_text('2007')
        elem2=driver.find_element_by_name('month')
        select2=Select(elem2)
        select2.select_by_visible_text('09')
        elem3 = driver.find_element_by_name('day')
        select3 = Select(elem3)
        select3.select_by_visible_text('28')
        eleme1 = driver.find_element_by_id('province')
        sele1 = Select(eleme1)
        sele1.select_by_visible_text('上海')
        sleep(2)
        eleme2 = driver.find_element_by_id('city')
        sele2 = Select(eleme2)
        sele2.select_by_visible_text('上海市')
        sleep(2)
        eleme3 = driver.find_element_by_name('area')
        sele3 = Select(eleme3)
        sele3.select_by_visible_text('黄浦区')
        sleep(2)
        driver.find_element_by_name('contact_addr').clear()
        sleep(1)
        driver.find_element_by_name('contact_addr').send_keys('林路8号')
        sleep(1)
        driver.find_element_by_name('zip').clear()
        sleep(1)
        driver.find_element_by_name('zip').send_keys('745932')
        sleep(1)
        driver.find_element_by_name('mobile').clear()
        sleep(1)
        driver.find_element_by_name('mobile').send_keys('13420201283')
        driver.find_element_by_xpath('//*[@name="user_info"]/table/tbody/tr[11]/td/label/input').click()
        sleep(1)
        # #修改密码成功后刷新
        driver.find_element_by_link_text('修改密码').click()
        driver.find_element_by_name('fpassword').send_keys('89005005')
        driver.find_element_by_name('password').send_keys('89005005')
        driver.find_element_by_name('repassword').send_keys('89005005')
        driver.find_element_by_xpath('//*[@class="form_content"]/form/table/tbody/tr[4]/td/label[1]/input').click()
        #首页
        driver.find_element_by_link_text('iwebshop').click()
        # #搜索商品
        driver.find_element_by_id('word').send_keys('男装')
        driver.find_element_by_class_name('btn').click()
        driver.find_element_by_xpath('//*[@class="display_list clearfix m_10"]/li/div/a').click()
        # 加入购物车
        driver.find_element_by_id('join_car').click()
        driver.find_element_by_xpath('//*[@id="4ea88dca0cb8f7aed6922cd01d25de11"]/img').click()
        sleep(1.5)
        driver.find_element_by_id('d20caec3b48a1eef164cb4ca81ba2587').click()
        sleep(1.5)
        js = "window.scrollTo(0,200)"
        driver.execute_script(js)
        sleep(1)
        driver.find_element_by_id('join_car').click()
        # 进入购物车-结算
        driver.find_element_by_link_text('进入购物车').click()
        driver.find_element_by_link_text('去结算').click()
        #提交订单
        driver.find_element_by_name('accept_name').send_keys('zhong')
        element1=driver.find_element_by_id('province')
        select1=Select(element1)
        select1.select_by_visible_text('广东')
        element2=driver.find_element_by_id('city')
        select2 = Select(element2)
        select2.select_by_visible_text('广州市')
        element3 = driver.find_element_by_id('area')
        select3 = Select(element3)
        select3.select_by_visible_text('番禺区')
        driver.find_element_by_name('address').send_keys('海大路一号')
        driver.find_element_by_name('mobile').send_keys('15914901111')
        driver.find_element_by_name('zip').send_keys('213232')
        driver.find_element_by_xpath('//*[@id="address_save_button"]/input').click()
        driver.find_element_by_class_name('submit_order').click()
        text = driver.find_element_by_class_name('f14').text
        self.assert_equal(driver,text,'订单已提交')
        # 取消订单
        driver.find_element_by_class_name('f_r').click()
        driver.find_element_by_xpath('//*[@class="btn_orange"]/input[2]').click()
        text=driver.find_element_by_class_name('green').text
        self.assert_equal(driver,text,'已取消')
        # 安全退出,到登录页面
        driver.find_element_by_class_name('reg').click()
        current_url=driver.current_url
        current_url=current_url.split('&')
        self.assert_equal(driver,current_url[-1],'action=login')

    def test_case4(self):
        # 后台登录-商品-会员-订单-营销-统计-系统-工具
        driver=self.driver
        driver.get('http://127.0.0.1/iwebshop/index.php?controller=systemadmin&action=index')
        driver.maximize_window()
        driver.implicitly_wait(10)
        #后台登陆
        driver.find_element_by_name('admin_name').send_keys('admin')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit').click()
        #商品-会员-订单-营销-统计-系统-工具
        driver.find_element_by_link_text('商品').click()
        driver.find_element_by_link_text('会员').click()
        driver.find_element_by_link_text('订单').click()
        driver.find_element_by_link_text('营销').click()
        driver.find_element_by_link_text('统计').click()
        driver.find_element_by_link_text('系统').click()
        driver.find_element_by_link_text('工具').click()

    def test_case5(self):
        # 后台登录-订单-查看订单-添加订单-发货,支付,完成-查看订单状态
        driver=self.driver
        driver.get('http://127.0.0.1/iwebshop/index.php?controller=systemadmin&action=index')
        driver.maximize_window()
        driver.implicitly_wait(10)
        #后台登陆
        driver.find_element_by_name('admin_name').send_keys('admin')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_name('captcha').send_keys('123456')
        driver.find_element_by_class_name('submit').click()
        #添加订单
        driver.find_element_by_link_text('订单').click()
        driver.find_element_by_class_name('addition').click()
        driver.find_element_by_id('user_name').click()
        sleep(2)
        # 切换表单  (div嵌套iframe,确定按钮要恢复默认页面操作)
        xf1 = driver.find_element_by_xpath('//*[@class="artPlusOpen"]')    #可用classname
        driver.switch_to.frame(xf1)
        driver.find_element_by_xpath('//*[@id="specs"]/div[1]/ul/li[4]/label').click()
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_id('alert_useryes').click()
        #添加订单商品
        driver.find_element_by_id('good_name').click()
        xf2 = driver.find_element_by_xpath('//*[@class="artPlusOpen"]')
        driver.switch_to.frame(xf2)
        driver.find_element_by_xpath('//*[@id="specs"]/div[1]/ul/li[3]/label').click()
        sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_id('alert_goodsyes').click()
        driver.find_element_by_class_name('submit').click()
        #订单信息保存
        driver.find_element_by_id('accept_name').send_keys('lsjfad')
        element1 = driver.find_element_by_id('province')
        select1=Select(element1)
        select1.select_by_visible_text('广东')
        element2=driver.find_element_by_id('city')
        select2 = Select(element2)
        select2.select_by_visible_text('广州市')
        element3 = driver.find_element_by_id('area')
        select3 = Select(element3)
        select3.select_by_visible_text('番禺区')
        driver.find_element_by_name('address').send_keys('海大路一号')
        driver.find_element_by_name('postcode').send_keys('213232')
        driver.find_element_by_name('mobile').send_keys('15914901111')
        driver.find_element_by_id('deli_id1').click()
        driver.find_element_by_id('deli_id1').click()
        driver.find_element_by_class_name('submit').click()
        #订单查看,发货,支付,完成
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/form/div[1]/table/tbody/tr[12]/td[11]/a[1]/img').click()
        driver.find_element_by_id('to_deliver').click()
        driver.find_element_by_id('deliveryes').click()
        sleep(2)
        driver.find_element_by_id('deliveryes').click()
        sleep(5)
        driver.find_element_by_id('to_pay').click()
        sleep(5)
        driver.find_element_by_id('payyes').click()
        sleep(5)
        driver.find_element_by_xpath('//div[@class="t_c"]/button[3]').click()
        sleep(3)
        driver.find_element_by_link_text('订单列表').click()
        text=driver.find_element_by_xpath('//div[@class="content"]/table/tbody/tr[12]/td[4]/b').text
        self.assert_equal(driver,text,'已付款')
        text = driver.find_element_by_xpath('//div[@class="content"]/table/tbody/tr[12]/td[5]/b').text
        self.assert_equal(driver, text, '已发货')

