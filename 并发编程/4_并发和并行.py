"""
-------------------------------------并发、并行------------------------------------------------------
并发(concurrency):
遇到I/O阻塞时（一般是网络I/O或磁盘I/O），
通过多个thread之间切换执行（多线程） 或
单线程内多个task之间切换执行，
以便最大化利用CPU时间，
但同一时刻，只允许有一个thread或task执行
适合I/O密集型，比如你要从网站上下载多个文件

并行(parallelism)：
多个进程完全同步同时的执行，
比如电脑是 6 核处理器，那么在运行程序时，可以强制Python开6个进程同时执行，加快运行速度
适合CPU密集型业务场景，比如大型计算

CPU-bound的任务主要是multi-processing，
IO-bound的话，如果IO比较快，用多线程，
如果IO比较慢，用asyncio，因为效率更加高

-----------------------------------------同步、异步---------------------------------------------------
同步：sync
操作一个接一个的执行，下一个操作必须等上一个操作完成后才能执行

异步：async
不同操作间可以相互交替执行，如果其中的某个操作被 block了，
程序并不会等待，而是会找出可执行的操作继续执行。
"""
