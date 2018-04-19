# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:51:31 2018

@author: Jess
"""
####后来检查得知我源代码的名称也是multiprocessing.py，判断有可能循环导入了自己的这段代码。
#import multiprocessing as mp
#def job(a,d):
#    print('aaaaa')
#
#if __name__=='__main__':
#    p1 = mp.Process(target=job,args=(1,2))
#    p1.start()
#    p1.join()
import multiprocessing as mp
"""
def job(a,d):
    print('aaaaa')

if __name__=='__main__':
    p1 = mp.Process(target=job,args=(1,2))
    p1.start()
    p1.join()
"""
#Queue的功能是将每个核或线程的运算结果放在队里中， 等到每个线程或核运行完毕后再从队列中取出结果，
# 继续加载运算。原因很简单, 多线程调用的函数不能有返回值[即不能有return], 所以使用Queue存储多个线程运算的结果


def job1(b):#定义一个被多线程调用的函数，b就像一个队列，用来保存每次函数运行的结果
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    b.put(res)
if __name__=="__main__":
    q=mp.Queue()#定义一个多线程队列，用来存储结果
    p1=mp.Process(target=job1,args=(q,))#定义两个线程函数，用来处理同一个任务,
    p2=mp.Process(target=job1,args=(q,))#args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的
    p1.start()#分别启动、连接两个线程 
    p2.start()
    p1.join()
    p2.join()
    res1=q.get()#上面是分两批处理的，所以这里分两批输出，将结果分别保存
    res2=q.get()
    print(res1+res2)