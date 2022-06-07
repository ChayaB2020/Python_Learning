import threading
x=0

def increment(num):
    global x
    x+=1

def taget_func():
    global x
    for i in range(100000):
        increment(i)
    
def main_func():
    global x
    x=0

    t1=threading.Thread(target=taget_func)
    t2=threading.Thread(target=taget_func)
    t1.start()
    t2.start()

    print("After calling threads")

    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_func()
        print("Iteration {0}: x = {1}".format(i,x))