import requests
from test_requests.common.base_api import BaseApi
from test_requests.common.get_token import GetToken
from test_requests.common.add_data import AddData


class Address(BaseApi):
    # def __init__(self):
        # self.token = GetToken().get_token()

    def create(self, userid, name, mobile, dep,token):
        """创建用户"""
        datas = AddData().data(userid, name, mobile, dep, token=token, api_name="create")
        return self.send(datas)

    def get(self, userid,token):
        """读取成员"""
        data = AddData().data(userid=userid, token=token, api_name="get")
        return self.send(data)

    def update(self, userid, name,token):
        """修改成员"""
        data = AddData().data(userid=userid, name=name, token=token, api_name="update")
        return self.send(data)

    def delete(self, userid,token):
        """删除成员"""
        data = AddData().data(userid=userid, token=token, api_name="delete")
        return self.send(data)


if __name__ == '__main__':
    print(Address().get())
