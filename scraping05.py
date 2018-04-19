# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 20:19:58 2018

@author: Jess
"""

import multiprocessing as mp
import re
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen,urljoin

base_url="https://morvanzhou.github.io/"

if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False

def crawl(url):
    html=urlopen(url)
    return html.read().decode()

def parse(html):
    k=BeautifulSoup(html,'lxml')#解析方法‘lxml’
    title=k.find("h1").get_text().strip()#。strip（）去掉语句前后空格
    url1=k.find_all("a",{"href":re.compile(r"^/.+?/$")})#表示以/开头，且以/结尾，中间只要有一个字符就ok
    urls=set([urljoin(base_url,o["href"]) for o in url1])#放在集合里，自动去重
    present_url=k.find("meta",{"property":"og:url"})["content"]
    return title,urls,present_url
"""
unseen=set([base_url,])
seen=set()

count,t1=1,time.time()

while len(unseen) !=0:
    if restricted_crawl and len(seen)>50:
        break#满足条件则中断整个循环
    print('\nDistributed Crawling...')
    htmls=[crawl(url) for url in unseen]
    
    print('\nDistributed Parsing...')
    results=[parse(html) for html in htmls]
    
    print('\nAnalysing...')
    seen.update(unseen)
    unseen.clear()
    
    for title,urls,present_url in results:#第一次用的是base——url，值返回一个结果【包含，标题，当前链接，整个页面的所有链接】
        print(count,title,present_url)
        count+=1
        unseen.update(urls - seen)
print("tatol time:%d"%(time.time()-t1))
"""

if __name__=="__main__": #分布式爬虫，要把参数放在这个下面
    pool=mp.Pool()
    unseen=set([base_url,])
    seen=set()
    count,t1=1,time.time()
    while len(unseen) !=0:
        if restricted_crawl and len(seen)>20:
            break#满足条件则中断整个循环
        print('\nDistributed Crawling...')
        job1=[pool.apply_async(crawl,args=(url,)) for url in unseen]
        htmls=[k.get() for k in job1]
        
        print('\nDistributed Parsing...')
        parse_h=[pool.apply_async(parse,args=(html2,)) for html2 in htmls]
        results=[g.get() for g in parse_h]
        
        print('\nAnalysing...')
        seen.update(unseen)
        unseen.clear()
        
        for title,urls,present_url in results:#第一次用的是base——url，值返回一个结果【包含，标题，当前链接，整个页面的所有链接】
            print(count,title,present_url)
            count+=1
            unseen.update(urls - seen)

    print("tatol time:%d"%(time.time()-t1))  

#if __name__=="__main__": 
#    unseen = set([base_url,])
#    seen = set()
#    pool = mp.Pool(4)                       
#    count, t1 = 1, time.time()
#    while len(unseen) != 0:                 # still get some url to visit
#        if restricted_crawl and len(seen) > 20:
#                break
#        print('\nDistributed Crawling...')
#        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
#        htmls = [j.get() for j in crawl_jobs]                                       # request connection
#    
#        print('\nDistributed Parsing...')
#        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
#        results = [j.get() for j in parse_jobs]                                     # parse html
#    
#        print('\nAnalysing...')
#        seen.update(unseen)         # seen the crawled
#        unseen.clear()              # nothing unseen
#    
#        for title,urls,present_url in results:
#            print(count, title, present_url)
#            count += 1
#            unseen.update(urls - seen)     # get new url to crawl
#    print('Total time: %.1f s' % (time.time()-t1, ))    # 16 s !!!