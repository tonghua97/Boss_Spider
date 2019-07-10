import requests
import time
from Boss_spider import create_headers
import random


class Boss_spiders(object):
    def __init__(self, url, headers, html):
        self.url = url
        self.headers = headers
        self.html = html

    def request_url(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.encoding = response.apparent_encoding
            # print(response.text)
            self.html.write(response.text + "\n")
        except:
            print("获取网页信息失败".center(20, "-"))

    def Run(self):
        self.request_url()


def main():
    url = "https://www.zhipin.com/c101280600/?period=1&page={number}"
    with open("html.txt", "a+", encoding="utf-8") as html:
        for i in range(1, 11):
            print("\r当前进度：正在爬取第{number}页数据{dot}".format(number=i, dot="·" * i), end="")
            url_format = url.format(number=i)
            Spider = Boss_spiders(url_format, create_headers.result, html)
            Spider.Run()
            time.sleep(random.uniform(2, 5))


if __name__ == '__main__':
    main()
