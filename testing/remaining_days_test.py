from datetime import date
f_date = date.today()
l_date = date(2093, 7, 9)
delta = l_date - f_date
print(delta.days)