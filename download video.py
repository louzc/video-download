import sys
from you_get import common as you_get
url=input("请输入要下载的视频/音频的链接")
path=str(input("请输入路径，若空则默认为C:/video"))
if not path:
    path=="C:/video"
print("请不要短时间内下载过多，否则可能无法正常下载")
sys.argv = ['you-get', '--debug', '-o', "C:/video",url]
you_get.main()
input("按enter退出")