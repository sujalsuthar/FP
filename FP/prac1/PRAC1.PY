import datetime
import calendar

birthdate = datetime.date(1947, 6, 5)

today = datetime.date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print(calendar.month(1947, 6))
print("shyam grandfather age is", age)