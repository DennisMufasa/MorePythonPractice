import time

print(time.asctime())
print(time.timezone)

from time import asctime, localtime, sleep
print(asctime())
sleep(5)
print(localtime())

