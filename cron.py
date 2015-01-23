from pusher import run
import time
from sys import argv
while True:

    run()
    if not argv[1]:
        time.sleep(300) #sleep for five minutes
    else:
        time.sleep(int(argv[1]))
