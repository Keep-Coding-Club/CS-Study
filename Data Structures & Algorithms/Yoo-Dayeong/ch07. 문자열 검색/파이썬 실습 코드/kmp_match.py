def kmp_match(txt, pat):
  pt = 0 # txt 커서
  pp = 0 # 패턴 커서
  skip = [0]*(len(pat)+1) # 건너뛰기 표
  
  # 건너뛰기 표 만들기
  skip[pt]=0
  while pt!=len(pat):
    if pat[pt] == pat[pp]:
      pt +=1
      pp +=1
      skip[pt]=pp
    elif pp == 0:
      pt += 1
      skip[pt]=pp
    else:
      pp=skip[pp]
      
  # 문자열 검색    
  pt = pp = 0
  while pt!=len(txt) and pp!=len(pat):
    if txt[pt]==pat[pp]:
      pt +=1
      pp += 1
    elif pp == 0:
      pt +=1
    else:
      pp=skip[pp]
  
  return pt-pp if pp==len(pat) else -1

s1= input()
s2=input()

idx = kmp_match(s1, s2)

if idx==1:
  print('-1')
else:
  print(f'{(idx+1)}번째 문자 일치')