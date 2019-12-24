import unittest
import time
import os

class Utils(unittest.TestCase):

    #断言方法，判断实际结果与预期结果是否相等，不等则报错信息并截图
    def assert_equal(self,driver,actual_result,expected_result):
        nowtime=time.strftime('%Y_%m_%d_%H_%M_%S')
        wenjianjia=time.strftime('%Y_%m_%d')
        run_methodName=self._testMethodName
        try:
            self.assertEqual(actual_result,expected_result)
        except AssertionError:
            try:
                os.mkdir('../images/%s' %(wenjianjia))
            except:
                pass
            driver.get_screenshot_as_file('../images/%s/%s_%s.jpg' %(wenjianjia,run_methodName,nowtime))
            raise

    # 断言方法，验证arg1是arg2的子串，不是则报错信息并截图
    def assert_in(self,driver,actual_result,expected_result):
        nowtime=time.strftime('%Y_%m_%d_%H_%M_%S')
        wenjianjia=time.strftime('%Y_%m_%d')
        run_methodName=self._testMethodName
        try:
            self.assertIn(actual_result,expected_result)
        except AssertionError:
            try:
                os.mkdir('../images/%s' %(wenjianjia))
            except:
                pass
            driver.get_screenshot_as_file('../images/%s/%s_%s.jpg' %(wenjianjia,run_methodName,nowtime))
            raise
