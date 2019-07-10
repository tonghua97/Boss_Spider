import datetime
import pandas as pd
import time

F = ['工程师', '前端', 'Java', 'Android', '测试', '架构', '算法', '技术', '基建', '机器', '排序']
G = ['数据分析', '产品', 'UI', 'ui', '交互设计', '设计岗位', '用户', '数据专员']
H = ['法务', '会计', '出纳', '财务', '审计', '内审', '总账', '财税', '资产']
I = ['HR', '招生', '行政', '招聘', '认证', '薪酬', '资质', '前台', '人力', 'hrbp', '人事', '文员', '文档']
J = ['运营专员', '客服', '运营助理', '新媒体', '运营主管', 'KA业务', '运营经理', '渠道', '招商', '培训'
    , '运力', '大客户', '运营', 'BBS', 'bbs', '项目', '客户', '售后', '商务', '城市经理', '营销', '仓库'
    , '电销', '资料', '地推', '司机', '司管', '区域经理', '电商', '催收', '外贸', '淘宝', '业务', '邀约'
    , '车险', '标注', '游戏', '顾问']
K = ['市场', '推广', '公关', '销售', '商业', '投资', '战略', 'BD']


def Classification(DATA, Data):
    for i, iii in zip(Data['职位名称'], range(len(Data['职位名称']))):
        for f in F:
            if f in i:
                data = '技术部'
                DATA.append(data)
                # print(i,f,data)
                break
        if len(DATA) == iii + 1:
            continue
        for g in G:
            if g in i:
                data = '产品部'
                DATA.append(data)
                # print(i,g,data)
                break
        if len(DATA) == iii + 1:
            continue
        for h in H:
            if h in i:
                data = '财务部'
                DATA.append(data)
                # print(i,h,data)
                break
        if len(DATA) == iii + 1:
            continue
        for ii in I:
            if ii in i:
                data = '人事部'
                DATA.append(data)
                # print(i,ii,data)
                break
        if len(DATA) == iii + 1:
            continue
        for j in J:
            if j in i:
                data = '运营部'
                DATA.append(data)
                # print(i,j,data)
                break
        if len(DATA) == iii + 1:
            continue
        for k in K:
            if k in i:
                data = '市场部'
                DATA.append(data)
                # print(i,k,data)
                break
        if len(DATA) == iii + 1:
            continue
        if len(DATA) < iii + 1:
            data = '其他'
            DATA.append(data)


def main():
    print("当前进度：正在为招聘职位分类···")
    Data = pd.read_excel("Boss直聘.xlsx")
    DATA = []
    Classification(DATA, Data)
    Data['部门分类'] = DATA
    Data.to_excel('Boss直聘(分类后).xlsx', index=False)


if __name__ == '__main__':
    main()
