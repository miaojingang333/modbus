import time
import sys
import win32gui, win32ui, win32con, win32api
import pytesseract
from PIL import Image
from PIL import ImageGrab

bbox = (700, 150, 800, 200)
im = ImageGrab.grab(bbox)

# 参数 保存截图文件的路径
time.sleep(0.1)
im.save('picture.png')

# def window_capture(filename):
#    hwnd = 0                                                # 窗口的编号，0号表示当前活跃窗口
#
#    hwndDC = win32gui.GetWindowDC(hwnd)
#    mfcDC = win32ui.CreateDCFromHandle(hwndDC)                # mfcDC创建可兼容的DC
#    saveDC = mfcDC.CreateCompatibleDC()                   # 创建bigmap准备保存图片
#    saveBitMap = win32ui.CreateBitmap()                                                        # 为bitmap开辟空间
#    saveBitMap.CreateCompatibleBitmap(mfcDC, 300, 300)
#                                                           # 高度saveDC，将截图保存到saveBitmap中
#    saveDC.SelectObject(saveBitMap)
#                                                           # 截取从左上角（0，0）长宽为（w，h）的图片
#    saveDC.BitBlt((0, 0), (300, 300), mfcDC, (1000, 500), win32con.SRCCOPY)
#    saveBitMap.SaveBitmapFile(saveDC, filename)
#
# beg = time.time()

def main():
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
   a = pytesseract.image_to_string(Image.open("picture.png"))
   if a == "bad":
      time.sleep(0.4)
      print("出现 bad ", time.strftime("%m-%d %H:%M:%S", time.localtime()))
      temp = sys.stdout
      with open("C:\\Users\\Administrator\\Desktop\\测试结果.txt", "a+") as f:
         sys.stdout = f  # 输出指向txt文件
         print("出现 bad ", time.strftime("%m-%d %H:%M:%S", time.localtime()))
         sys.stdout = temp  # 输出重定向回consle
while True:
   bbox = (700, 150, 800, 200)
   im = ImageGrab.grab(bbox)

   # 参数 保存截图文件的路径
   time.sleep(0.1)
   im.save('picture.png')
   #window_capture("picture.png")
   main()
   end = time.time()
   time.sleep(0.1)
