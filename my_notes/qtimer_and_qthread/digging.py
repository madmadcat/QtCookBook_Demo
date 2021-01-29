import itertools
import codecs
import random
import bisect
import time
import os

class Ore:
    def __init__(self, sec):
        self.second = sec
        self.goldnum = 0
        self.start = time.clock()

        if os.path.exists('gold.gd'):
            with codecs.open('gold.gd', 'w', 'utf-8') as f:
                f.write('\x00')

    def digging(self):
        ore_list = [i for i in range(256)]
        weights = [100 for i in range(256)]
        weights[170] = 5
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        isgold = ore_list[bisect.bisect(cumdist, x)]
        with codecs.open('gold.gd', 'a', 'utf-8') as f:
            f.write(chr(isgold))
        if isgold == 170:
            return 1
        else:
            return 0

    def begin_dig(self):
        while True:
            gold = self.digging()
            if gold == 1:
                self.goldnum += 1
            end = time.clock ()
            besec = int(end - self.start)
            if besec == self.second:
                break
        return self.goldnum