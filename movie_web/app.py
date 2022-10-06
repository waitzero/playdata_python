import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from movie import Movie, MvService

# flask 객체 생성. 웹 앱 객체 생성
app = Flask(__name__)
service = MvService()

@app.route('/')
def root():
    data = service.get_all()
    return render_template('index.html', cols =cols, data=data)

@app.route('/search', methods=['POST', 'GET'])
def search():

    if request.method == 'POST':
        name = request.form['name']#폼파라메터 속성
    else:
        name = request.args['name']  # 폼파라메터 속성
    mv:Movie = service.get_by_name(name)
    return render_template('search.html', mv=mv)
@app.route('/ticket-rate')
def rate():
    img_path='static/piegraph.png'
    val = service.get_ticket_rate()
    labels = val[:, 0]
    rate = val[:, 1]*100
    fig, ax = plt.subplot()
    ex = (0, 0, 0, 0, 0)  # 각 부채꼴 떨어뜨릴 거리. 0인 요소는 붙어서 출력됨
    plt.pie(rate, labels=labels, autopct='%.1f%%', counterclock=False,
            startangle=90, explode=ex)
    fig.savefig(img_path)
    img_path = '/'+img_path
    return render_template('rate.html', val=val, img_path=img_path)

if __name__=='__main__':
    app.run() # 플라스크 앱 실행