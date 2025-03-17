import time
import datetime

timestamp = float(time.strftime('%H.%M'))
# timestamp = 20
# noon = time.strftime('%H')
# print(type(noon))
print(timestamp)
# print(noon)

if 6 <= timestamp < 12:
    print("GoodMorning")
elif 12 <= timestamp < 18:
    print("GoodAfternoon")
elif 18 <= timestamp < 20:
    print("GoodEvening")
else:
    print("GoodNight")




