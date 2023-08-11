def bf_match(txt, pat):
  pt = 0 # txt 커서
  pp = 0 # 패턴 커서
  
  while pt!=len(txt) and pp!=len(pat):
    if txt[pt] == pat[pp]:
      pt +=1
      pp +=1
    else:
      pt = pt-pp+1
      pp =0
  
  return pt-pp if pp==len(pat) else -1

s1= input()
s2=input()

idx = bf_match(s1, s2)

if idx==1:
  print('-1')
else:
  print(f'{(idx+1)}번째 문자 일치')