import requests

class HTTP:
    def get(self,url,return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else return ''
        return r.json() if return_json else  return r.text

        '''
        简化代码的写法：
        1.通过三元表达式
        2.巧妙的使用if+return
        3.提取成函数
        '''


        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''