# 分别对7行数据、8行数据、9行数据、11行数据的图片进行切割
# 导入相关的库
from PIL import Image
import os
from os import path
if not path.exists("keyframes_cutting"):
    os.mkdir("keyframes_cutting")

'''对7行数据图片切割'''
if not path.exists("keyframes_cutting/picture7"):
    os.mkdir("keyframes_cutting/picture7")
i = 0
files = os.listdir("./keyframes/keyframes7/")
files.sort(key= lambda x:int(x[:-4]))
for l in range(len(files)):
    files[l] = "keyframes/keyframes7/" + files[l]

for pic in files:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.15 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture7/k%s-A.jpg"%(str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture7/k%s-B.jpg"%(str(i)))

print("keyframes7 cutting done.")

'''对8行数据图片切割'''
if not path.exists("keyframes_cutting/picture8"):
    os.mkdir("keyframes_cutting/picture8")
i = 0
files = os.listdir("./keyframes/keyframes8/")
files.sort(key= lambda x:int(x[:-4]))
for l in range(len(files)):
    files[l] = "keyframes/keyframes8/" + files[l]

for pic in files:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.15 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture8/k%s-A.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture8/k%s-B.jpg" % (str(i)))
print("keyframes8 cutting done.")

'''对9行数据图片切割'''
if not path.exists("keyframes_cutting/picture9"):
    os.mkdir("keyframes_cutting/picture9")
i = 0
files = os.listdir("./keyframes/keyframes9/")
files.sort(key= lambda x:int(x[:-4]))
for l in range(len(files)):
    files[l] = "keyframes/keyframes9/" + files[l]

for pic in files:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.15 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture9/k%s-A.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture9/k%s-B.jpg" % (str(i)))
print("keyframes9 cutting done.")

'''对11行数据中的正常图片切割'''
if not path.exists("keyframes_cutting/picture11_normal1"):
    os.mkdir("keyframes_cutting/picture11_normal1")
if not path.exists("keyframes_cutting/picture11_normal2"):
    os.mkdir("keyframes_cutting/picture11_normal2")
if not path.exists("keyframes_cutting/picture11_normal3"):
    os.mkdir("keyframes_cutting/picture11_normal3")

files1 = os.listdir("./keyframes/keyframes11_normal1/")
files1.sort(key= lambda x:int(x[:-4]))
for l in range(len(files1)):
    files1[l] = "keyframes/keyframes11_normal1/" + files1[l]
files2 = os.listdir("./keyframes/keyframes11_normal2/")
files2.sort(key= lambda x:int(x[:-4]))
for l in range(len(files2)):
    files2[l] = "keyframes/keyframes11_normal2/" + files2[l]
files3 = os.listdir("./keyframes/keyframes11_normal3/")
files3.sort(key= lambda x:int(x[:-4]))
for l in range(len(files3)):
    files3[l] = "keyframes/keyframes11_normal3/" + files3[l]
# 正常部分第一部分
i = 0
for pic in files1:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.12 * w  # 这里数据过小，故宽度也减小
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_normal1/k%s-A.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_normal1/k%s-B.jpg" % (str(i)))
print("keyframes11_normal1 cutting done.")
# 正常部分第二部分
i = 0
for pic in files2:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.15 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_normal2/k%s-A.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_normal2/k%s-B.jpg" % (str(i)))
print("keyframes11_normal2 cutting done.")
# 正常部分第三部分
i = 0
for pic in files3:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.15 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_normal3/k%s-A.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_normal3/k%s-B.jpg" % (str(i)))
print("keyframes11_normal3 cutting done.")

'''对11行特殊数据（有图案）图片切割'''
if not path.exists("keyframes_cutting/picture11_special"):
    os.mkdir("keyframes_cutting/picture11_special")
i = 0
files = os.listdir("./keyframes/keyframes11_special/")
files.sort(key= lambda x:int(x[:-4]))
for l in range(len(files)):
    files[l] = "keyframes/keyframes11_special/" + files[l]

for pic in files:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    x = 0
    y = 0.08 * h
    w1 = 0.12 * w  # 这里数据过小，故宽度减小
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_special/k%s-A.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.31 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_special/k%s-B.jpg" % (str(i)))

    x = 0.11 * w
    y = 0.39 * h
    w1 = 0.41 * w
    h1 = 0.6 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_special/k%s-C.jpg" % (str(i)))

    x = 0.52 * w
    y = 0.77 * h
    w1 = 0.48 * w
    h1 = 0.23 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_special/k%s-D.jpg" % (str(i)))
print("keyframes11_special cutting done.")

'''对11行有猫头鹰的数据图片切割'''
if not path.exists("keyframes_cutting/picture11_owl"):
    os.mkdir("keyframes_cutting/picture11_owl")
i = 0
files = os.listdir("./keyframes/keyframes11_owl/")
files.sort(key= lambda x:int(x[:-4]))
for l in range(len(files)):
    files[l] = "keyframes/keyframes11_owl/" + files[l]

for pic in files:
    print(pic)
    # 打开一张图
    img = Image.open(pic)
    i = i+1
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度

    # 左部数据因为数据不全，直接在主程序中手动添加至列表，只提取右部信息
    x = 0.11 * w
    y = 0.08 * h
    w1 = 0.89 * w
    h1 = 0.9 * h
    region = img.crop((x, y, x + w1, y + h1))
    region.save("keyframes_cutting/picture11_owl/k%s-B.jpg" % (str(i)))
print("keyframes11_owl cutting done.")