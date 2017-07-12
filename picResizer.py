"""
功能:需要将单个图片批处理处理成目前尺寸图片
使用:pics中输入对应的宽、高、名称即可。
"""
import os
from PIL import Image


# 图片类定义
class APic(object):
    def __init__(self, width, height, filename):
        self.width = width  # 宽
        self.height = height  # 高
        self.filename = filename  # 输出文件名称


'''
filein:  输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''


def resizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
    out.save(fileout, type)


pics = [APic(187, 105, 'pic2'), APic(230, 240, 'pic3')]
filein = 'pic.jpg'
fileType = 'png'
for pic in pics:
    fileout = pic.filename + "." + fileType
    width = pic.width
    height = pic.height
    resizeImage(filein, fileout, width, height, fileType)
