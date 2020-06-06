from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
client = MongoClient('localhost', port=27017)
db = client.dbsparta
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/memo', methods=['POST'])
def write_memo():
    url=request.form['url']
    comment=request.form['comment']
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')
    db.memos.insert_one({
        'img': og_image['content'],
        'title': og_title['content'],
        'description': og_description['content'],
        'comment': comment,
        'url': url
    })
    return jsonify({
        "result": "success",
        "msg": "ok"
    })
@app.route('/memo', methods=['GET'])
def read_memos():
    memos = list(db.memos.find({},{'_id':0}))
    return jsonify({
        "result": "success",
        "data": memos
    })
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)