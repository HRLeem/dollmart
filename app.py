from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/memo', methods=['GET'])
def listing():
    movies = list(db.movie.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'movies':movies})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    movies = {
        'url' : url_receive
        , 'comment' : comment_receive
    }
    print(url_receive, comment_receive)
    db.movie.insert_one(movies)
    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('127.0.0.1',
           port=6009
           ,debug=True)