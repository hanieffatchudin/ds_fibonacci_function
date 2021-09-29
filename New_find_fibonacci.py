
    # write your code here
fibonacci = []
def angka_fibo(n):
   if n <= 1:
       return n
   else:
       return(angka_fibo(n-1) + angka_fibo(n-2))

for i in range(20): #disini nilai 20 menunjukan ada 20 angka fibonacci, bisa ganti sesuai kebutuhan
  fibonacci.append(angka_fibo(i))

def find_fibonacci(a):
  if a in fibonacci:
    return True
  else :
    return False
    #code diatas dapat menentukan apakah angka tersebut bilang fibonacci atau bukan

    print(find_fibonacci(1))
    print(find_fibonacci(10))
    print(find_fibonacci(11))
