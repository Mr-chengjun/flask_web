#-*- coding:utf-8 -*-
from flask import Flask,render_template,request
import pymysql

db = pymysql.connect('localhost','root','123456','test')
cursor = db.cursor()

# sql_s = """select job_name,job_desc,comp_name,work_addr,education,work_years,min_salary,max_salary,comp_url,job_detail_url from lagou1 ORDER BY RAND() limit 15"""
# cursor.execute(sql_s)
# resus = cursor.fetchall() 
sql_s = """select job_name,job_desc,comp_name,work_addr,education,work_years,min_salary,max_salary,comp_url,job_detail_url from lagou1 ORDER BY RAND() limit 15"""

app = Flask(__name__)

#注册
@app.route('/login',methods=['GET'])
def login():
    return render_template('common/register.html')

#注册的提交
@app.route('/login',methods=['POST'])
def login_post():
    name = request.form['username']
    pwd1 = request.form['password']
    pwd2 = request.form['confirm_password']
    mail = request.form['email']
    sql = """select * from userpwd where username = '%s'
    """%(name)
    if cursor.execute(sql):
        return render_template('common/register.html',message='用户名已存在')
    elif pwd1 != pwd2:
        return render_template('common/register.html',message='前后密码不一致，请输入')
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
           #实现随机分配数据
            cursor.execute(sql_s)
            resus = cursor.fetchall() 
            return render_template('boke/index.html',title=name,res= resus)   
    return render_template('common/login1.html',message='用户名或密码错误，请重新输入')

@app.route('/index')
def index():
    #实现随机分配数据
    cursor.execute(sql_s)
    resus = cursor.fetchall() 
    return render_template('boke/index.html',res= resus)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
app.run(debug=True)



