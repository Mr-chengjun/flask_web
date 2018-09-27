#-*- coding:utf-8 -*-

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/login',methods=['GET'])
def login():
    return render_template('common/test.html')

@app.route('/login',methods=['POST'])
def login_post():
    if request.form['email'] == 'cheng' and request.form['pass'] == '123':
        return '欢迎你'
    return '账号或者密码错误了哦'
app.run(debug=True)