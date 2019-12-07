import requests
import app


class EmpApi:
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
    def add_emp(self,username,mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-07-01",
            "formOfEmployment": 1,
            "workNumber": "1322131",
            "departmentName": "开发部",
            "departmentId": "1066240656856453120",
            "correctionTime": "2019-11-30"
        }
        return requests.post(self.emp_url,json=data,headers = app.headers)

    def query_emp(self):
        query_url = self.emp_url + "/" + app.emp_id
        return requests.get(query_url,headers = app.headers)

    def modify_emp(self,username):
        modify_emp_url = self.emp_url+"/" + app.emp_id
        return requests.put(modify_emp_url,json={"username":username},headers = app.headers)

    def delete_emp(self):
        delete_emp_url = self.emp_url + "/" + app.emp_id
        return requests.delete(delete_emp_url,headers=app.headers)