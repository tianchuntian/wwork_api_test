import pytest
import requests
from filelock import FileLock


@pytest.fixture(scope="session")
def test_get_token():
    """获取access_token"""
    # re=None
    # while FileLock('session.lock'):
    corpid = "ww15bace27683db2b6"  # 企业id
    corpsecret = "wh0y--u-w2mJcOkrtfVxxOV-88sU5bEG8ES38yOzGGs"  # 应用凭证秘钥
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    re = requests.get(url=url)
    print('get_token')
    # print(re.json()["access_token"])
    return re.json()["access_token"]


def test_create(userid, name, mobile, dep, test_get_token):
    """创建用户"""
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token}"
    data = {"userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [dep]}
    re = requests.post(url, json=data)
    # print(re.json())
    return re.json()


def test_get(test_get_token, userid):
    """读取成员"""
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token}&userid={userid}'
    re = requests.get(url)
    # print(re.json())
    return re.json()


def test_update(test_get_token, userid, name):
    """修改成员"""
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_token}'
    data = {"userid": userid,
            "name": name}
    re = requests.post(url, json=data)
    return re.json()["errcode"]


def test_delete(test_get_token, userid):
    """删除成员"""
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token}&userid={userid}'
    re = requests.get(url)
    # print(re.json())
    return re.json()["errcode"]


def test_create_data():
    """制造测试数据"""
    data = [("zhangsan" + str(i + 1), "张三" + str(i + 1), "138%08d" % (i + 1), 1, "李四" + str(i + 1)) for i in range(20)]
    return data


@pytest.mark.parametrize("userid,name,mobile,dep,name2", test_create_data())
def test_all(userid, name, mobile, dep, name2, test_get_token):
    """创建成员之前先判断该成员是否已存在，如果存在，先删除该成员"""
    if test_get(test_get_token, userid)["errcode"] == 0:
        print("存在该成员，现已删除！")
        test_delete(test_get_token, userid)
    """创建成员"""
    assert test_create(userid, name, mobile, dep, test_get_token)["errcode"] == 0
    """查询创建成员"""
    assert userid == test_get(test_get_token, userid)["userid"]
    """修改成员"""
    assert 0 == test_update(test_get_token, userid, name2)
    """查询修改后的成员"""
    assert userid == test_get(test_get_token, userid)["userid"]
    """删除成员"""
    assert 0 == test_delete(test_get_token, userid)
    """查询删除后的成员"""
    assert "userid not found" in test_get(test_get_token, userid)["errmsg"]
