import time
import threading


def fun1():
    while True:
        print("Monitoring .......")
        time.sleep(1)


t1 = threading.Thread(target=fun1, daemon=True)

t1.start()
t1.join()
print("I'm in the main program")
