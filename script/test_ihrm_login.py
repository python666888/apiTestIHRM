import logging
import unittest

import app
from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def test01_login_success(self):
        response = self.login_api.login("13800000002","123456")
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")
        jsonData = response.json()
        token = "Bearer " + jsonData.get('data')
        app.headers = {"Content-Type":"application/json","Authorization":token}
        logging.info("保存的请求头信息：{}".format(app.headers))


    def test02_mobile_error(self):
        response = self.login_api.login("13800000023","123456")
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self,response,200,False,20001,"用户名或密码错误")

    def test03_password_error(self):
        response = self.login_api.login("13800000002","223456")
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self,response,200,False,20001,"用户名或密码错误")

    def test04_none_params(self):
        response = self.login_api.login_none_params()
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙")

    def test05_mobile_empty(self):
        response = self.login_api.login("","error")
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self,response,200,False,20001,"用户名或密码错误")

    def test06_password_empty(self):
        response = self.login_api.login("13800000002","")
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self,response,200,False,20001,"用户名或密码错误")

    def test07_extra_params(self):
        response = self.login_api.login_extra_params()
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test08_less_params(self):
        response = self.login_api.login_less_params()
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self, response, 200, False, 99999, "抱歉，系统繁忙")