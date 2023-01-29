r = int(input())
for s in range(1, r + 1):
    print(f'%{r}s' % ('*' * s))
# 문자열 빈자리 포맷팅 '%<num>s' % <차지할 str>