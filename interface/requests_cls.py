
import requests

class RequestsInterface(object):

    def get(self,**kwargs):

        '''封装get方法'''

        params = kwargs.get('params')
        headers = kwargs.get('headers')
        url = kwargs.get('url')
        try:
            result = requests.get(url=url,headers=headers,params=params).json()
            return result
        except Exception as e:
            print('get请求错误{}'.format(e))

    def post(self,url,**kwargs):

        '''封装post方法'''

        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        files = kwargs.get("files")
        try:
            result = requests.post(url, params=params, data=data, json=json, files=files).json()
            return result
        except Exception as e:
            print("post请求错误: %s" % e)
