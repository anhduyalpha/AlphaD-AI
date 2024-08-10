import itertools
import threading
import time
import sys

#here is the animation
def animate(done):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animate)
    t.start()
    
def main():
    animate()
if __name__ == '__main__':
    main()