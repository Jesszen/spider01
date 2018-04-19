# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 21:58:03 2018

@author: Jess
"""

from bs4 import BeautifulSoup
import requests
url="http://www.ngchina.com.cn/animals/"
html=requests.get(url).text
#相当于html=urlopen("").read().decode("utf_8")

soup=BeautifulSoup(html,features="lxml")#把网页结构放进去
image_url=soup.find_all("ul",{"class":"img_list"})

for li in image_url:#每一个ul
    img=li.find_all("img")#针对每一个ul 找出所有img，是一个元素
    for i in img:
        k=i["src"]#提取每一个图片的网址
        r=requests.get(k,stream=True)#单独打开图片的网页
        img_name=k.split('/')[-1]#网址按照/分列，取最后一个
        with open("./img/%s"%img_name,"wb")as f:#中间那个给下载的图片取名字
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print("save_name%s" %img_name)
