# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:30:04 2018

@author: Jess
"""

from  urllib.request  import urlopen
html=urlopen( "https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode("utf-8")


import re
res=re.findall(r"<title>(.+?)</title>",html)#模块标签内
print("this is :" ,res)

p=re.findall(r"<p>(.+?)</p>",html, flags=re.DOTALL)#因为。不包含换行。当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
print("p is:",p[0])

res=re.findall(r'href="(.*?)"',html)#爬出来的是”“里面的内容，href=，相当于限定范围，为什么”（。*？）”，因为源码就是这个形式
print(res)

from bs4 import BeautifulSoup 

soup=BeautifulSoup(html,features="lxml")
print(soup.h1)


all_href=soup.find_all("a")
print(all_href)
href=[l["href"] for l in all_href]# 以列表的形式储存
print('\n',href)

html2=urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode("utf-8")
soup2=BeautifulSoup(html2,features="lxml")
print(soup2)
ul1=soup2.find_all("li",{"class":"month"})#class  不支持以month开头
print(ul1)
for m in ul1:
    print(m.get_text())
k=[m.get_text() for m in ul1]#把for 循环中的  储存成列表形式
print(k)
ul1=soup2.select('li[class^="month"]')#不筛选二月 feb month
print(ul1)
for k in ul1:
    print(k.get_text())

ul2=soup2.find("ul",{"class":"jan"})#如果要嵌套，则第一步只要find
print(ul2)
jan=ul2.find_all("li")#可以有find——all
for i in jan:
    print(i.get_text())
    
html3=urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode("utf-8")
soup3=BeautifulSoup(html3,features="lxml")
img=soup3.find_all("img")
for i in img:
    print(i["src"])
img2=soup3.find_all("img",{"src":re.compile(r".*?\.jpg")})#刷选以。jpg结尾的图片链接
print(img2)
#k=[i["src"] for i in img2]
print([i["src"] for i in img2])

course=soup3.find_all("a",{"href":re.compile(r"https://morvanzhou.github.io")})#筛选以，，，开头是链接
print(course)
for i in course:
    print(i["href"])