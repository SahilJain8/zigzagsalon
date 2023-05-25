from datetime import datetime,timedelta
from customerapp.models import Appointment

def calculate_end_time(start_time, duration):
    start_time_t=datetime.strptime(start_time, '%H:%M').time()
    start_time_seconds = start_time_t.hour*3600 + start_time_t.minute*60 + start_time_t.second
    duration_in_seconds = int(duration.total_seconds())
    end_time_seconds = start_time_seconds + duration_in_seconds
    hours, remainder = divmod(end_time_seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    time_str = f"{hours:02d}:{minutes:02d}"
    
    return time_str
def convert_to_12_hour_format(time_str):
    # Convert the time string to a datetime object
    time_obj = datetime.strptime(time_str, '%H:%M:%S').time()

    # Format the time in 12-hour format with "AM" and "PM" indicators
    formatted_time = time_obj.strftime('%I:%M %p')

    return formatted_time
def timeslot_gen(start,end):
    start_time = datetime.strptime(start, '%I:%M %p')
    end_time = datetime.strptime(end, '%I:%M %p')
    interval = timedelta(minutes=15)
    time_slots = []
    current_time = start_time
    while current_time <= end_time:
        time_slots.append(current_time.strftime('%I:%M %p'))
        current_time += interval
    return time_slots

def timeslot_gen_tf(start, end):
    start_time = datetime.strptime(start, '%I:%M %p')
    end_time = datetime.strptime(end, '%I:%M %p')

    time_slots = []
    current_time = start_time

    while current_time <= end_time:
        time_slot = current_time.strftime('%H:%M')
        time_slots.append(time_slot)
        current_time += timedelta(minutes=15)

    return time_slots