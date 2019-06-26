import time, argparse

step = 30
minutes = 10

def parse_args():
    # definition
    parser = argparse.ArgumentParser(description="show a countdown")
    # arguments (not options)
    parser.add_argument("time", type=int, default=10,
        help="total amount of time (min)")
    # options
    parser.add_argument("-s", "--step", dest="step", type=int, default=30,
        help="step (seconds), def = 30")
    # reading
    args = parser.parse_args()
    global step, minutes
    minutes = args.time
    step = args.step

parse_args()

seconds = minutes * 60
while seconds > 0:
    if not seconds % step:
        print("%02d:%02d" % (seconds // 60, seconds % 60))
    time.sleep(1)
    seconds -= 1

