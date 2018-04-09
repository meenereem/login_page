class Request:
    def __init__(self, request_id, email, name, description, time):
        self.request_id = request_id
        self.email = email
        self.name = name
        self.description = description
        self.time = time

def submit_request(db, email, name, description):
    q_str = "INSERT INTO requests ({1}, {2}, {3}, {4}) values (%s, %s, %s, %s)".format(TABLE_NAME, FIELD_EMAIL, FIELD_NAME, FIELD_DESCRIPTION, FIELD_TIME)
    c = db.cursor()
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    c.execute(q_str, [email, name, description, t])
    db.commit()

def select_all_requests(db):
    c = db.cursor()
    string = 'SELECT * FROM requests'
    c.execute(string)
    reqs = [Request(r[0], r[1], r[2], r[3], r[4]) for r in c.fetchall()]
    return reqs

TABLE_NAME = 'requests'
FIELD_EMAIL = 'email'
FIELD_NAME = 'name'
FIELD_DESCRIPTION = 'description'
FIELD_TIME = 'time'
