# -*- coding: utf-8 -*-
# 生成词云图
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

# 获取文本信息
text = open(u'./result/result.csv', 'r').read()
# text = open(u'result.txt', 'r').read()
print(text)
# 获取图片
img = np.array(Image.open("image.jpg"))
# 可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white", max_words=2000, mask=img, max_font_size=80, random_state=42)
# 形成词云
wc.generate(text)
# 从图片获取颜色
image_colors = ImageColorGenerator(img)

# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
# plt.figure()

plt.show()
# 保存图片
wc.to_file('./Visualization/ciyun.png')
# wc.to_file('ciyun1.png')