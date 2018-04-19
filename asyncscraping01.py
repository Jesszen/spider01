# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:53:15 2018

@author: Jess
"""
import time
import requests

base_url="https://morvanzhou.github.io"
"""
def normal():
    for _ in range(2):
        r=requests.get(base_url)
        print(r.url)

t1=time.time()
normal()
print("noraml total time",time.time()-t1)
"""
import aiohttp
import asyncio
import re
from bs4 import BeautifulSoup
import multiprocessing as mp
from urllib.request import urlopen,urljoin
"""
async def job(k):
    response= await k.get(base_url)
    return str(response.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:#官网推荐建立 Session 的形式
        tasks=[loop.create_task(job(session)) for _ in range(2)]
        finished,unfinished=await asyncio.wait(tasks)
        all_results=[r.result() for r in finished]
        print(all_results)
t1=time.time()
loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("aiohttp time",time.time()-t1)
"""
unseen=set([base_url,])
seen=set()

async def crawl(url,sess):
    p=await sess.get(url)
    html=await p.text()
    return html
def parse(k):
    soup=BeautifulSoup(k,"lxml")
    urls=soup.find_all("a",{"href":re.compile(r"^/.+?/$")})
    page_urls=set(urljoin(base_url,e["href"]) for e in urls)
    present_url=soup.find("meta",{'property': "og:url"})["content"]
    title=soup.find("h1").get_text().strip()
    return page_urls,title,present_url

async def main(loop):
    pool=mp.Pool()
    async with aiohttp.ClientSession() as session:
        count=1
        while len(unseen) !=0:
            print("\n async crawl")
            tasks=[loop.create_task(crawl(url,session)) for url in unseen]
            finished,unfinished=await asyncio.wait(tasks)
            htmls=[r.result() for r in finished]
            print("\n parsing")
            results2=[pool.apply_async(parse,(html,)) for html in htmls]
            parse_jobs=[z.get() for z in results2]
            print("\n analysing")
            seen.update(unseen)
            unseen.clear()
            for page_urls,title,present_url in parse_jobs:
                unseen.update(page_urls - seen)
                count +=1

if __name__=="__main__":
    t1=time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print("async total time",time.time()-t1)
    
                  
            
            
            