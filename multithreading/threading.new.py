'''
join():mainthread->owner
   worker thread ->worker



'''
import threading
import time
def task():
    time.sleep(3)
    print("thread finished")
t=threading.Thread(target=task)
t.start()
t.join()
print("main thread ends here")    

#multiple threads with join

def task(name):
    print(name,"started")
    time.sleep(2)
    print(name,"finished")
t1=threading.Thread(
    target=task,args=("a",)
)    
t2=threading.Thread(
    target=task,args=("a",)
)    
t1.start()
t2.start()
t1.join()
t2.join()
print("all threads completed")

#example on naming threads
def task():
    print(threading.current_thread().name,"started")
    time.sleep(2)
    print(threading.current_thread().name,"finished")
t1=threading.Thread(target=task,name="download thread")  
t2=threading.Thread(target=task,name="upload thread")
t1.start()
t2.start()    
