#!/usr/bin/python

import time
import argparse
import os
import sys
import signal

# The default amount of time for pizza cooking (13mins)
default_pizza=780

def sigint_handler(signal, frame):
    sys.exit(0)

def my_usage(progname):
    return progname + ' [-h] [([-H H] [-m m] [-s s]) | --pizza]'

def main():
    parser = argparse.ArgumentParser(description='This is a timer, which makes beeping sound after a configured time', usage=my_usage(os.path.basename(__file__)))
    
    group_time = parser.add_argument_group('Time options')
    group_time.add_argument('-H', type=int, nargs=1, help='number of hours', default=[0])
    group_time.add_argument('-m', type=int, nargs=1, help='number of mintes', default=[0])
    group_time.add_argument('-s', type=int, nargs=1, help='number of seconds', default=[0])
    
    parser.add_argument('--pizza', action='store_true', help='I want to make a pizza!', default=False)
    
    args = parser.parse_args()
    more_than_one_sec=False

    if args.pizza:
        # The pizza parameter is set, so we ignore every given value, and we wait default_pizza amount of time
        time.sleep(default_pizza)
        more_than_one_sec=True
    else:
        # We are not cooking a pizza, so we wait the defiend amount of time
        hours_in_seconds = args.H[0] * 60 * 60
        minutes_in_seconds = args.m[0] * 60
        sum_of_secs = hours_in_seconds + minutes_in_seconds + args.s[0]
        time.sleep(sum_of_secs)
        if sum_of_secs > 0:
            more_than_one_sec=True
    
    if more_than_one_sec:
        for i in range(50):
            print('\r\a', end='')
            sys.stdout.flush()
            time.sleep(0.2)
    else:
        print('No timer was set, thus at least one sec must be defined')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    main()
