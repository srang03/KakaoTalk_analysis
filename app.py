from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import datetime as dt
import kakao_read as kr

#Flask 객체 인스턴스 생성
app = Flask(__name__)

# url 패턴 - 라우터 설정 - Decorater

@app.route('/')
def index():
    filename = request.form.get('file')
    if filename is not None :
        return filename
    else :
        return render_template('index.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        text_file_name = str(dt.datetime.now()).replace(' ','').replace(':','_').replace('.','_')
        f.save('./text/'+text_file_name+'.txt')

        img_name = kr.kakao_read(text_file_name)
        return  render_template('index.html', data=img_name)



# 메인 테스트
if __name__ == "__main__":
    app.run(debug=True)
