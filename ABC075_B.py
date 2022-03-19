from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="075"
#問題
problem="b"

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
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  ans=[[S[i][j] for j in range(W)] for i in range(H)]
  for i in range(H):
    for j in range(W):
      if S[i][j]=='.':
        tmp=0
        for k in [-1,0,1]:
          for l in [-1,0,1]:
            if 0<=i+k<H and 0<=j+l<W and S[i+k][j+l]=="#": tmp+=1
        ans[i][j]=tmp
  for i in range(H):
    print(*ans[i],sep='')
  """ここから上にコードを記述"""

  print(test_case[__+1])