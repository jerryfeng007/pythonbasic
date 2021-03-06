"""
--------------------------------多线程、协程之间的共同点和区别-----------------------------------------
共同点：
都是并发操作，都适用于I/O密集型场景
多线程同一时间点只能有一个线程在执行
协程同一时间点只能有一个任务在执行

不同点：
多线程，是在I/O阻塞时通过切换线程来达到并发的效果
在什么情况下做线程切换是由操作系统来决定的，开发者不用操心，但会造成race condition；

协程，只有一个线程，在I/O阻塞时通过在线程内切换任务来达到并发的效果，
在什么情况下做任务切换是开发者决定的，不会有race condition的情况；
开发者要提前知道一个任务的哪个环节会造成I/O阻塞，然后把这个环节的代码异步化处理，
并且通过await来标识在任务的该环节中断该任务执行，从而去执行下一个事件循环任务。

多线程的线程切换比协程的任务切换开销更大；
线程数不能无限增加
对于开发者而言，多线程并发的代码比协程并发的更容易书写。
一般情况下协程并发的处理效率比多线程并发更高

"""


