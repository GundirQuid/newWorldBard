from datetime import datetime, timedelta


class Timer:
    def __init__(self, duration_in_milliseconds: int = 0, function=None):
        self.duration = duration_in_milliseconds
        self.function = function
        self.start_time = datetime.now() - timedelta(seconds=100)
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = datetime.now()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        if self.active:
            current_time = datetime.now()
            if (current_time - self.start_time) >= timedelta(milliseconds=self.duration):
                if self.function and self.start_time != 0:
                    self.function()
                self.deactivate()
