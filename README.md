##BOSS直聘爬虫(数据存放在Excel里)

####实现的过程
1. 分析页面得到翻页URL：https://www.zhipin.com/c101280600/?period=1&page=2;请求方式为Get请求
2. 拿到Request Header所有信息来伪装请求
3. 将获取的数据存放与txt文件中
4. 使用re模块提取信息
5. 使用pandas将信息存入excel,然后做分类处理

---
####调用的python模块:
	import requests,random,re,pandas,time

---
####懒人解说：
1. 打开浏览器按F12点击Network,刷新,复制Request Headers内的所有信息复制到create_headers.py文件的headers变量中
2. 运行main.py
3. 文件夹中就会出现Boss直聘.xlsx&html.txt&Boss直聘(分类后).xlsx文件
4. 想要整站爬取得同学可以看看我得create_headers.py和spider.py来做深度爬虫