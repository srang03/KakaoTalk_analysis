from wordcloud import WordCloud
import datetime as dt

def kakao_read(file_name):
    text = ''
    with open("./text/" + file_name + '.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            text += line

    font = 'C:/Windows/Fonts/NanumBarunGothicBold.ttf'

    print(text[:1000])

    wc = WordCloud(font_path=font, background_color="white", width=600, height=400)
    wc.generate(text)
    img_file_name = 'result{}.png'.format(str(dt.datetime.now()).replace(' ','').replace(':','_').replace('.','_'))
    wc.to_file('./static/' + img_file_name)

    return img_file_name

