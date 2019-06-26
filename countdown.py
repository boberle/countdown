import time, argparse, subprocess

step = 30
minutes = 10
invert = False

def parse_args():
    # definition
    parser = argparse.ArgumentParser(description="show a countdown v.1.1.0")
    # arguments (not options)
    parser.add_argument("time", type=int, default=10,
        help="total amount of time (min)")
    # options
    parser.add_argument("-s", "--step", dest="step", type=int, default=30,
        help="step (seconds), def = 30")
    parser.add_argument("-a", "--alarm", dest="alarm", action="store_true",
        default=False, help="invert the color of the screen")
    # reading
    args = parser.parse_args()
    global step, minutes, invert
    minutes = args.time
    step = args.step
    invert = args.alarm

parse_args()

seconds = minutes * 60
print("Ctrl-C to pause...")
while seconds > 0:
    try:
        if not seconds % step:
            print("%02d:%02d" % (seconds // 60, seconds % 60))
        time.sleep(1)
        seconds -= 1
    except KeyboardInterrupt:
        try:
            input("Ctrl-C to stop, Enter to continue...")
        except KeyboardInterrupt:
            print()
            invert = False
            break

if invert:
    subprocess.run(('xcalib', '-a', '-i'), check=True)
    input("press Enter to restore the screen")
    subprocess.run(('xcalib', '-a', '-i'), check=True)

print("done!")

