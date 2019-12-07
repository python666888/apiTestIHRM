import time,unittest,app
from report.HTMLTestRunner import HTMLTestRunner
from script.test_ihrm_login import TestIHRMLogin
from script.test_ihrm_emp_params import TestEmp


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestEmp))


report_path = app.base_dir + "/report/ihrm{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_path,mode="wb")as f:
    runner = HTMLTestRunner(stream=f,title="人力资源紫铜测试报告",description="基于某某生成的报告")
    runner.run(suite)