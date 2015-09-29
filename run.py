#!/usr/bin/python
import time
import sys

# Time Definitions
seconds_minute = 1
minutes_hour = 60
hours_day = 24

# Task Definitions
task_time = 25
break_time = 5

# UI Definitions
progress_bar_length = 40

def alert():
    print ('\a')

def progress(count, total, suffix=''):
    filled_len = int(round(progress_bar_length * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (progress_bar_length - filled_len)
    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

def print_help():
    print("Help")

# Initial Entry into Program; Clear Screen
print(chr(27) + "[2J")

while True:
    # Task Loop
    for i in range(0, task_time):
        time.sleep(seconds_minute)
        progress(i,task_time,'Task Time Elapsed: %s:00' % i)
    alert()
    # Break Loop
    for i in range(0, break_time):
        time.sleep(seconds_minute)
        progress(i,break_time,'Break Time Elapsed: %s:00' % i)
    alert()





