import threading
import time
def student(name):
    print(name,"started exam")
    time.sleep(3)
    print(name,"submitted paper")
t1=threading.Thread(
    target=student,
    args=("ak",),
    name="student-1"    
) 
t2=threading.Thread(
    target=student,
    args=("anandkishore",),
    name="student-2"
)
t1.start()
t2.start()
print("exam is completed")
