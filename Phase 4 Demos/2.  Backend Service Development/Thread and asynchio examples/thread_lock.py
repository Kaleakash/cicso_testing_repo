import threading
import time
avl = 2
# write the code using thread safe with locking concept
lock = threading.Lock()
def ticket_booking():
    print(f"Ticket booking requested by {threading.current_thread().name}")
    time.sleep(2)
    global avl
    with lock:
        if avl > 0:
            print(f"Ticket booking started by {threading.current_thread().name}")
            time.sleep(1)
            avl -= 1
            print(f"Ticket booking completed by {threading.current_thread().name}")
        else:
            print(f"Tickets sold out for {threading.current_thread().name}")


# set the custom name for the thread 
t1 = threading.Thread(target=ticket_booking, name="Raj") # thread reference for task1
t2 = threading.Thread(target=ticket_booking, name="Ravi") # thread reference for task2
t3 = threading.Thread(target=ticket_booking, name="Ajay") # thread reference for task3
t4 = threading.Thread(target=ticket_booking, name="Vijay") # thread reference for task4
t1.start()          # thread ready to run 
t2.start()          # thread ready to run 
t3.start()          # thread ready to run 
t4.start()          # thread ready to run 

