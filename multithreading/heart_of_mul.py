'''
1.Race Condition
2.Synchronization
3.Lock
4.Rlock

'''
#why we need synchronization?
'''
balance=1000
thread-1--withdraw 500
thread-2--withdraw 700

both are accessing the same variable
without proper control

incorrent balance
wrong transactions
data corrrupt

to aviod the we will use:
synchronization:
this is a process of controlling
access to shared resources so 
that only one thread modifies at a time

lock:
shared
resoures:any variable,file,database,object

example:
count=0
if multiple threads modifies count simultaneously

#race condition:
occurs when multiple threads access and modify
shared data simultaneously causing unpredictable outputs




count=0
count+=1
print(count)
#write with thread
import threading
count=0
def increament():
    global count
    count+=1
threads=[]
for i in range(10):
    t=threading.Thread(target=increament)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(count) 

10
9
10

'''
'''
critical section:
code section where shared resources are
accessed is called critical section
count+=1-->critical section

To avoid the race condition?
one thread should enter critical section at a time:

solution:lock
 what is a lock?
 synchoronization mechanism
 that allows only one thread to execute
 a critical section at a time


 Tread A acquires lock
 other threads will wait
 thread A releases lock
 next thread gets lock


 import threading
 lock=threading.lock()

 #to apply lock
 lock.acquire()


 #to release
 lock.release()

'''
import threading
count=0
lock=threading.Lock()
def increament():
    global count
    for i in range(10000):
        
        with lock:
        #critical section
            count+=1
        
        
t1=threading.Thread(target=increament)
t2=threading.Thread(target=increament)
t1.start()
t2.start()

t1.join()
t2.join()
print(count)


# #bank example
class bank:
    def __init__(self):
        self.balance=1000
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
#t1=500
#t2=700    #negative   
# 
import threading
class Bank:
    def __init__(self):
        self.balance=1000
        self.lock=threading.Lock()
    def withdraw(self,amount):
        with lock:
            if self.balance>=amount:
                self.balance-=amount
                print(amount,"withdraw")
            else:
                print("insufficient balance")
bank=Bank()
a1=threading.Thread(
    target=bank.withdraw,
    args=(700,)
)
a2=threading.Thread(
    target=bank.withdraw,
    args=(500,)
)
a1.start()
a2.start()

a1.join()
a2.join()
print(bank.balance)
'''
deadlock:
where the threads wait forever for locks
thread 1:
lockA
waiting for lock B

thread2:
lock B
waiting for lock A

thread 1-->waiting lock A
thread 2-->waiting lock B
deadlock


Rlock:Recursive lock
A thread can aquire the same
lock multiple times

why Rlock:
normal lock
acquire once
release once


if same thread acquires again
deadlock



'''
# import threading
# lock=threading.Lock()
# def outer():
#     lock.acquire()
#     inner()
#     lock.release()
# def inner():
#     lock.acquire()
#     print("inner")
#     lock.release()
# outer()
'''
outer() acquired the lock
inner() trying to acquire the same lock
lock is already head above
wait forever
'''        
lock=threading.RLock()
def inner():
    with lock:
        print("Inner")
def outer():
    with lock:
        print("outer")
        inner()
outer()
'''
outer acquire
count=1
inner acquire
count=2
inner release the lock
count=1
outer release the lock
count=2


'''        
