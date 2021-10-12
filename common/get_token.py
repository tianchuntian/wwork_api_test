import yaml

from test_requests.common.base_api import BaseApi


class GetToken(BaseApi):
    """获取token"""

    def get_token(self):
        """获取access_token"""
        data = yaml.safe_load(open("../case_datas/get_token.yaml", encoding='utf-8'))
        re = self.send(data)
        print(re["access_token"])
        return re["access_token"]


if __name__ == '__main__':
    print(GetToken().get_token())
