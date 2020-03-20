from datetime import datetime, date, timedelta
import time

DURATION = 1
stop_at = timedelta(minutes=DURATION)
now = datetime.now()
stop = now + stop_at
print (f'Started Pomodoro for {DURATION} mins')
while 1:
    current = datetime.now()
    print (current)
    if current >= stop:
        print('Pomodoro timer done!')
        exit(0)
    time.sleep(1)
