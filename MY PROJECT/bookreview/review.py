from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('localhost', 27017)  
db = client.dbsparta 


@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']

    db.reviews.insert_one({
        'title': title,
        'author': author,
        'review': review
    })
    return jsonify({'result':'success', 'msg': '리뷰 작성 성공!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)