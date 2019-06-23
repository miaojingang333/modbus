from PIL import ImageGrab
import time
from baidu666 import get_connect

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
while True:
    bbox = (700, 150, 800, 200)
    im = ImageGrab.grab(bbox)

    # 参数 保存截图文件的路径
    time.sleep(0.1)
    im.save('picture.png')

    if get_connect() >= "5005":
        time.sleep(0.5)
        print("偏高", get_connect())
    if get_connect() <= ("49.95"):
        time.sleep(0.5)
        print("偏低", get_connect())
        #print("出现 bad ", time.strftime("%m-%d %H:%M:%S", time.localtime()))
    #else:
        #print(get_connect())