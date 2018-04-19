# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:30:51 2018

@author: Jess
"""
import time
import asyncio
#def job(t):
#    print("start",t)
#    time.sleep(t)
#    print("job",t,"takes",t)
#    
#def main():
#    [job(i) for i in range(1,3)]
#t1=time.time()
#main()
#print("no async total time",time.time() -t1)

async def job(t):#将产生协程对象
    print("start",t)
    await asyncio.sleep(t)#await  表示可以切换其他任务
    print("job",t,"takes",t)

async def main(loop):
    tasks=[loop.create_task(job(t)) for t in range(1,3)]#创建任务,create_task函数创建了一个任务对象
    await asyncio.wait(tasks)#执行并等待所有任务完成！！！！！！！加await 原因可能是一下？
    #asyncio.wait()函数会确保一切传递是future，这意味着如果你传递协程，
    #你将很难找出协程结束还是待定，因为输入对象与输出对象不再匹配。
"""
协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。
协程对象需要注册到事件循环，由事件循环调用。
直接调用协程函数，协程并不会开始运行，只是返回一个协程对象
==============================================================================
注意，协程中不能有阻塞型函数，非阻塞型函数需要全部加上yield from，time模块的sleep()函数是阻塞型的，
这里不能用，必须换成asyncio.sleep()。
使用time.sleep()函数的后果是线程被阻塞，结果整个事件循环被冻结，无法正常运行（因为协程中只有1个线程在工作）

*******************************************************************************
一个协程函数不能直接调用运行，只能把协程加入到事件循环loop中。
asyncio.get_event_loop方法可以创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并启动事件循环。
--------------------------------------------------------------------------------
future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权。
协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行。
-------------------------------------------------------------------------------
task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。

Task是Future的一个子类，也是协程的一个框架。Task可以让你记录到任务结束处理的时间。
由于任务是Future类型，其它的协程可以等待一个任务，当任务处理完毕时你也可以获取到它的结果。

创建了我们的事件循环，并且通过事件循环对象的create_task函数创建了一个任务对象。
函数create_task接受我们想要转换为任务的函数。
然后我们运行事件循环，直到任务完成。
在最后，一旦任务结束，我们就获得任务的结果。
************************************************************
event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。
当满足事件发生的时候，调用相应的协程函数。

--------------------------------------------------------
你必须使用return或者await语句，用于将返回值返回给调用者。
关键字await只能在async def函数中使用
关键字async和await可以认为是异步编程中的接口
"""
    
t1=time.time()

loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))

"""
run_until_complete 是一个阻塞（blocking）调用，直到协程运行结束，它才返回。这一点从函数名不难看出。
run_until_complete 的参数是一个 future，但是我们这里传给它的却是协程对象，
之所以能这样，是因为它在内部做了检查，通过 ensure_future 函数把协程对象包装（wrap）成了 future。

loop.run_until_complete 只接受单个 future。

"""
#loop.close()
print("async total time",time.time() -t1)