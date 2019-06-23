

import os
import sys

while True:

    temp=sys.stdout # 记录当前输出指向，默认是consle

    with open("outputlog.txt","a+") as f:
        sys.stdout=f   # 输出指向txt文件
       #   "\nfilename:",os.path.basename(__file__))
        print("some other information")
        print("some other")
        print("information")
        sys.stdout=temp # 输出重定向回consle
        #print(f.readlines()) # 将记录在文件中的结果输出到屏幕

