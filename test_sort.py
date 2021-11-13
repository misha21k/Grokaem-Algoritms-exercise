import time
import random
from quick_sort import quick_sort
from selection_sort import selection_sort
from kasatov_sort import kasatov_sort
from bubble_sont import bubble_sort
from merger_sort import merger_sort

size = 100000
a = [random.randint(1, size) for i in range(size)]
time1 = time.time()
b = merger_sort(a)
time2 = time.time()
print(time2 - time1)
