from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for, g
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from users import *
from sessions import *
from todo_list import *
from myrequests import *
from results import *
from postmarker.core import PostmarkClient
import os, json, bcrypt, sqlite3


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass'
app.config['MYSQL_DATABASE_DB'] = 'morgdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
# ssh dng@mir-38
@app.before_request
def before_request():
    g.db = mysql.connect()
    # g.db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db", check_same_thread=False)

@app.teardown_request
def teardown_request(exception):
    if g.db is not None:
        g.db.close()

@app.route('/')
def home():
    if get_logged_in_user() is None:
        return redirect('/login')
    else:
        return render_template('index.html')
 
@app.route('/signup', methods=['GET', 'POST'])
def do_admin_signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if is_email_already_taken(g.db, request.form['username']) == False:
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
        create_user_account(g.db, request.form['username'], hashed)
        return redirect('/login')
    else:
        return render_template('signup.html', message = "username or password already exists")


@app.route('/email', methods=['POST'])
def send_result_email():
        postmark = PostmarkClient(server_token='a27b1880-5284-4389-b274-b74d22b2b22c')
        postmark.emails.send(
        From='dng4@wisc.edu',
        To=request.form['email'],
        Subject='Message',
        HtmlBody=request.form['message'])
        return render_template('index.html')

def corr_user():
    token = session.get('token')
    email = session.get('email')
    user = get_one_by_email_session(g.db, email)
    if user is None:
        return False
    if user.token == token:
        return True
    return False

@app.route('/secondpage', methods=['POST', 'GET'])
def route():
    if corr_user() == False:
        return redirect('/login')
    else:
        return render_template('secondpage.html')

@app.route('/todopage', methods=['POST', 'GET'])
def todo():
    if corr_user() == False:
        return redirect('/login')
    else:
        user = get_logged_in_user()
        tasks = select_all_tasks(g.db, user.email)
        return render_template('todo.html', tasks=tasks)

@app.route('/todo_add', methods=['POST'])
def add_task():
    user = get_logged_in_user()
    if request.form['task'] != None:
        add_todo_task(g.db, user.email, request.form['task'])
    return jsonify({"success": True})

@app.route('/todo_delete', methods=['POST'])
def del_task():
    var = request.json
    user = get_logged_in_user()
    delete_selected_task(g.db, request.form['task_id'], user.email )
    return jsonify({"success": True})

@app.route('/requestpage', methods=['POST', 'GET'])
def req():
    if corr_user() == False:
        return redirect('/login')
    else:   
        return render_template('requests.html')

@app.route('/request_add', methods=['POST'])
def add_request():
    if request.form['email'] != None and request.form['name'] != None and request.form['description'] != None:
        print(request)
        submit_request(g.db, request.form['email'], request.form['name'], request.form['description'])
    return jsonify({"success": True})

@app.route('/Results', methods=['POST', 'GET'])
def get_results():
    if corr_user() == False:
        return redirect('/login')
    else:
        result_information = select_all_results(g.db)
        request_information = select_all_requests(g.db)
        return render_template('results.html', request_information=request_information, result_information=result_information)

@app.route('/Index', methods=['POST', 'GET'])
def ret():
    if corr_user() == False:
        return redirect('/login')
    else:
        return render_template('index.html')

def get_logged_in_user():
    token = session.get('token')
    email = session.get('email')
    if email != None and token != None:
        user = get_one_by_email_session(g.db, email)
        if user.token != token:
            return None
        else:
            return user
    return None


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    user = get_logged_in_user()
    print(user)
    if user is not None: 
        delete_row(g.db, user.email)
    session['email'] = None
    session['token'] = None
    return home()

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    password = request.form['password']
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
    if is_email_already_taken(g.db, request.form['username']) == True:
        obj = get_one_by_email(g.db, request.form['username'])
        if bcrypt.checkpw(password.encode('utf-8'), obj.password.encode('utf-8')) == True:
            create_session_token(g.db, request.form['username'])
            return render_template('index.html', email = obj.email)
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)