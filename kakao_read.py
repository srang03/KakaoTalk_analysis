from wordcloud import WordCloud
import datetime as dt
import re

stopwords = ['사진', '이모티콘', '보이스톡 해요', '보이스톡 취소', '보이스톡', '자동환불 완료 기간', '내 받기를 완료하지 않아', '카카오페이머니로', '환불되었습니다',
'받기 완료', '받은 카카오페이머니는', '송금', '및', '온오프라인', '결제는', '물론', '투자도', '가능해요', '받으세요', '을', '를', '이', '가', '장', '받으세요', '받기','완료',
'쓸만큼', '한번에', '충전하고', '아이폰', '에어팟', '응', '에', '동영상', '원', '원을', '파일', '시에', '오늘', '내일', '선물', '메세지', '보냈습니다', '과', '와'
'예약']
def preprocessing(text):
    processing_data = ''
    people = ['']
    if text.startswith('---------------'): # 날짜 요일에 해당하는 부분 처리
        print()
    else:

        tmp = text.split(']') # ] 기준으로 스플릿
        name = tmp[0].replace('[','')  # 이름 가져오기
        if name in people : # people에 name이 있는지 여부 확인
            print()
        else :
            people.append(name) # 없으면 불용어 사전에 추가
        
            if name not in stopwords:
                if len(name) == 3 :
                    stopwords.append(name+'님')
                    stopwords.append(name)
                    stopwords.append(name[1:3])
                    stopwords.append(name[1:3]+'이')
                    stopwords.append(name[1:3]+'아')    
                    stopwords.append(name[2]+'아')
                    stopwords.append(name[2]+'이')        
                else :
                    stopwords.append(name)
                    stopwords.append(name[1:3])



                stopwords.append(name)

        text = tmp[-1]
        print("데이터 전처리 전 : ", text)
        # 개행문자 제거
        text = re.sub('\\\\n', ' ', text)
        # 공백 제거
        text = re.sub('\n', '', text)
        text = re.sub('\r', '', text)
        # 불필요한 탭키 제거
        text = re.sub('\t', '', text)
        # 특수문자,자음 제거
        text = re.sub('[.,;:\)*?!~`’"^\-_+<>@\#$%&=#}※ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㅠㅜ]', '', text)
        # 중복 생성 공백값
        text = re.sub(' +', ' ', text)
        # 알파벳 소문자 대문자 원소들 제거
        text  =re.sub('[a-zA-Z]','', text)
        # 자음 모음 원소들 제거
        text = re.sub('[ㄱ-ㅎㅏ-ㅣ]','', text)
        text = re.sub('[^가-힣 ]','', text)
        print("데이터 전처리 후 : ", text)
        if text == '':
            print('')
   
        else : 
            tmp = text.split(' ')
            for i in tmp:
                if i not in stopwords:
                    processing_data += (i+' ')
        print("-----------------------------------------------")
    return processing_data

def kakao_read(file_name):
    text = ''
    with open("./text/" + file_name + '.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            text += preprocessing(line)
    print(text)
    font = 'C:/Windows/Fonts/NanumBarunGothicBold.ttf'

    print(text[:1000])

    wc = WordCloud(font_path=font, background_color="white", width=600, height=400)
    wc.generate(text)
    img_file_name = 'result{}.png'.format(str(dt.datetime.now()).replace(' ','').replace(':','_').replace('.','_'))
    wc.to_file('./static/' + img_file_name)

    return img_file_name
