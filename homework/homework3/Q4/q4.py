from datetime import datetime, timedelta
import jdatetime
input_str = input("Enter Your Birthday In This Format yyyy-mm-dd HH:MM:SS: ")
# input_str = '2001-06-13 14:30:10'

birthday = datetime.strptime(input_str, '%Y-%m-%d %H:%M:%S')
age_second = (datetime.now() - birthday).total_seconds()
print(f"The total number of seconds that have passed is {age_second} seconds")

next_birthday = birthday + timedelta(days=365)
lef_day = (datetime.now() - next_birthday).days
lef_min = (next_birthday - datetime.now()).seconds // 60
print(f"The Number of days left are {lef_day} and The Minutes left are {lef_min} minutes")

birthday_jalali = jdatetime.datetime.fromgregorian(datetime=birthday)
print('Your Birthday In Jalali Calender',birthday_jalali)