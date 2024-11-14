import sys
input = sys.stdin.readline

n= int(input())
# fibo(n) = fibo(n-1) + fibo(n-2) (단 n>=2)
def fibo(n):
  # 리턴 조건
  if n<=1:
    return n
  #탐색 조건
  return fibo(n-1) + fibo(n-2)
print(fibo(n))
