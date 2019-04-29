import time

def timer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return  warpper



@timer
def test1():
    time.sleep(3)
    print("in the test1")

