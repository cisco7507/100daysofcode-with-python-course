#! env python
from datetime import datetime, timedelta, date
import requests


def get_log_file(log_url, log_file):
    # Transfer log file from web_url to a local file
    try:
        r = requests.get(log_url)
        with open(log_file, 'w') as f:
            f.write(r.text)
        return
    except Exception as err:
        print(f'Error: {err}')
        exit(1)


def get_time_stamps(log_file):
    try:
        with open(log_file, 'r') as f:
            for line in f:
                if 'shutdown initiated' in line.lower():
                    line_time_stamp = line.split()[1]
                    line_time_stamp_obj = datetime.strptime(line_time_stamp, '%Y-%m-%dT%H:%M:%S')
                    yield line_time_stamp_obj
    except Exception as err:
        print(f'Error:{err}')


if __name__ == '__main__':
    log_url = 'https://bites-data.s3.us-east-2.amazonaws.com/messages.log'
    local_log_file = 'log_file.txt'
    log_file = get_log_file(log_url, local_log_file)

    shutdown_initiated_time_stamps = [time_stamp for time_stamp in get_time_stamps(local_log_file)]
    if shutdown_initiated_time_stamps:
        delta = shutdown_initiated_time_stamps[-1] - shutdown_initiated_time_stamps[0]
        print(f'The time delta between the relevant events is: {delta}')
    else:
        print(f'No shutdown initiated events found in the log file: {local_log_file}')
