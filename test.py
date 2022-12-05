import sys, time

print('hello world', file=sys.stdout)

time.sleep(1)

sys.stdout.flush()

time.sleep(2)