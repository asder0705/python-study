#9_라이브러리.PY
#pickle라이브러리로 객체 저장
#%%
import pickle
#객체의 형태를 그래도 유지하면서 파일로 저장 및 불러오기 가능
members = {'id1' :['강호동', 52], 'id2':['유재석', 48]}

f= open('members.pickle', 'wb') #파일 쓰기모드로 열기
pickle.dump(members, f)
f.close()#파일 닫기

# %%
import pickle
f = open('members.pickle', 'rb')
data = pickle.load(f)
print(data)
# %%
#time 라이브러리
import time
print(time.time())
#1970년 1월 1일 0시 0분 0초부터 현재까지 지난시간

print(time.localtime(time.time()))
print(time.localtime(time.time()).tm_wday)
#0: 월요일 ~6:일요일

#날짜/시간 출력형식 지정
# print(time.strftime('출력포멧', time.localtime(time.time())))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %p %H:%M:%S', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %p %I:%M:%S', time.localtime(time.time())))

#sleep 함수 대기
for i in range(10):
    print(i)
    time.sleep(1) #1초대기
# %%
#날짜 관련 라이브러리
from datetime import datetime, timedelta
time1 = datetime(2001,7,5,18,0,0)
#                 년  월일시 분 초
time2 = datetime.now()#현재 날짜 및 시간
print(time1,time2)

#날짜 계산이 가능
print(time2-time1) #날짜 차이

#특정 날짜로부터 시간 계산
print(time2+timedelta(days=30)) #오늘로부터 30일뒤 몇일인지
print(time2+timedelta(days=3, hours=-4)) #오늘로부터 3일 및 4시간 전 날짜 

#숙제 1)
#여러분들의 탄생일로부터 오늘까지 몇일이 지났는지 출력
# %%
#random 라이브러리
#난수를 발생시키는 모듈
#1) 0.0~1.0 사이의 실수타입 난수 생성
import random 
print(random.random())

#2) 시작값 ~ 마지막값 전까지의 정수형 난수 생성
print(random.randint(1,10)) #1~10까지

#3)리스트를 무작위로 섞는 함수
numlist  = [1,2,3,4,5]
random.shuffle(numlist) #입력 리스트를 변화시킴
print(numlist)

#4) 리스트의 항목중 무작위로 하나의 값을 얻을 때
print(random.choice(numlist))


# %%
import random
randomnum = random.randint(1,100)
game_on = True
count = 0
while game_on :
    #사용자가 맞출때까지
    try :
        user_num = int(input("1~100사이의 숫자를 입력하세요 >"))
        if user_num < 0 or user_num > 100 : 
            print('숫자 범위를 벗어났습니다. 다시 입력하세요.')
            continue
    except :
        print('잘못입력했습니다. 다시 입력하세요.')
        continue
    count += 1
    if randomnum == user_num :
        game_on = False
    elif randomnum > user_num :
        print('up~~~~~~~!!!')
    else :
        print('down!!!!!!!!')
print(f'{count}횟수로 숫자를 맞췄습니다.')

# %%
#가위, 바위, 보 게임 만들기
#컴퓨터로부터 랜덤하게 '가위' '바위' '보' 를 얻은 후,
#사용자 입력을 받아 승부 결과를 출력한다.
#이긴경우, 진경우 , 비긴경우 출력
import random
game_on= True
rcp_list = ['가위', '바위', '보']
while game_on :
    comsel = random.choice(['가위','바위', '보'])
    usersel = input("가위,바위,보 중 입력하세요 >")
    if not usersel in rcp_list :#not은 조건의 반전 true -> false, false-> true
        print('잘못입력하셨습니다. 다시 입력하세요')
        continue

    print(f'com:{comsel},user:{usersel}')
    #비긴경우
    if usersel ==comsel :
        print("비김")
        continue
    #이긴경우
    elif (usersel =='가위' and comsel == '보')  or \
        (usersel == '바위' and comsel =='가위')  or \
        (usersel == '보' and comsel == '바위') :
        print("이김.")
    #진경우
    else :
        print("짐")
        game_on = False
        

# %%
from statics import getmode, getavg
numlist = [1,1,1,2,2,3]
# numlist = ['사과', '사과', '포도']
print(getmode(numlist))
print(getavg(numlist))

# %%
