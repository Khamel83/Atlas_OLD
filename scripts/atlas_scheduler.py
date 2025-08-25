#!/usr/bin/env python3
import time
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', action='store_true')
    args = parser.parse_args()

    if args.start:
        print('Scheduler started.')
        while True:
            time.sleep(60)