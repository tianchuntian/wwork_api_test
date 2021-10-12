import yaml


class AddData:
    def data(self, userid=None, name=None, mobile=None, dep=None, token=None, api_name=None):
        """拼装生成请求数据"""
        url_methods = yaml.safe_load(open('../case_datas/env.yaml', encoding='utf-8'))
        url_method = url_methods[api_name]
        # print(url_method)
        datas = {'method': url_method["method"],
                 'url': url_method['env']['test'],
                 'params': {'access_token': token,
                            'userid': userid},
                 'json':
                     {'userid': userid,
                      'name': name,
                      'mobile': mobile,
                      'department': dep}}

        return datas


if __name__ == '__main__':
    AddData().data()
