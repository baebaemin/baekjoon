_, X = map(int, input().split())
lst_A = list(map(int, input().split()))
print(' '.join(str(n) for n in lst_A if n < X))
# 반복과 조건문을 통해 리스트를 만들고 그걸 다시 join을 통해 문자열을 조립, 반환하는 방법보다
# 출력용이므로 join에 반복과 조건문을 넣기