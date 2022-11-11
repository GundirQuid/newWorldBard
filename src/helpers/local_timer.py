from datetime import datetime, timedelta


class Timer:
    def __init__(self, duration_in_milliseconds: int = 0):
        self.duration: int = duration_in_milliseconds
        self.start_time: datetime = datetime.now() - timedelta(seconds=100)
        self.active: bool = False

    def activate(self):
        self.active: bool = True
        self.start_time: datetime = datetime.now()

    def deactivate(self):
        self.active: bool = False
        self.start_time: datetime = datetime(1, 1, 1, 1, 1, 1, 1)

    def update(self):
        if self.active:
            current_time: datetime = datetime.now()
            if (current_time - self.start_time) >= timedelta(milliseconds=self.duration):
                self.deactivate()
