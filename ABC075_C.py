from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="075"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import deque
  import copy
  def bfs(g,s):
    inf=10**30
    D=[inf]*len(g)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in g[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  E=[]
  ans=0
  for i in range(M):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].add(b)
    G[b].add(a)
    E.append((a,b))
  for i in range(M):
    a,b=E[i]
    G2=copy.deepcopy(G)
    G2[a].remove(b)
    G2[b].remove(a)
    D=bfs(G2,0)
    if sum([1 for j in range(N) if D[j]<100])<N: ans+=1
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])