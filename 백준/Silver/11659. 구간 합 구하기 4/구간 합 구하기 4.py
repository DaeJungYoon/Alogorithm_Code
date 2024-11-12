import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

#누적합 리스트 만들기
acc = [0]
for num in nums:
  acc.append(acc[-1]+num) # acc[-1]: acc의 맨 오른쪽

for _ in range(M): #M번에 거처서 
  i, j = map(int, input().split()) #i부터 j까지 입력 받음
  print(acc[j] - acc[i-1])
  
  
