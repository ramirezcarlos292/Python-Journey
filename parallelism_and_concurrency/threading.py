import threading
import time

def count_numbers():
    for i in range(1, 41):
        print(f"Counting {i}")
        time.sleep(1)
    
def print_message():
    for _ in range(40):
        print("Hello for the other thread!")
        time.sleep(1.5)

# Create threads
thread1 = threading.Thread(target=count_numbers)
thread2 = threading.Thread(target=print_message)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads completed!")