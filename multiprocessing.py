import multiprocessing
import time
from New_find_fibonacci import find_fibonacci

start = time.perf_counter()

proceses = []
for num in range(100):

  p = multiprocessing.Process(target = find_fibonacci, args=[num])
  p.start()

  processes.append(p)

for process in processes:
  process.join()
 

finish = time.perf_counter()

executed_time= round(finish-start, 2)
print(f"Finished in {executed_time} second(s)")