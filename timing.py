import time

def calculate_time(function):
    def wrapper():
        timebefore = time.time()
        function()
        timeafter = time.time()
        print(f"Total time {timeafter - timebefore}")
    return wrapper

@calculate_time
def c1():
    return time.sleep(2)
