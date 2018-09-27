#-*- coding:utf-8 -*-
from flask import Flask,render_template,request
import pymysql

db = pymysql.connect('localhost','root','123456','test')
cursor = db.cursor()

app = Flask(__name__)

@app.route('/login',methods=['GET'])
def login():
    return render_template('common/register.html')

@app.route('/login',methods=['POST'])
def login_post():
    name = request.form['username']
    pwd1 = request.form['password']
    mail = request.form['email']
    sql = """select * from userpwd where username = '%s'
    """%(name)
    if cursor.execute(sql):
        return render_template('common/register.html',message='用户名已存在')
    sql_insert = """insert into userpwd(username,email,passwd) values('%s','%s','%s')
         """%(name,mail,pwd1)
    cursor.execute(sql_insert)
    db.commit()
    return render_template('common/login1.html',message='注册成功，可以登陆了') 
@app.route('/signin',methods=['GET'])
def login1():
    return render_template('common/login1.html')

@app.route('/index',methods=['POST'])
def login1_post():
    name = request.form['username']
    passwd =  request.form['password']
    sql = """select * from userpwd where username='%s'
    """%(name)
    cursor.execute(sql)
    results = cursor.fetchall()
    for res in results:
        if res[-1] == passwd:
            return render_template('index.html',mes='wellcom '+name)   
    return render_template('common/login1.html',message='用户名或密码错误，请重新输入')

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
app.run(debug=True)