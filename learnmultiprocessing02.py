# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:27:10 2018

@author: Jess
"""

import multiprocessing as mp
import threading as td
import time

def job(b):
    res=0
    for i in range(1000000):
        res+=i+i**2+i**3
    b.put(res)#process  禁止出现返回值
    
def normal():
    res=0
    for n in range(2):
        for i in range(1000000):
            res+=i+i**2+i**3
    print("normal",res)

def multicore():
    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))
    p2=mp.Process(target=job,args=(q,))
    p1.start()#两个进程要都先start
    p2.start()#两个进程要都先start
    p1.join()
    p2.join()
    res1=q.get()
    res2=q.get()
    print("multicore",res1+res2)
    
def thread():
    q=mp.Queue()
    t1=td.Thread(target=job,args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)
"""            
if __name__=="__main__":
    st=time.time()
    normal()
    st1=time.time()
    print("normal",st1-st)
    multicore()
    st2=time.time()
    print("multicore",st2-st1)
    thread()
    st3=time.time()
    print("thread",st3-st2)
"""
#pool

def job2(x):
    return x*x #进程池pool,需要被调用的函数有返回值

def multipool():
    pool=mp.Pool()#定义一个进程池
    k=pool.map(job2,range(10))#map ,把函数，和传入值放进去
    print(k)
    h=pool.apply_async(job2,(2,))#每次只能运行一个，除非迭代
    print(h.get())
    g=[pool.apply_async(job2,(i,)) for i in range(10)]#(i,)，要有个，表示可迭代，否则报错
    print([z.get() for z in g])#只能放入一组参数，并返回一个结果，如果想得到map()的效果需要通过迭代
#if __name__=="__main__":
#    multipool()
    
    
"""
共享内存
进程锁
"""
def plus(v,num,l):#定义多进程被调用函数
    l.acquire()#锁住共享，防止不同进程之间争抢共享内存
    for _ in range(10):
        time.sleep(0.1)#间隔0.1s
        v.value +=num
        print(v.value)
    l.release()
def mul():
    l=mp.Lock()
    v=mp.Value("i",0)
    p1=mp.Process(target=plus,args=(v,1,l))
    p2=mp.Process(target=plus,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__=="__main__":
    mul()