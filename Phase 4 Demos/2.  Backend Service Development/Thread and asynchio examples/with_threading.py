import threading
import time

def task1():
    print("Task 1 Started")
    time.sleep(3)
    print("Task 1 Completed")

def task2():
    print("Task 2 Started")
    time.sleep(3)
    print("Task 2 Completed")

def task3():
    print("Task 3 Started")
    time.sleep(3)
    print("Task 3 Completed")


start = time.time()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Total Time:", time.time() - start)