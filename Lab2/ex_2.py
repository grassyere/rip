#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
#data2 = gen_random(1, 3, 10)

# Реализация задания 2
data2 = Unique(data1)
print(*data2)
print(*sorted(Unique(gen_random(1, 3, 10))))

