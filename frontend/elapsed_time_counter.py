import datetime


class ElapsedTime:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_counting(self):
        self.start_time = datetime.datetime.now()

    def stop_counting(self):
        self.end_time = datetime.datetime.now()

    def get_seconds(self):
        elapsed_time = round((self.end_time - self.start_time).total_seconds(), 1)
        return elapsed_time
