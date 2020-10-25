from collections import deque

MAX_REQUESTS_PER_SECOND = 3
MAX_REQUESTS_PER_TEN_SECONDS = 20
MAX_REQUESTS_PER_MINUTE = 60

class Tracker:
    def __init__(self, time):
        self.time = time
        self.count = 0

    def increment(self):
        self.count += 1
        
    def get_time(self):
        return self.time

    def get_count(self):
        return self.count

def purge_old_times(d, current_time, time_duration):
    lowest_time_allowed = current_time - (time_duration - 1)

    while len(d) > 0 and d[0].get_time() < lowest_time_allowed:
        d.popleft()

def count_dropped_requests(request_times):
    curr_tracker = Tracker(0)

    ten_second_period = deque()
    minute_period = deque()

    total_dropped_requests = 0

    for time in request_times:
        if curr_tracker.get_time() != time:
            curr_tracker = Tracker(time)

            ten_second_period.append(curr_tracker)
            minute_period.append(curr_tracker)

        curr_tracker.increment()

        if curr_tracker.get_count() > MAX_REQUESTS_PER_SECOND:
            total_dropped_requests += 1
            print("Dropped at time [second rate]", time)
            continue
        
        purge_old_times(ten_second_period, time, 10)
        if sum(tracker.get_count() for tracker in ten_second_period) > MAX_REQUESTS_PER_TEN_SECONDS:
            total_dropped_requests += 1
            print("Dropped at time [10-second rate]", time)
            continue
    
        purge_old_times(minute_period, time, 60)
        if sum(tracker.get_count() for tracker in minute_period) > MAX_REQUESTS_PER_MINUTE:
            total_dropped_requests += 1
            print("Dropped at time [minute rate]", time)

    return total_dropped_requests


print(count_dropped_requests([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]))
