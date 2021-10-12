import requests


class Test_request():

    def test_get_token(self):
        """获取token"""
        corpid = "ww15bace27683db2b6"  # 企业id
        corpsecret = "wh0y--u-w2mJcOkrtfVxxFwbsEXzW-DfmzIjdiflRQ4"  # 应用凭证秘钥
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        re = requests.get(url=url)
        return re.json()["access_token"]

    def test_create(self):
        """创建部门"""
        data = {
            "name": "中讯院成都研发中心",
            "parentid": 1,
            "name_en": "RDGZ",
            "order": 1,
        }
        re = requests.post(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.test_get_token()}", json=data)
        print(re.json())
        assert re.status_code==200

    def test_query(self):
        """查询部门列表"""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.test_get_token()}&id=1"
        re = requests.get(url)
        print(re.text)

    def test_update(self):
        """更新部门"""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.test_get_token()}"
        data = {
            "id": 2,
            "name": "中讯院成都研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        re = requests.post(url, json=data)
        print(re.json())

    def test_delete(self):
        """删除部门"""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.test_get_token()}&id=2"
        re = requests.get(url)
        print(re.json())
        assert re.json()["errmsg"]=='deleted'