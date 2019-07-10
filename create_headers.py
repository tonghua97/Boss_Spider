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


headers = ''''''

Headers = Simple_structure(headers)
result = Headers.Structural_data


def main():
    print(result)


if __name__ == '__main__':
    main()
