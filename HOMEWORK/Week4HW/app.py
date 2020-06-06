from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/register', methods=['POST'])
def register_confirm():
    KoreanName_receive = request.form['KoreanName_give']
    Level_receive = request.form['Level_give']
    Address_receive = request.form['Address_give']
    PhoneNumber_receive = request.form['PhoneNumber_give']

    doc = {
        'KoreanName':KoreanName_receive,
        'Level': Level_receive,
        'Address': Address_receive,
        'PhoneNumber':PhoneNumber_receive
    }
    db.registration.insert_one(doc)

    return jsonify({'result':'success', 'msg': '!!!Successfully Registered!!!'})


@app.route('/register', methods=['GET'])
def read_registrations():
  registeredInformation = list(db.registration.find({},{'_id':0})) 
                                                            # _id 값을 가져오면 돌아가지 않습니다.
  return jsonify({'result':'success', 'all_registrations': registeredInformation})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) 