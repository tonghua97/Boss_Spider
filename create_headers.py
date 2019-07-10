import pandas as pd
import random


class Simple_structure(object):
    def __init__(self, URL_data):
        # 1.将数据设置成字符串,并传入参数
        self.URL_data = URL_data

    @property
    def Structural_data(self):
        # 2.使用split进行切片传化为列表
        LIST = self.URL_data.split('\n')
        # 3.使用查找函数对第一个引号进行切片,并将分割的信息分开放入列表
        KEYS = []
        VALUES = []
        for i in LIST:
            if i.count(":") > 1:
                # print(i.rfind(":"))
                KEYS.append(i[0:i.rfind(":")].replace(":", ""))
                VALUES.append(i[i.rfind(":") + 1:])
            else:
                i2 = i.split(":")
                KEYS.append(i2[0])
                VALUES.append(i2[1])
        # 4.使用zip函数压缩，再使用dict构造成列表
        formdata = dict(zip(KEYS, VALUES))
        # 5.返回转化结果
        return formdata

    @property
    def gain_proxy(slef):
        proxys = pd.read_excel(r'代理池(已检测可用).xlsx')
        proxy = proxys['Proxy_Pool']
        return random.choice(list(proxy))


headers = ''':authority:www.zhipin.com
:method:GET
:path:/c101280600/?period=1&page=10
:scheme:https
accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding:gzip,deflate,br
accept-language:zh-CN,zh;q=0.9
cache-control:max-age=0
cookie:lastCity=101280600;__c=1562721489;__g=-;__l=l=%2Fwww.zhipin.com%2Fjob_detail%2F18fc391f5673fb921X1-09u7FFU~.html%3Fka%3Dsearch_list_1&r=;Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1562549969,1562633593,1562670593,1562721489;t=UP0bCWEkgh4zF13h;wt=UP0bCWEkgh4zF13h;JSESSIONID="";__a=89045758.1558864236.1562670593.1562721489.1653.35.22.1653;Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1562721762
upgrade-insecure-requests:1
user-agent:Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/73.0.3683.103Safari/537.36'''

Headers = Simple_structure(headers)
result = Headers.Structural_data


def main():
    print(result)


if __name__ == '__main__':
    main()
