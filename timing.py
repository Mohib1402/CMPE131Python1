import time

def calculate_time(function):
    timebefore = time.time()
    function()
    timeafter = time.time()
    print(f'Total time {timeafter - timebefore}')
