from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="075"
#問題
problem="d"

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
  N,K=map(int,input().split())
  p=[list(map(int,input().split())) for _ in range(N)]
  p.sort()
  ans=10**100
  for i in range(N):
    x0=p[i][0]
    for j in range(N):
      y0=p[j][1]
      for k in range(N):
        y1=p[k][1]
        cnt=0
        idx=0
        while idx<N and cnt<K:
          x,y=p[idx]
          if x0<=x and y0<=y<=y1: cnt+=1
          idx+=1
        if cnt==K: ans=min(ans, (x-x0)*(y1-y0))
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])