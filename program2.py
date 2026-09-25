from collections import deque
number=int(input())
arr=list(map(int,input().split()))
k=int(input())
max_deq=deque()
min_deq=deque()
left=0
max_length=0
start_pos=1
for right in range(number):
  while max_deq and arr[max_deq[-1]]<arr[right]:
    max_deq.pop()
  max_deq.append(right)
  while min_deq and arr[min_deq[-1]]>arr[right]:
    min_deq.pop()
  min_deq.append(right)
  while  max_deq and min_deq and arr[max_deq[0]]-arr[min_deq[0]]>k:
    if max_deq[0]==left:
      max_deq.popleft()
    if min_deq[0]==left:
      min_deq.popleft()
    left=left+1
  length=right-left+1
  if length>max_length:
    max_length=length
    start_pos=left+1
print(max_length,start_pos)
