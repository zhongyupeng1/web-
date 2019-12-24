import unittest,time
# from case.backstage import Back_stage
# from case.goods_choose import Goods_choose
# from case.login import Login
# from case.registered import Registered
# from case.scene import Scene
from tools.HTMLTestRunner import HTMLTestRunner

discover=unittest.defaultTestLoader.discover('./case/',pattern='*.py')
nowtime=time.strftime('%Y_%m_%d_%H_%M_%S')
report_name='./Report/'+nowtime+'_report.html'
with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='Web测试用例执行结果',description='操作系统:Windows 7       集成环境:XAMPP python+selenium')
    runner.run(discover)