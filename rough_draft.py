class HourClock:

    def __init__(self, hour=0):
        self.hour = hour

    @property
    def hours(self):
        return self.hour

    @hours.setter
    def hours(self, other):
        self.hour = other % 12
        if self.hour < 0:
            self.hour = 0



clock = HourClock()
print(clock.hours)
clock.hours += 5
print(clock.hours)
clock.hours += 5
print(clock.hours)
clock.hours += 5
print(clock.hours)
clock.hours -= 4
print(clock.hours)




