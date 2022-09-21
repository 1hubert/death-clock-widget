import os
from datetime import date


def place_value(number):
    return ("{:,}".format(number))


DEATH_DATE = date(2093, 7, 9)
DEATH_CLOCK_PATH = "c:\\Users\\Hubert\\Desktop"

delta = DEATH_DATE - date.today()
remaining_days = delta.days

script_location = os.path.dirname(__file__)
with open(script_location + '\\current_count.txt', 'r+') as f:
    current_count = int(f.readline().strip())

    if current_count != remaining_days:
        old_filename = DEATH_CLOCK_PATH + '\\' + str(place_value(current_count))
        new_filename = DEATH_CLOCK_PATH + '\\' + str(place_value(remaining_days))
        os.rename(old_filename, new_filename)
        f.seek(0)
        f.write(str(remaining_days) + "                                      ")
