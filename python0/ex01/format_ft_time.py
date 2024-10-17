import time
from datetime import date

epoch_time = int(round(time.time() * 10000)) / 10000
first_str = "Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation".format(epoch_time, epoch_time)
today = date.today()
second_str = today.strftime("%b %d %Y")

print(first_str)
print(second_str)