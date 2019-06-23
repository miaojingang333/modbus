import time
from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = '16074031'
API_KEY = 'MSora39m52n9SrvClMy3CUfm'
SECRET_KEY = 'ndpL06oTPVMbvxByFTlNsjq8QjvDnRzR'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    # r 读的意思  b 二进制
    with open(filePath, 'rb') as f:
        return f.read()

def get_connect():
    image = get_file_content('picture.png')

    """ 调用通用文字识别, 图片参数为本地图片 """
    content = client.basicGeneral(image)

    image_content = ""


    for words in content["words_result"]:
        image_content += words["words"]
    return image_content



    # if image_content == "bad":
    #
    #     print("出现 bad ", time.strftime("%m-%d %H:%M:%S", time.localtime()))
    # else:
    #     time.sleep(1)
    #     print(words["words"], time.strftime("%m-%d %H:%M:%S", time.localtime()))
    #
    #


