import pymysql,json
from requests import Response

import app


def assert_common(self, response, http_code, success, code, message):
    '''
   @type=response:Response
    '''

    jsonData = response.json()
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertIn(message,jsonData.get("message"))

class DButils:
    def __init__(self,host,user,password,database):
        self.conn = pymysql.connect(host,user,password,database)
        ##enter 和 exit是内置魔法方法，当进入with时候进入enter,关闭时候exit
    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

def read_login_data():
    login_data_path = app.base_dir + "/data/login_data.json"
    with open(login_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            http_code = login_data.get("http_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            result_list.append((mobile, password, http_code, success, code, message))
    print("result_list的值为：", result_list)
    return result_list


def read_add_emp_data():
    emp_data_path = app.base_dir + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username,mobile,http_code,success,code,message))
    print("新增数据列表为：",result_list)
    return result_list

def read_query_emp_data():
    emp_data_path = app.base_dir + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        username = query_emp_data.get("username")
        mobile = query_emp_data.get("mobile")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))
    print("新增数据列表为：", result_list)
    return result_list

def read_modify_emp_data():
    emp_data_path = app.base_dir + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("username")
        http_code = modify_emp_data.get("http_code")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        result_list.append((username, http_code, success, code, message))
    print("新增数据列表为：", result_list)
    return result_list

def read_delete_emp_data():
    emp_data_path = app.base_dir + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        deletete_emp_data = jsonData.get("delete_emp")
        username = deletete_emp_data.get("username")
        http_code = deletete_emp_data.get("http_code")
        success = deletete_emp_data.get("success")
        code = deletete_emp_data.get("code")
        message = deletete_emp_data.get("message")
        result_list.append((username, http_code, success, code, message))
    print("新增数据列表为：", result_list)
    return result_list
