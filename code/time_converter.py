import time


def get_time():
    """REturn current time  forman HH:MM:SS"""
    return time.strftime("%H:%M:%S", time.localtime())

def time_converter(input_time):
    """ count time in seconds from HH:MM:SS format"""
    if len(input_time) == 8:
        # HH:MM:SS
        time_format = "%H:%M:%S"
    elif len(input_time) == 5:
        # HH:MM
        time_format = "%H:%M"
    elif len(input_time) == 7:
        # HH:MM AM/PM
        time_format = "%I:%M %p"
    elif len(input_time) == 8 and input_time[2] == ":":
        # HH:MM:SS AM/PM
        time_format = "%I:%M:%S %p"
    else:
        print("Invalid time format")
        return
    try:
        # Convert the input time to seconds
        time_in_seconds = int(time.mktime(time.strptime(input_time, time_format)))
        print(f"Time in seconds: {time_in_seconds}")
    except ValueError:
        print("Invalid time format")
   
        
def time_to_sec(input_time):
    """ count time in seconds from HH:MM:SS format"""
    time_list = list(map(int, input_time.split(":")))
    print(f"Time in seconds: {sum(x * 60 ** i for i, x in enumerate(reversed(time_list)))}")


if __name__ == '__main__':
    
    current_time = get_time()
    print(f"Current time is {current_time}")
    time_converter(current_time)
    time_converter("12:30:45")
    time_to_sec("12:30:45")
    # time_converter("12:30")
    # time_converter("12:30:45 AM")
    # time_converter("12:30 AM")
    # time_converter("12:30 PM")
    # time_converter("12:30:45 PM")
    # time_converter("12:30 PM")
    # time_converter("12:30:45 AM")