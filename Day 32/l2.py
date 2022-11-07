import datetime as dt

now = dt.datetime.now()
year = now.year

print(year)

#creating from scratch
date_of_birth = dt.datetime(year=2002, month=6, day=18)
print(date_of_birth)
