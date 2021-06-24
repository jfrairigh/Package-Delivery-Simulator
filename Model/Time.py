from datetime import datetime


# Time complexity = O(1)
# Space complexity = O(1)
class Time:
    def __init__(self, start_hour, start_minute, start_second=0):
        self._hour = start_hour
        self._minute = start_minute
        self._second = start_second

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    def increase_hour(self, num_hrs):
        self._hour += num_hrs

    def increase_minute(self, num_min):
        self._minute += num_min
        self.increase_hour(int(self._minute/60))
        self._minute = self._minute % 60

    def increase_second(self, num_sec):
        self._second += num_sec
        self.increase_minute(int(self._second/60))
        self._second = self._second % 60

    def set_hour(self, hrs):
        self._hour = hrs

    def set_minute(self, minute):
        self._minute = minute

    def __str__(self):
        arbitrary_year = 2021
        arbitrary_month = 1
        arbitrary_day = 15
        return '{:%H:%M:%S}'.format(datetime(arbitrary_year, arbitrary_month, arbitrary_day, self._hour, self._minute, self._second))
