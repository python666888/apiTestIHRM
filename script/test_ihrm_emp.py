import logging
import unittest

import app
from api.emp_api import EmpApi
from utils import assert_common, DButils


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emp_api = EmpApi()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def test01_add_emp(self):
        response = self.emp_api.add_emp("道光441","15095202122")
        logging.info("添加结果：{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")
        #保存员工id
        jsonData = response.json()
        emp_id = jsonData.get('data').get('id')
        app.emp_id = emp_id
        logging.info("保存的员工id：{}".format(app.emp_id))

    def test02_query_emp(self):
        response = self.emp_api.query_emp()
        logging.info("查询员工结果：{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")

    def test03_modify_emp(self):
        response = self.emp_api.modify_emp("宣统441")
        logging.info("修改后数据为：{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")

        with DButils("182.92.81.159","readuser","iHRM_user_2019","ihrm")as db:
            query_sql = "select username from bs_user where id={} limit 1".format(app.emp_id)
            logging.info("1234")
            db.execute(query_sql)
            logging.info("abcd")
            result = db.fetchone()
        logging.info("------查询数据库中员工id{}的username是{}".format(app.emp_id,result[0]))
        logging.info("9999")
        self.assertEqual("宣统441",result[0])

    def test04_delete_emp(self):
        response = self.emp_api.delete_emp()
        logging.info("删除员工返回数据为：{}".format(response.json()))
        assert_common(self, response, 200, True, 10000, "操作成功")
