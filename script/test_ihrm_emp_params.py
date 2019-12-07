import logging
import unittest
from parameterized import parameterized
import app
from api.emp_api import EmpApi
from utils import read_add_emp_data, assert_common, read_modify_emp_data, DButils, read_delete_emp_data


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self,username,mobile,http_code,success,code,message):
        response = self.emp_api.add_emp(username,mobile)
        logging.info("添加结果：{}".format(response.json()))
        assert_common(self,response,http_code,success,code,message)
        #保存员工id
        jsonData = response.json()
        emp_id = jsonData.get('data').get('id')
        app.emp_id = emp_id
        logging.info("保存的员工id：{}".format(app.emp_id))

    @parameterized.expand(read_add_emp_data)
    def test02_mobile_error(self,http_code,success,code,message):
        response = self.emp_api.query_emp()
        logging.info("登陆接口返回数据：{}".format(response.json()))
        assert_common(self, response, http_code, success, code,message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self,username,http_code,success,code,message):
        response = self.emp_api.modify_emp(username)
        logging.info("修改后数据为：{}".format(response.json()))
        assert_common(self, response, http_code, success, code,message)

        with DButils("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm")as db:
            query_sql = "select username from bs_user where id={} limit 1".format(app.emp_id)
            db.execute(query_sql)
            result = db.fetchone()
        logging.info("------查询数据库中员工id{}的username是{}".format(app.emp_id, result[0]))
        self.assertEqual(username, result[0])


    @parameterized.expand(read_delete_emp_data)
    def test04_delete_emp(self,http_code,success,code,message):
        response = self.emp_api.delete_emp()
        logging.info("删除员工返回数据为：{}".format(response.json()))
        assert_common(self, response, http_code, success, code, message)
