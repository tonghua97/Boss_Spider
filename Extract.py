import re
import pandas as pd


def formatting():
    result = []
    with open("html.txt", "r", encoding="utf-8") as r:
        HTML = r.read()

    position = re.findall('<div class="job-title">(.*?)</div>', HTML, re.S)
    price = re.findall('<span class="red">(.*?)</span>', HTML, re.S)
    price = map(lambda x: x.replace("·13薪", ""), price)
    address = re.findall(
        '<div class="info-primary">.*?<p>(.*?)<em class="vline"></em>.*?<em class="vline"></em>.*?</p>', HTML, re.S)
    address = map(lambda x: x.replace(" ", ""), address)
    experience = re.findall(
        '<div class="info-primary">.*?<p>.*?<em class="vline"></em>(.*?)<em class="vline"></em>.*?</p>', HTML, re.S)
    experience = map(lambda x: x.replace(" ", ""), experience)
    education = re.findall(
        '<div class="info-primary">.*?<p>.*?<em class="vline"></em>.*?<em class="vline"></em>(.*?)</p>', HTML, re.S)
    education = map(lambda x: x.replace(" ", ""), education)
    company = re.findall('<h3 class="name"><a href=".*?target="_blank">(.*?)</a></h3>', HTML, re.S)
    company = map(lambda x: x.replace(".", ""), company)
    hyperlink = re.findall('<div class="info-primary">.*?<h3 class="name">.*?<a href="(.*?)" data-jid=', HTML, re.S)
    hyperlink = map(lambda x: "https://www.zhipin.com" + x, hyperlink)

    for i, j, k, t, m, n, o in zip(position, price, address, experience, education, company, hyperlink):
        job = {
            '职位名称': i,
            '薪资待遇': j,
            '工作地址': k,
            '工作经验': t,
            '学历要求': m,
            '公司名称': n,
            '详细链接': o
        }
        result.append(job)
    return result


def on_file(data):
    file = pd.DataFrame(data, columns=["职位名称", "薪资待遇", "工作地址", "工作经验", "学历要求", "公司名称", "详细链接"])
    file.to_excel("Boss直聘.xlsx", index=False)


def main():
    print("\n当前进度：正在格式化信息中···")
    result = formatting()
    on_file(result)


if __name__ == '__main__':
    main()
