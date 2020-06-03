from flask import Flask, render_template, request


app=Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/mypage')
def page():
    return 'This is My PAGE'


if __name__ ==  '__main__':
    app.run('0.0.0.0',port=5000,debug=True)