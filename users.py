class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

def create_user_account(db, email, password):
    q_str = "INSERT INTO users ({1}, {2}) values (%s, %s)".format(TABLE_NAME, FIELD_EMAIL, FIELD_PASSHASH)
    c = db.cursor()
    c.execute(q_str, [email, password])
    db.commit()
    return get_one_by_email(db, email)

def get_one_by_email(db, email):
    if email is None:
        print("none")
        return None
    q_str = "SELECT {0}, {1} FROM {2} WHERE {3}=%s".format(FIELD_EMAIL, FIELD_PASSHASH, TABLE_NAME, FIELD_EMAIL)
    c = db.cursor()
    c.execute(q_str, [email])
    users = [User(r[0], r[1]) for r in c.fetchall()]
    if len(users) < 1:
        return None
    return users[0]

def is_email_already_taken(db, email):
    user = get_one_by_email(db, email)
    if user is None:
        return False
    return True

########
# Defs #
########
TABLE_NAME = 'users'
FIELD_EMAIL = 'email'
FIELD_PASSHASH = 'password'


