#import time dan find_fibonacci
import time
from New_find_fibonacci import find_fibonacci

#code perhitungan waktu, untuk menjalankan fungsi argument dari 1-100
start = time.perf_counter()
for a in range(1,101):
  print(find_fibonacci(a))

finish = time.perf_counter()

executed_time= round(finish-start, 2)
print(f"Finished in {executed_time} second(s)")