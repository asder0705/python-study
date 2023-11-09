#10_파일입출력

#%%
#(1) 텍스트 파일 읽기
file_path = './data/회원정보.txt'
f= open(file_path, 'r', encoding='utf-8')
text = f.read() #파일의 모든 내용읽어 문자열로 반환
print(text)
f.close() #파일닫기


#with 키워드를 통해 파일 열기
#파일 닫기를 안해도 된다.
with open(file_path, 'r', encoding='utf-8') as f :
    text = f.read()
print(text)   
#with를 벗어나면 자동으로 파일 닫기가 됨

#한줄씩 읽어서 리스트로 반환
#readilnes()
with open(file_path, 'r', encoding='utf-8') as f :
    text = f.readlines()
print(text)   

#한사람의 정보 딕셔너리 저장
#key : 
memberlist = []
with open(file_path, 'r', encoding='utf-8') as f :
    liens = f.readlines()
    keylist = liens[0].strip('\n').split(',')
    #'ID,PW,Name,Phone,Address\n'
    
    for line in liens[1:] :
        vallist = line.strip('\n').split(',')
        memberdic = dict()
        for key, val in zip (keylist, vallist) :
            memberdic[key] = val
        print(memberdic)
        memberlist.append(memberdic)
print(memberlist)
#텍스트를 자료구조화

#수원시에 거주하는 사람 정보를 출력
#반복문을 통해 각 자료를 조회
search_regiom = '수원시'
for mem in memberlist :
    if search_regiom in mem['Address'] :
        print(mem)
        
#이름이 강동원인 사람의 정보를 조회
search_name = '강동원'
for mem in memberlist :
    if search_name == mem['Name'] :
        print(mem)

#ID가 id02인 사람의 주소를 부산광역시 해운대구
search_id = 'id02'
for i, mem in enumerate(memberlist) :
    if search_id == mem['ID'] :
        memberlist[i]['Address']= '부산광역시 해운대구'
    
print(memberlist)

# %%
#파일 쓰기
with open('./data/파일쓰기실습1.txt','w', encoding='utf-8') as f :
    for i in range(1,11) :
        f.write(f'{i}번째 줄입니다. \n')
print("파일 쓰기가 완료되었습니다.")

#수정된memberlist 텍스트로 저장
with open('./data/memberAlter.txt', 'w', encoding='utf-8') as f :
    keylist = memberlist[0].keys()
    text = ','.join(keylist) + '\n'
    f.write(text)
    for mem in memberlist :
        vallist = mem.values()
        text = ','.join(vallist)+'\n'
        f.write(text)
print("파일 쓰기가 완료되었습니다.")

#a모드 (append모드) : 파일 끝에 내용을 추가하여 파일쓴다.
#w모드 (write모드)  : 기존 파일 내용을 다 지우고 새롭게 쓰기.
# f = open('./data/memberAlter.txt', 'w', encoding='utf-8') 
# f.close()

#새로운 멤버 추가
new_member = 'id06,0000,유재석,010-0000-0000,서울시 방배동'
with open('./data/memberAlter.txt', 'a', encoding='utf-8') as f :
    f.write(new_member +'\n')
print("파일 쓰기가 완료되었습니다")

# %%
#대전 광역시 행정구역 폴더 만들기
import os 
path = './data'
region = '대전'

folderpath = os.path.join(path, region) #경로생성
print(folderpath)
if not os.path.isdir(folderpath) :
    os.makedirs(folderpath)
    
with open(os.path.join(path, '대전.csv'), 'r', encoding='euc-kr') as f :
    liens = f.readlines()
    gulist = liens[0].strip('\n').split(',')
    print(gulist)
    
    for line in liens[1:] : #동 정보
         donglist = line.strip('\n').split(',')
         for gu, dong in zip(gulist, donglist) :
            dongpath = os.path.join(path, region, gu, dong)
            if not os.path.isdir(dongpath) and dong != '':
                 os.makedirs(dongpath)


            #각 동별로 한글 파일
            file_name = f'{dong}.hwp'
            file_path =os.path.join(dongpath, file_name)
            print(file_path)
            if not os.path.isdir(file_path)  and dong != '':
                f = open(file_path, 'wb')
                f.close()
    