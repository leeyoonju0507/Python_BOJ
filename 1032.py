a = int(input())
#첫번째 문장 입력받고 배열로 만들기 = 기준문장
b = input()
lst = []
for i in b:
    lst.append(i)

#두번째 문장이후부터 입력받고 기준문장과 비교
for i in range(a-1):
    c = input()
    n = 0
    for j in c:
        if j != lst[n]:
            lst[n] = '?'
        n+=1
for i in lst:
    print(i,end='')