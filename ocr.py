#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 3 16:00:00 2019
利用百度api实现图片文本识别
@author: Wang Xiaopeng
"""

import glob
from os import path
import os
from aip import AipOcr
from PIL import Image
import xlwt
import xlrd
import xlutils.copy
import time
import csv


def write_excel_csv(list):
    # 创建workbook
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = workbook.add_sheet('result', cell_overwrite_ok=True)
    workbook.save('./result/result.xls')

    # 已获取到了所有信息的字典数组
    message = [{} for j in range(219)]  # 至少219项
    result = [[] for j in range(219)] # 写入csv里的二维列表
    for i in range(20):
        for j in range(7, 14):
            list[i][j] = float(list[i][j])
        sum = list[i][7] + list[i][8] + list[i][9] + list[i][10] + list[i][11] + list[i][12] + list[i][13]
        message[i] = {'date':list[i][-1],
                      'language':[list[i][0], list[i][1], list[i][2], list[i][3], list[i][4], list[i][5], list[i][6]],
                      'value':[list[i][7], list[i][8], list[i][9], list[i][10], list[i][11], list[i][12], list[i][13]],
                      'rate':[list[i][7] / sum, list[i][8] / sum, list[i][9] / sum, list[i][10] / sum, list[i][11] / sum, list[i][12] / sum, list[i][13] / sum]}  # 使用orc精确度低，会导致识别数据不全
        result[i].append(message[i].get('date'))
        # 生成写进csv里的列表
        for k in range(7):
            result[i].append(message[i].get('language')[k])
            result[i].append(message[i].get('rate')[k])
    for i in range(20, 40):
        for j in range(8, 16):
            list[i][j] = float(list[i][j])
        sum = list[i][8] + list[i][9] + list[i][10] + list[i][11] + list[i][12] + list[i][13] + list[i][14] + list[i][15]
        message[i] = {'date':list[i][-1],
                      'language':[list[i][0], list[i][1], list[i][2], list[i][3], list[i][4], list[i][5], list[i][6], list[i][7]],
                      'value':[list[i][8], list[i][9], list[i][10], list[i][11], list[i][12], list[i][13], list[i][14], list[i][15]],
                      'rate':[list[i][8] / sum, list[i][9] / sum, list[i][10] / sum, list[i][11] / sum, list[i][12] / sum, list[i][13] / sum, list[i][14] / sum, list[i][15] / sum]}
        result[i].append(message[i].get('date'))
        for k in range(8):
            result[i].append(message[i].get('language')[k])
            result[i].append(message[i].get('rate')[k])
    for i in range(40, 60):
        for j in range(9, 18):
            list[i][j] = float(list[i][j])
        sum = list[i][9] + list[i][10] + list[i][11] + list[i][12] + list[i][13] + list[i][14] + list[i][15] + list[i][16] + list[i][17]
        message[i] = {'date':list[i][-1],
                      'language':[list[i][0], list[i][1], list[i][2], list[i][3], list[i][4], list[i][5], list[i][6], list[i][7], list[i][8]],
                      'value':[list[i][9], list[i][10], list[i][11], list[i][12], list[i][13], list[i][14], list[i][15], list[i][16], list[i][17]],
                      'rate':[list[i][9] / sum, list[i][10] / sum, list[i][11] / sum, list[i][12] / sum, list[i][13] / sum, list[i][14] / sum, list[i][15] / sum, list[i][16] / sum, list[i][17] / sum]}
        result[i].append(message[i].get('date'))
        for k in range(9):
            result[i].append(message[i].get('language')[k])
            result[i].append(message[i].get('rate')[k])
    for i in range(60, 219):
        for j in range(11, 22):
            list[i][j] = float(list[i][j])
        sum = list[i][11] + list[i][12] + list[i][13] + list[i][14] + list[i][15] + list[i][16] + list[i][17] + list[i][18] + list[i][19] + list[i][20] + list[i][21]
        message[i] = {'date':list[i][-1],
                      'language':[list[i][0], list[i][1], list[i][2], list[i][3], list[i][4], list[i][5], list[i][6], list[i][7], list[i][8], list[i][9], list[i][10]],
                      'value':[list[i][11], list[i][12], list[i][13], list[i][14], list[i][15], list[i][16], list[i][17], list[i][18], list[i][19], list[i][20], list[i][21]],
                      'rate':[list[i][11] / sum, list[i][12] / sum, list[i][13] / sum, list[i][14] / sum, list[i][15] / sum, list[i][16] / sum, list[i][17] / sum, list[i][18] / sum, list[i][19] / sum, list[i][20] / sum, list[i][21] / sum]}
        result[i].append(message[i].get('date'))
        for k in range(11):
            result[i].append(message[i].get('language')[k])
            result[i].append(message[i].get('rate')[k])

    # 写csv
    file = open('./result/result.csv','a',newline='')
    content = csv.writer(file)
    for i in range(219):
        content.writerow(result[i])

    # 写excel
    for i in range(219):  # 一共多少条信息（20+20+20+159）就要循环更新几次
        data = xlrd.open_workbook('./result/result.xls')
        ws = xlutils.copy.copy(data)
        table = ws.get_sheet(0)
        table.write(0, i + 1, message[i].get('date'))  # 每一条记录都会增加一个季度信息
        # for j in range(len(message[i].get('language'))):
        #     table.write(j+1, 0, message[i].get('language')[j])
        ws.save('./result/result.xls')  # 每次新加信息最好就保存一次，否则造成下面获取行数信息更新不及时
        data = xlrd.open_workbook('./result/result.xls')
        table1 = data.sheet_by_index(0)
        nrows = table1.nrows  # 获取此时行数
        ncols = table1.ncols  # 获取此时列数
        print(nrows, ncols)
        s = []  # 获取此时已出现过的编程语言列表
        for j in range(nrows - 1):
            s.append(table1.cell_value(j + 1, 0))
        print(s)
        # t = []
        # for j in range(ncols-1):
        #     t.append(table1.cell_value(0, j+1))  # 获取此时已出现的月份列表
        # print(t)
        for j in range(len(message[i].get('language'))):
            if message[i].get('language')[j] in s:
                table.write(s.index(message[i].get('language')[j]) + 1, i + 1, message[i].get('value')[j])
            else:
                table.write(nrows, 0, message[i].get('language')[j])  # 这里的行数一定要注意
                table.write(nrows, i + 1, message[i].get('value')[j])
                print(nrows)
            ws.save('./result/result.xls')
            data = xlrd.open_workbook('./result/result.xls')
            table1 = data.sheet_by_index(0)
            nrows = table1.nrows  # 获取此时行数
            ncols = table1.ncols  # 获取此时列数




def convertimg(picfile, outdir):
    '''调整图片大小，对于过大的图片进行压缩
    picfile:    图片路径
    outdir：    图片输出路径
    '''
    img = Image.open(picfile)
    width, height = img.size
    while (width * height > 4000000):  # 该数值压缩后的图片大约 两百多k
        width = width // 2
        height = height // 2
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(path.join(outdir, os.path.basename(picfile)))


def baiduOCR(picfile, k):               # 正常图片的识别（共（20+20+20+30+6+68）×2=328张）需要单独一个百度账号调用api
    filename = path.basename(picfile)

    APP_ID = '16795710'  # 第一个账号
    API_KEY = 'AQLljP54joLObXjFdS6CtYAj'
    SECRECT_KEY = 'mXPXGvMfa2QHg5yv0pvFHQgKyGRR4dDP'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    # message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    message = client.basicAccurate(img)   # 通用文字高精度识别，每天 500 次免费
    # message = client.accurate(img)  # 含位置高精度版
    time.sleep(0.5)  # 为解决qps并行提交速度过快的问题  另一种思路是，只要有error_msg，就重发
    print(message)
    print("识别成功！")
    i.close()

    k = k // 2
    for text in message.get('words_result'):
        list[k].append(text.get('words').strip())  # 去除开头结尾的空格 防止有的识别出来是'C'而有的是' C'


def baiduOCR1(picfile, k, j):            # 对有图标图片的识别（共54×4=208张）和下面共用另一个百度账号调用api
    filename = path.basename(picfile)

    APP_ID = '17920138'  # 第二个账号
    API_KEY = '9v98zCuZICwCXWg84UpIRnAG'
    SECRECT_KEY = 'HuTGlxz8RjIHKhO3RGFIPyZZRtfWnWtv'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    # message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    message = client.basicAccurate(img)   # 通用文字高精度识别，每天 500 次免费
    # message = client.accurate(img)  # 含位置高精度版
    time.sleep(0.5)  # 为解决qps并行提交速度过快的问题
    print(message)
    print("识别成功！")
    i.close()

    k = k // 2 + j // 4
    for text in message.get('words_result'):
        list[k].append(text.get('words').strip())


def baiduOCR2(picfile, k, j):              # 对有猫头鹰图片的识别（共3张）
    filename = path.basename(picfile)

    APP_ID = '17920138'  # 第二个账号
    API_KEY = '9v98zCuZICwCXWg84UpIRnAG'
    SECRECT_KEY = 'HuTGlxz8RjIHKhO3RGFIPyZZRtfWnWtv'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("正在识别图片：\t" + filename)
    # message = client.basicGeneral(img)  # 通用文字识别，每天 50 000 次免费
    message = client.basicAccurate(img)   # 通用文字高精度识别，每天 500 次免费
    # message = client.accurate(img)  # 含位置高精度版
    time.sleep(0.5)  # 为解决qps并行提交速度过快的问题
    print(message)
    print("识别成功！")
    i.close()

    k = k // 2 + j
    if j % 3 == 0:
        manual = ['Java', 'C', 'JavaScript', 'PHP', 'C++', 'Visual Basic', 'Perl', 'C#', 'Delphi', 'Pascal', 'Python']  # 文字识别出来的words起始有一个空格
        list[k].extend(manual)      # 注意要用extend增加一个数据集合不能用append，append是增加一项，会把列表作为一项插入
    elif j % 3 == 1:
        manual = ['Java', 'JavaScript', 'C', 'PHP', 'C++', 'Visual Basic', 'Perl', 'C#', 'Delphi', 'Pascal', 'Python']
        list[k].extend(manual)
    else:
        manual = ['Java', 'JavaScript', 'C', 'PHP', 'C++', 'Visual Basic', 'Perl', 'C#', 'Delphi', 'Python', 'Pascal']
        list[k].extend(manual)

    for text in message.get('words_result'):
        list[k].append(text.get('words').strip())


if __name__ == "__main__":

    list = [[]for i in range(250)]  # 总共219个关键帧，故至少219个数组存储信息

    '''对7行数据的图片文件夹进行识别'''
    if not path.exists("tmp7"):
        os.mkdir("tmp7")
    for picfile in glob.glob("keyframes_cutting/picture7/*"):
        convertimg(picfile, "tmp7")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp7/")
    files.sort(key= lambda x:int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp7/" + files[l]
    print(files)
    k = 0
    for picfile in files:
        baiduOCR(picfile, k)
        k = k + 1
        os.remove(picfile)
    os.removedirs("tmp7")
    print("7行数据图片已识别完毕！")
    print(list)

    '''对8行数据的图片文件夹进行识别'''
    if not path.exists("tmp8"):
        os.mkdir("tmp8")
    for picfile in glob.glob("keyframes_cutting/picture8/*"):
        convertimg(picfile, "tmp8")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp8/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp8/" + files[l]
    print(files)
    k = 40 # 算上picture7的40张图片
    for picfile in files:
        baiduOCR(picfile, k)
        k = k + 1
        os.remove(picfile)
    os.removedirs("tmp8")
    print("8行数据图片已识别完毕！")
    print(list)

    '''对9行数据的图片文件夹进行识别'''
    if not path.exists("tmp9"):
        os.mkdir("tmp9")
    for picfile in glob.glob("keyframes_cutting/picture9/*"):
        convertimg(picfile, "tmp9")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp9/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp9/" + files[l]
    print(files)
    k = 80
    for picfile in files:
        baiduOCR(picfile, k)
        k = k + 1
        os.remove(picfile)
    os.removedirs("tmp9")
    print("9行数据图片已识别完毕！")
    print(list)

    '''对11行数据的正常图片文件夹1进行识别'''
    if not path.exists("tmp11_normal1"):
        os.mkdir("tmp11_normal1")
    for picfile in glob.glob("keyframes_cutting/picture11_normal1/*"):
        convertimg(picfile, "tmp11_normal1")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp11_normal1/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp11_normal1/" + files[l]
    print(files)
    k = 120
    for picfile in files:
        baiduOCR(picfile, k)
        k = k + 1
        os.remove(picfile)
    os.removedirs("tmp11_normal1")
    print(list)

    '''对11行数据的特殊图片（有图案）文件夹进行识别'''
    if not path.exists("tmp11_special"):
        os.mkdir("tmp11_special")
    for picfile in glob.glob("keyframes_cutting/picture11_special/*"):
        convertimg(picfile, "tmp11_special")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp11_special/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp11_special/" + files[l]
    print(files)
    k = 180  # 这里的k只是起到基数的作用
    j = 0  # j才是作为增量的值
    for picfile in files:
        baiduOCR1(picfile, k, j) # 这里也要注意是4张图片为一组，暂时考虑重新写一个函数
        j = j + 1  # 用于4张图片一组数据的计数
        os.remove(picfile)
    os.removedirs("tmp11_special")
    print(list)

    '''对11行数据的正常图片文件夹2进行识别'''
    if not path.exists("tmp11_normal2"):
        os.mkdir("tmp11_normal2")
    for picfile in glob.glob("keyframes_cutting/picture11_normal2/*"):
        convertimg(picfile, "tmp11_normal2")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp11_normal2/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp11_normal2/" + files[l]
    print(files)
    k = 284  # 虽然上一组是四张图片一组，但为了对应方便，还是按照两张一组计数
    for picfile in files:
        baiduOCR(picfile, k)
        k = k + 1
        os.remove(picfile)
    os.removedirs("tmp11_normal2")
    print(list)

    '''对11行数据的猫头鹰图片文件夹进行识别'''
    if not path.exists("tmp11_owl"):
        os.mkdir("tmp11_owl")
    for picfile in glob.glob("keyframes_cutting/picture11_owl/*"):
        convertimg(picfile, "tmp11_owl")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp11_owl/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp11_owl/" + files[l]
    print(files)
    k = 296  # 同样，k作为基数
    j = 0  # j作为增量
    for picfile in files:    # 这里要对数据进行手动添加，因为我们只截取了右半部分
        baiduOCR2(picfile, k, j)
        j = j + 1  # 用j来判断是第几张图片
        os.remove(picfile)
    os.removedirs("tmp11_owl")
    print(list)

    '''对11行数据的正常图片文件夹3进行识别'''
    if not path.exists("tmp11_normal3"):
        os.mkdir("tmp11_normal3")
    for picfile in glob.glob("keyframes_cutting/picture11_normal3/*"):
        convertimg(picfile, "tmp11_normal3")
    print("图片识别...")
    '''必须先对文件名排序，不然会出现1、10、11、2、20、21、22这样的顺序'''
    files = os.listdir("./tmp11_normal3/")
    files.sort(key=lambda x: int(x[1:-6]))
    for l in range(len(files)):
        files[l] = "tmp11_normal3/" + files[l]
    print(files)
    k = 302 # 加上最后的136共438 对应总共219个关键帧
    for picfile in files:
        baiduOCR(picfile, k)
        k = k + 1
        os.remove(picfile)
    os.removedirs("tmp11_normal3")
    print("11行数据图片已识别完毕！")
    print(list)
    f = open('result/result_list.txt', 'a')
    f.write(str(list))
    f.close()
    print("全部数据图片已识别完毕！")
    # write_excel_csv(list)   # 我们将结果单独拿出来再进行数据处理

