n=int(input())
intvals=[] 
for i in range(n):
  start,end=map(int,input().split())
  intvals.append([start,end])   
  intvals.sort()   
  res=[]   
  for start,end in intvals:
    if len(res)==0:
      res.append([start,end])
    elif start<=res[-1][1]:
      res[-1][1]=max(res[-1][1],end)
    else:
      res.append([start,end])
for start,end in res:
  print(start,end)
