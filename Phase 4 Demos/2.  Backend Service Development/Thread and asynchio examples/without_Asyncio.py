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

task1()
task2()
task3()

print("Total Time:", time.time() - start)