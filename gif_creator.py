''' 参考 https://github.com/HeZhang1994/gif-creator 生成自定义延时的GIF图像 '''
import os
import shutil
import imageio


def same_duration(PATTERN):
    print('\nPattern %d - Each frame of GIF image has the same duration.' % PATTERN)

    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(PATH_INPUT_IMAGE) if iN.endswith(FORMAT_INPUT_IMAGE)))
    imgNames.sort(key=lambda x: int(x[:-4]))  # 按数字顺序排序

    for imgName in imgNames:
        imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))

    imageio.mimsave(PATH_OUTPUT_IMAGE + GIF_NAME_SAME, imgGIF, duration=DURATION_FRAME)


def different_duration(PATTERN):
    print('\nPattern %d - Each frame of GIF image has different duration.' % PATTERN)

    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(PATH_INPUT_IMAGE) if iN.endswith(FORMAT_INPUT_IMAGE)))
    imgNames.sort(key=lambda x: int(x[:-4]))

    for imgName in imgNames:
        if imgName == '1.jpg' or imgName == '8456.jpg':
            # '1.jpg'    - The first frame in GIF image.
            # '8456.jpg' - The last frame in GIF image.
            tt = 0
            while tt < REPEAT_TIMES_FRAME:
                imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))
                tt += 1
        else:
            imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))

    imageio.mimsave(PATH_OUTPUT_IMAGE + GIF_NAME_DIFF, imgGIF, duration=DURATION_FRAME)


# 设置输入/输出图片文件夹路径
PATH_INPUT_IMAGE = 'keyframes_extract_matlab/keyframes_images/'
PATH_OUTPUT_IMAGE = 'Visualization/gif/'

if os.path.exists(PATH_OUTPUT_IMAGE) is True:
    shutil.rmtree(PATH_OUTPUT_IMAGE)
os.mkdir(PATH_OUTPUT_IMAGE)

# 设置输入图片的格式
FORMAT_INPUT_IMAGE = '.jpg'

# 设置输出图片的名字
GIF_NAME_SAME = "imgGIF_SAME.gif"
GIF_NAME_DIFF = "imgGIF_DIFF.gif"

# 每帧的周期长度
DURATION_FRAME = 0.25

# 第一帧和最后一帧重复的帧数
REPEAT_TIMES_FRAME = 6


# 开始生成GIF
print('\nStart creating GIF image...')

# 两种模式依次运行生成两个GIF
PATTERN = 1  # 每帧有相同周期
same_duration(PATTERN)
print('\nPATTERN 1 complete!\n')
PATTERN = 2  # 第一帧和最后一帧有更长的周期（通过重复添加第一帧和最后一帧实现）
different_duration(PATTERN)
print('\nPATTERN 2 complete!\n')