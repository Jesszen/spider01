# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:29:22 2018

@author: Jess
"""

import re
#单次匹配
"""
\d : 任何数字
\D : 不是数字
\s : 任何 white space, 如 [\t\n\r\f\v]
\S : 不是 white space
\w : 任何大小写字母, 数字和 “” [a-zA-Z0-9]
\W : 不是 \w
\b : 空白字符 (只在某个字的开头或结尾)
\B : 空白字符 (不在某个字的开头或结尾)
\\ : 匹配 \
. : 匹配任何字符 (除了 \n)
^ : 匹配开头
$ : 匹配结尾
? : 前面的字符可有可无
"""
print(re.search(r"cat","dog runs to cat"))

print(re.search(r"r[ua]n","dog ran to cat"))

print(re.search(r"r[a-z]n","dog ran to cat"))

print(re.search(r"r[A-Z]n","dog ran to cat rAn"))

print(re.search(r"r[A-Z0-9]n","dog ran to cat r9n"))

print(re.search(r"r\dn","dog ran to cat r8n"))

print(re.search(r"r\Dn","dog ran to cat r8n"))

print(re.search(r"r\sn","dog r\nn to cat r8n"))#\n 表示换行

print(re.search(r"r\Sn","dog r\nn to cat r8n"))

print(re.search(r"r\wn","dog rnn to cat r8n"))

print(re.search(r"r\Wn","dog r-n to cat r8n"))

print(re.search(r"\brnn\b","dog rnn to cat r8n"))

print(re.search(r"\Brnn\B","dog ernnn to cat r8n"))
print(re.search(r"\Brnn\b","dog 8rnn to cat r8n"))

print(re.search(r"rnn\\","dog rnn\ to cat r8n"))

print(re.search(r"r.n","dog r[n to cat r8n"))

print(re.search(r"^rnn","rnn\ to cat r8n"))
print(re.search(r"rnn$","dog rnn\ to cat rnn"))

print(re.search(r"Mon(day)?\b","dog Mon rnn\ to cat r8n"))

string="""
dog runs to cat
i am monster"""
print(re.search(r"^i",string,flags=re.M))#re。M 把段落看成多个行

#多次匹配
"""
* : 重复零次或多次
+ : 重复一次或多次
{n, m} : 重复 n 至 m 次
{n} : 重复 n 次
"""
print(re.search(r"ab*","a is s"))

print(re.search(r"ab+","ab is s"))

print(re.search(r"ab{1,8}","abbbbb is s "))

#分组
match =re.search(r"(\d+),Date: (.+)","ID: 021523,Date: Feb/12/2017")#r后如果连个（），中间除，号外还有其他字符，则要带匹配项之间相同
print(match.group(1))
print(match.group(2))

match =re.search(r"(?P<id>\d+),Date: (?P<date>.+)","ID: 021523,Date: Feb/12/2017")#?P<>,可以标注键名，注意P是大写
print(match.group("id"))
print(match.group(2))

#匹配全部项
print(re.findall(r"r[au]n","dog run ran me"))#返回的是一个列表

print(re.findall(r"(ran|run)",'dao ran run me '))#|是or的意思
  
#替换
print(re.sub(r"r[au]n","fos","dao ran run me"))#所有能匹配的项目都换成fos

#分割
print(re.split(r"[:*/.\\]","a: c/ d*f"))

#正则表达式单独赋值

complie_1=re.compile(r"r[au]n")
print(re.search(complie_1,"dao ren ran"))

print(re.search(r"^ceb","feb month"))