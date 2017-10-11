import re
from urllib import request, parse, error
import json
import time

url_reg = re.compile(r'img[\s]+src="(http.*?)\?')

img_name = re.compile(r'i/(.*)')
url = 'https://www.zhuangbi.info/?page={}'
path = r'D:\images\{}'

imageList = []

for page in range(3, 82):
    time.sleep(1)
    try:
        html = request.urlopen(url.format(page)).read()
        for imgurl in url_reg.findall(str(html)):
            print(imgurl)
            imageList.append(imgurl)
    except:
        pass

print("完成", len(imageList))

with open('imgeUrls.json', "w") as f:
    f.write(json.dumps(imageList))

print("写入完成")

for img in imageList:
    time.sleep(1)
    try:
        if img in imageList:
            imageList.remove(img)
        request.urlretrieve(img, path.format(img_name.findall(img)[0]))
        print(img, "--->  下载完成")
    except:
        imageList.append(img)
