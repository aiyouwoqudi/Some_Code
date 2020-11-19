import os
srcFile = r'C:\Users\MaZongYang\Desktop\111111.txt'
dstFile = r'C:\Users\MaZongYang\Desktop\这是啥.txt'
try:
    os.rename(srcFile,dstFile)
except Exception as e:
    print(e)
    print('rename file fail\r\n')
else:
    print('rename file success\r\n')
