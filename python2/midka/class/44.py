class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minutes = self.seconds // 60
        remaining_seconds = self.seconds % 60
        return f'{minutes}:{remaining_seconds:02}'

    def convert_to_hours(self):
        hours = self.seconds // 3600
        remaining_minutes = (self.seconds % 3600) // 60
        remaining_seconds = self.seconds % 60
        return f'{hours}:{remaining_minutes:02}:{remaining_seconds:02}'

time_obj = Time(230)

print(time_obj.convert_to_minutes())  
print(time_obj.convert_to_hours())   
