import time
time.sleep(3) # затормозить код на 3 секунды

# ---------------------------------------------------------------------------

import datetime as dt, sys, os, platform # array, math, random, cmath
print(dt.datetime.now().time().microsecond) # время, дата

print(sys.path)           # путь папки
print(os.name)            # название ОС
print(platform.system())    # ОС

# ---------------------------------------------------------------------------

from math import sqrt as sq,ceil

print(ceil(sq(27)))

# ---------------------------------------------------------------------------

import modules as mod

mod.write_name()
print(mod.custom_sum(5,0,2))
