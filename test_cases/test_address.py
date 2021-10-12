from test_requests.api.address import Address
import pytest
import yaml

from test_requests.common.get_token import GetToken


class TestAddress():
    def setup_class(self):
        "实例化,在这个测试类中，只调用一次获取token的方法，提升脚本性能 "
        self.address = Address()
        self.token = GetToken().get_token()

    @pytest.mark.parametrize("dict1", yaml.safe_load(open("../case_datas/create.yaml", encoding="utf-8")))
    @pytest.mark.run(order=1)
    def test_create(self, dict1):
        """测试create这个api的用例"""
        "判断，如果该用户是否已经存在，如果存在，删除"
        if self.address.get(userid=dict1["userid"], token=self.token)["errcode"] == 0:
            self.address.delete(userid=dict1["userid"], token=self.token)
        assert self.address.create(userid=dict1["userid"], name=dict1["name"],
                                   mobile=dict1["mobile"], dep=dict1["department"], token=self.token)["errcode"] == 0

    @pytest.mark.parametrize("dict1", yaml.safe_load(open("../case_datas/get.yaml", encoding='utf-8')))
    @pytest.mark.run(order=2)
    def test_get(self, dict1):
        "测试get这个api的用例"
        assert self.address.get(userid=dict1["userid"], token=self.token)["userid"] == dict1["userid"]

    @pytest.mark.parametrize("dict1", yaml.safe_load(open("../case_datas/update.yaml", encoding="utf-8")))
    @pytest.mark.run(order=3)
    def test_update(self, dict1):
        "测试update这个api的用例"
        assert self.address.update(userid=dict1["userid"], name=dict1["name"], token=self.token)["errcode"] == 0

    @pytest.mark.parametrize("dict1", yaml.safe_load(open("../case_datas/get.yaml", encoding='utf-8')))
    @pytest.mark.run(order=4)
    def test_get(self, dict1):
        "测试get这个api的用例"
        assert self.address.get(userid=dict1["userid"], token=self.token)["userid"] == dict1["userid"]

    @pytest.mark.parametrize("dict1", yaml.safe_load(open('../case_datas/delete.yaml', encoding="utf-8")))
    @pytest.mark.run(order=5)
    def test_delete(self, dict1):
        "测试delete这个api的用例"
        assert self.address.delete(userid=dict1["userid"], token=self.token)["errcode"] == 0


