def get_divisor(B):
    B = int(B)
    divisors = []

    for i in range(1, B):
        if (B % i == 0):            
            divisors.append(i)            

    return divisors

while True:
  k = int(input())
  if k == -1:
    break

  if sum(get_divisor(k)) == k:
    print(k, "=", end=" ")
    print(*get_divisor(k), sep=" + ")
  else:
    print(f"{k} is NOT perfect.")