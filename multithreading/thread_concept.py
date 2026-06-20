'''
what is a program?
a program is a set of instructions
stored on a disk

print("hello")


storing on a disk???

python hello.py
hello

what is processs?
when a program starts executing it becomes
a procees
running?
python hello.py
hello


os --operating system

chrome:
vs code:
spotify:
each one is a separate process



characteristics:
1.Independent
2.separate memory:
chrome:1.8GB,vs-code-500MB
3.Heavy a Weight:
Memory allocations
resoures allocation
cpu scheduling

what is a thread?
A thread is smallest unit of execution inside a process

Restaurant==process
workers inside res = threads


worker1-taking the orders
worker2-cooking
worker3-
worker4-cleaning



visually:
process:
chrome:
  +thread1
  +thread2
  +thread3



process                 thread
1.independent           part of process
2.heavy weight          light weight
3.separate memory        shared memory
4.slow                    fast
5.expensive               cheap
6.communication           difficult easy  

why threads are faster?
threads will share the memory
process needs separate memory allocation


concurrency?
teacher checking the notebooks
student A
student B
student C



concurrency:
A
B
C
A
B
C
one at a time
rapidly switching
appears simultaneously
cpu -->only one

parallelism:
cashier1-->customer 1
cashier2-->customer 2
cashier3-->customer 3
truly simultaneous
 cpu1-->taska
 cpu2-->taskb
 cpu3-->taskc

 A
 B
 A
 B
 A
 B


 Parallelism:
 cpu1-AAA
 cpu2-BBB


 one chef cooking?

 soup
 noodles
 fried rice


 parallelism:

 chef1-soup
 chef2-noodles
 chef3-fried rice

 python threads will use---concurrency
 due to GIL-Global Interpreter  lock

'''
#creation of threads:
# import threading

# #function created(do's nothing)
# def display():
#     print("hello")
# #tread object(creation)    
# t=threading.Thread(target=display)
# #start thread
# t.start()


# #multiple threads:
# import threading
# def task():
#     print("thread running")
# t1=threading.Thread(target=task)    
# t2=threading.Thread(target=task)  
# t3=threading.Thread(target=task) 

# t1.start()
# t2.start()
# t3.start()

# '''
# main thread
#    + t1
#    + t2
#    + t3


#    all executes independently

# '''
# #treads with loops:
# def numbers():
#     for i in range(5):
#         print(i)
# t=threading.Thread(target=numbers)
# t.start()


# #two threads with diff task
# def even():
#     for i in range(0,10,2):
#         print("even:",i)
# def odd():
#     for i in range(1,10,2):
#         print("odd:",i)
# t1=threading.Thread(target=even)
# t2=threading.Thread(target=odd)
# t1.start()
# t2.start()   
# '''
# os scheduler decides:
# which thread to runs first?

# '''
# import threading
# print(threading.current_thread())

# #naming of threads:
# import threading
# def task():
#     print(threading.current_thread().name)
# t=threading.Thread(target=task,
#                    name="student_thread")
# t.start()    


#passing arguments
import threading
def square(n):
    print(n*n)
t=threading.Thread(target=square,
                   args=(5,))
t.start()    

#to delay the threads
import time
print("start")
time.sleep(5)
print("end")

def task():
    for i in range(5):
        print(i)
        time.sleep(1)
t=threading.Thread(target=task)
t.start()




#retry mechanism
# while True:
#     try:
#         connect()
#     except:
#         time.sleep(5) 




