# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:18:31 2018

@author: Jess
"""

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import random
base_url="https://baike.baidu.com"
his=["/item/%E8%9C%98%E8%9B%9B/8135707"]
"""
url=base_url +his[-1]
html=urlopen(url).read().decode("utf-8")
soup=BeautifulSoup(html,features="lxml")
print(soup.find("h1").get_text(),'url',his[-1])

sub_urls=soup.find_all("a",{"target":"_blank","href":re.compile(r"^/item/(%.{2})+")})#{2}表示紧跟的前一个。重复两次，
                      #+，表示前一个（）重复多次，$结尾
#for i in sub_urls:
#    print(i.get_text())

if len(sub_urls)!=0:
    his.append(random.sample(sub_urls,1)[0]["href"])
else:
    his.pop()#.pop(),删除列表最后一个值，如果列表只有一个值，则清空，print（his。pop（））打印被删除的值
print(his)
"""
for i in range(20):
    url=base_url + his[-1]#不能把字符串和列表相加，需要用【-1】选定最后一个，在循环中，添加了一个，这个-1，也就选择了新加的链接
    html=urlopen(url).read().decode("utf-8")
    soup=BeautifulSoup(html,features="lxml")
    his1=soup.find_all("a",{"target":"_blank","href":re.compile(r"/item/(%.{2})+$")})
    print(i,soup.find("h1").get_text())
    if len(his1)!=0:
        his.append(random.sample(his1,1)[0]["href"])
    else:
        his.pop()#如果len（his1）空，那就删除这个循环已经爬过的页面，因为此时his1有两个元素
    print(his[1])