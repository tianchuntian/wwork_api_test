import yaml


def test_yaml():
    data = yaml.safe_load(open("../case_datas/env.yaml", encoding="utf-8"))
    # print(type(data))
    print(data["create"]["env"][data["create"]["default"]])


def test_dump_yaml():
    data={"create":{
                    "default":"test",
                    "env":{
                            "test":"https://qyapi.weixin.qq.com/cgi-bin/user/create",
                            "dev":"https://www.baidu.com"
        }
    }}
    with open("../case_datas/env.yaml","w",encoding='utf-8') as fp:
      yaml.safe_dump(data=data,stream=fp)


def test_get_token_yaml():
    data = yaml.safe_load(open("../case_datas/get_token.yaml", encoding="utf-8"))
    # print(type(data))
    print(data)