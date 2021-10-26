import os
from datetime import date


def place_value(number): 
    return ("{:,}".format(number))


current_date = date.today()
death_date = date(2093, 7, 9)
delta = death_date - current_date
remaining_days = delta.days

with open('c:\\Users\\Hubert\\Documents\\Projekty Python\\2020.04\\1 - days to DEATH counter in a pseudo-widget format\\current_count.txt', 'r+') as f:
    current_count = int(f.readline().strip())

    if current_count != remaining_days:
        old_filename = "c:\\Users\\Hubert\\Desktop\\" + str(place_value(current_count))
        new_filename = "c:\\Users\\Hubert\\Desktop\\" + str(place_value(remaining_days))
        os.rename(old_filename, new_filename)
        f.seek(0)
        f.write(str(remaining_days) + "                                      ")


