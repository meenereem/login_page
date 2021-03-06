import uuid
from flask import Flask, session

class Session:
    def __init__(self, email, token):
        self.email = email
        self.token = token

def create_session_token(db, email):
    token = uuid.uuid4().hex
    session['token'] = token
    session['email'] = email
    q_str = "INSERT INTO user_sessions ({1}, {2}) values (%s, %s)".format(TABLE_NAME, FIELD_EMAIL, FIELD_TOKEN)
    c = db.cursor()
    c.execute(q_str, [email, token])
    db.commit()

def get_one_by_email_session(db, email):
    if email is None:
        return None
    q_str = "SELECT {0}, {1} from {2} WHERE {3}=%s".format(FIELD_EMAIL, FIELD_TOKEN, TABLE_NAME, FIELD_EMAIL)
    c = db.cursor()
    c.execute(q_str, [email])
    user_sessions = [Session(r[0], r[1]) for r in c.fetchall()]
    if len(user_sessions) < 1:
        return None
    return user_sessions[0]

def delete_row(db, email):
    c = db.cursor()
    c.execute('delete from user_sessions WHERE email=%s', [email])
    db.commit()
########
# Defs #
########
TABLE_NAME = 'user_sessions'
FIELD_EMAIL = 'email'
FIELD_TOKEN = 'token'