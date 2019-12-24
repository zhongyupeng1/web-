# 1.导包
from selenium import webdriver
from time import sleep
from tools.Util import Utils
from selenium.webdriver.common.action_chains import ActionChains

class Goods_choose(Utils):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        driver=self.driver
        driver.get('http://127.0.0.1/iwebshop/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        sleep(1)
        action = ActionChains(driver)
        element1 = driver.find_element_by_class_name('allsort')
        action.move_to_element(element1).perform()
        sleep(1)
        element2 = driver.find_element_by_xpath('//*[@id="div_allsort"]/li[2]/h2')
        action.move_to_element(element2).perform()
        sleep(1)
        driver.find_element_by_link_text('纤体').click()

    def tearDown(self) -> None:
        # 暂停1秒后关闭浏览器
        sleep(1)
        self.driver.quit()

    def test_case1(self):
        #全部商品分类-商品筛选-选不限
        text=self.driver.find_element_by_class_name('p_name').text
        self.assert_equal(self.driver,text,'Clarins/娇韵诗 纤体精华霜第五代')

    def test_case2(self):
        #全部商品分类-商品筛选-选Clarins娇韵诗、法国
        driver = self.driver
        driver.find_element_by_id('brand_43').click()
        driver.find_element_by_id('attr_176_%E6%B3%95%E5%9B%BD').click()
        text=driver.find_element_by_class_name('p_name').text
        self.assert_equal(driver,text,'Clarins/娇韵诗 纤体精华霜第五代')

    def test_case3(self):
        #全部商品分类-商品筛选-选Clarins娇韵诗、英国、中性
        driver = self.driver
        driver.find_element_by_id('brand_43').click()
        driver.find_element_by_id('attr_176_%E8%8B%B1%E5%9B%BD').click()
        driver.find_element_by_id('attr_177_%E4%B8%AD%E6%80%A7').click()
        text=driver.find_element_by_class_name('gray').text
        self.assert_equal(driver,text,'对不起，没有找到相关商品')

    def test_case4(self):
        #全部商品分类-商品筛选-选不限、法国、敏感性、25岁以上
        driver = self.driver
        driver.find_element_by_id('attr_176_%E6%B3%95%E5%9B%BD').click()
        driver.find_element_by_id('attr_177_%E6%95%8F%E6%84%9F%E6%80%A7').click()
        driver.find_element_by_id('attr_178_25%E5%B2%81%E4%BB%A5%E4%B8%8A').click()
        text=driver.find_element_by_class_name('gray').text
        self.assert_equal(driver,text,'对不起，没有找到相关商品')

    def test_case5(self):
        #全部商品分类-商品筛选-选Clarins娇韵诗、法国、中性、25岁以上、乳液状
        driver = self.driver
        driver.find_element_by_id('brand_43').click()
        driver.find_element_by_id('attr_176_%E6%B3%95%E5%9B%BD').click()
        driver.find_element_by_id('attr_177_%E4%B8%AD%E6%80%A7').click()
        driver.find_element_by_id('attr_178_25%E5%B2%81%E4%BB%A5%E4%B8%8A').click()
        driver.find_element_by_id('attr_179_%E4%B9%B3%E6%B6%B2%E7%8A%B6').click()
        text=driver.find_element_by_class_name('gray').text
        self.assert_equal(driver,text,'对不起，没有找到相关商品')

    def test_case6(self):
        # 全部商品分类-商品筛选-选Clarins娇韵诗、法国、中性、25岁以上、乳液状、防晒
        driver = self.driver
        driver.find_element_by_id('brand_43').click()
        driver.find_element_by_id('attr_176_%E6%B3%95%E5%9B%BD').click()
        driver.find_element_by_id('attr_177_%E4%B8%AD%E6%80%A7').click()
        driver.find_element_by_id('attr_178_25%E5%B2%81%E4%BB%A5%E4%B8%8A').click()
        driver.find_element_by_id('attr_179_%E4%B9%B3%E6%B6%B2%E7%8A%B6').click()
        driver.find_element_by_id('attr_180_%E9%98%B2%E6%99%92').click()
        text = driver.find_element_by_class_name('gray').text
        self.assert_equal(driver, text, '对不起，没有找到相关商品')

    def test_case7(self):
        # 全部商品分类-商品筛选-选Clarins娇韵诗、法国、敏感性、25岁以上、乳液状、防晒、1-399
        driver = self.driver
        driver.find_element_by_id('brand_43').click()
        driver.find_element_by_id('attr_176_%E6%B3%95%E5%9B%BD').click()
        driver.find_element_by_id('attr_177_%E6%95%8F%E6%84%9F%E6%80%A7').click()
        driver.find_element_by_id('attr_178_25%E5%B2%81%E4%BB%A5%E4%B8%8A').click()
        driver.find_element_by_id('attr_179_%E4%B9%B3%E6%B6%B2%E7%8A%B6').click()
        driver.find_element_by_id('attr_180_%E9%98%B2%E6%99%92').click()
        driver.find_element_by_id('1-399').click()
        text = driver.find_element_by_class_name('gray').text
        self.assert_equal(driver, text, '对不起，没有找到相关商品')

    def test_case8(self):
        # 全部商品分类-商品筛选-价格输入99-499
        driver = self.driver
        driver.find_element_by_name('min_price').send_keys('99')
        driver.find_element_by_name('max_price').send_keys('499')
        driver.find_element_by_class_name('btn_gray_s').click()
        text = driver.find_element_by_class_name('p_name').text
        self.assert_equal(driver, text, 'Clarins/娇韵诗 纤体精华霜第五代')




