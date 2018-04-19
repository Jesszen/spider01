# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:17:04 2018

@author: Jess
"""
import requests
import webbrowser
#parameter={'wd':"saas"}#百度的关键词"wd"

#r=requests.get("https://www.baidu.com/baidu?",params=parameter)
#print(r.url)
#webbrowser.open(r.url)

"""
data={"firstname":"Jess","lastname":"zen"}
r=requests.post("http://pythonscraping.com/pages/files/processing.php",data=data)
print(r.text)
file={"uploadFile":open("C:/Users/Jess/Pictures/1.jpg","rb")}
r=requests.post("http://pythonscraping.com/files/processing2.php",files=file)
print(r.text)
payload={'username': 'Morvan', 'password': 'password'}
r=requests.post("http://pythonscraping.com/pages/cookies/welcome.php",data=payload)
print(r.cookies.get_dict())

r=requests.get("http://pythonscraping.com/pages/cookies/welcome.php",cookies=r.cookies)
print(r.text)

###在一个会话中，不需要每次传递cookies
session=requests.Session()
payload={'username': 'Morvan', 'password': 'password'}
r=session.post("http://pythonscraping.com/pages/cookies/welcome.php",data=payload)#session会话，而不是直接调用requests。post
print(r.cookies.get_dict())
r=session.get("http://pythonscraping.com/pages/cookies/welcome.php")
print(r.text)
"""

"""
下载图片
"""
src="https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

import os

print(os.getcwd())
os.makedirs('./img/', exist_ok=True)#当时空的文件夹是，不可见，即隐藏状态
from urllib.request import urlretrieve
urlretrieve(src,"./img/pppppp.png")
session=requests.Session()
#########################session.trust_env = False#解决代理问题
r=session.get(src)
with open("./img/image222.png","wb") as f:#wb 是写入
    f.write(r.content)#requests  可以断点下载
    
r=session.get(src,stream=True)
with open("./img/image33333.png","wb") as f:
    for chunk in r.iter_content(chunk_size=3):#把r分成很多个chunk，然后写入chunk
        f.write(chunk)
