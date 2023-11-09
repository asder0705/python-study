#8_ 자료구조 활용py

#%%
#(1)데이터의 중심 지표를 구하기
#데이터의 중심 지표 - 데이터를 대표하는 하나의 값
#ex) 평균, 최빈값, 중앙값

numlist = [1,2,3,1,2,1,1,3,3,3,100]
#1) 평균
avg = sum(numlist) / len(numlist)
print(avg) #10.9

#2) 최빈값
num_set = set(numlist)
num_dick = dict()
for f in num_set :
    num_dick[f] = numlist.count(f)
print(num_dick)

max_num = max(num_dick.values())
modes = []
for k, v in num_dick.items() :
    if v == max_num :
        print('최빈값', k, v )
        # mode = k
        modes.append(k)
        # break
print(modes)

#3) 중앙값
#리스트를 오름차순으로 정렬한 후,
#리스트의 크기를 n이라고 할 떄, 다음의 인덱스 값이 중앙값
#n이 홀수인 경우 : n//2
#n이 짝수인 경우 : (n//2, n//2-1) 인덱스 값들의 평균
numlist.sort() #기존 리스트를 변경해서 정렬
# sorted(numlist) # 정렬된 리스트를 반환, 기존 리스트 변경 안함

size = len(numlist)

if size % 2== 1 :
    midval = numlist[size//2]
else :
    midval = (numlist[size//2] +  numlist[size//2-2]) /2
print('중앙값', midval)
# %%
#2) set 예제
datelist = ['09/10', '09/11', '09/12', '10/01', '10/13', '11/20']
#위의 헬스장 이용 횟수 데이터에서 달별이용횟수를 출력하시오.

#2-1) 유니크한 달 값 구하기 (달만 있는 list 만들기, set활용)
monlist = []
for d in datelist :
    monlist.append(d[:2])
monlist = [d[:2] for d in datelist ] # 위랑 같은 표현
monlist = [d.split('/')[0] for d in datelist ]

monset = set(monlist)
#2-2) 달별 이용 횟수 구하기 dick에 저장및 count() 함수 활용
moncount = list()
for m in monset :
    moncount.append((m, monlist.count(m)))
print(moncount)
#----------------------------------------------------------------------
#빈도수 구하는 모듈
from collections import Counter
#collection 라이브러리에서 counter 클래스 사용
moncount = Counter(monlist)
print(moncount)
print(moncount.most_common(1)) #가장 빈도수 높은것 1개
print(moncount.most_common(3)) #가장 빈도수 높은것 3개

Counter1 = Counter(['사과', '사과', '딸기'])
Counter2 = Counter(['포도', '포도', '딸기'])
print(Counter1, Counter2)
#집합연산 가능
print(Counter1 + Counter2) #합집합
print(Counter1 - Counter2) #차집합
print(Counter2 - Counter1) #
print(Counter1 & Counter2) #교집합
# %%
