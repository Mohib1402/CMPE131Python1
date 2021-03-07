import time

def calculate_time(function):
    def wrapper():
        timebefore = time.time()
        function()
        timeafter = time.time()

        # Prints the time difference before and after the function is implemented
        print(f"Total time {timeafter - timebefore}")
    return wrapper

# Testing Function
@calculate_time
def c1():
    return time.sleep(2)
