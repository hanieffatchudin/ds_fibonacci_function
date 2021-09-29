import threading
import time
from New_find_fibonacci import find_fibonacci

start = time.perf_counter()

threads = []
for a in range(100):

  t = threading.Thread(target = find_fibonacci)
  t.start()

  threads.append(t)

for thread in threads:
  thread.join()
 

finish = time.perf_counter()

executed_time= round(finish-start, 2)
print(f"Finished in {executed_time} second(s)")