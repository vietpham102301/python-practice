from datetime import datetime

str_input = str(input())
date_time = datetime.strptime(str_input, "%Y-%m-%d %H:%M:%S.%f")

extract_infor = lambda dt: (dt.year, dt.month, dt.day, dt.strftime("%H:%M:%S.%f"))

year, month, day, time = extract_infor(date_time)

print(year)
print(month)
print(day)
print(time)
