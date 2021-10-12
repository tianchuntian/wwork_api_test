import requests


class BaseApi:
    """封装基本公共方法"""

    def send(self, data):
        """发送请求"""
        return requests.request(**data).json()
