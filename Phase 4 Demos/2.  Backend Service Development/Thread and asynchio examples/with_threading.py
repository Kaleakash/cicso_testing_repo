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
    time.sleep(5)
    print("Task 3 Completed")


start = time.time()

t1 = threading.Thread(target=task1) # thread reference for task1
t2 = threading.Thread(target=task2) # thread reference for task2
t3 = threading.Thread(target=task3) # thread reference for task3

t1.start()          # thread ready to run 
t2.start()          # thread ready to run 
t3.start()          # thread ready to run 

# t1.join()
# t2.join()
# t3.join()
# need to execute below line code after all thread destroyed
t1.join()  # wait for t1 to finish
t2.join()  # wait for t2 to finish
t3.join()  # wait for t3 to finish
print("Total Time:", time.time() - start)