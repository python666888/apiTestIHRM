import logging
import unittest
from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import read_login_data, assert_common


class TestIHRMLoginParameterized(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    @parameterized.expand(read_login_data())
    def test01_login_success(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile,password)
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self, response, http_code, success, code, message)

