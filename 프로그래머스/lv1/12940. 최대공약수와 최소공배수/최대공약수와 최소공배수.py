def solution(n, m):
    answer = []
    def GCD(n, m):
      while m:
          n, m = m, (n % m)
      answer.append(n)
      return n
    answer.append((n*m)//GCD(n,m))
    return answer