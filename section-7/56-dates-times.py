import datetime
import time
print(datetime.datetime.now())

yesterday=datetime.datetime(2017,9,9,4,0,0,0)
now = datetime.datetime.now()
delta = now - yesterday
print(delta)
print(delta.total_seconds())

filename=now.strftime("%Y-%m-%d-%H-%M-%S-%f")+"-sample.txt"
def create_file():
    with open(filename,"w") as file:
        file.write("") # Writing empty string

create_file()

print(now+datetime.timedelta(days=2)) # adding 2 days

times = []
for i in range(5):
    times.append(datetime.datetime.now())
    time.sleep(1)

print(times)
