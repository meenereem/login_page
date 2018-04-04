class Request:
    def __init__(self, request_id, email, name, description):
        self.request_id = request_id
        self.email = email
        self.name = name
        self.description = description

def submit_request(db, email, name, description):
    q_str = "INSERT INTO requests ({1}, {2}, {3}) values (%s, %s, %s)".format(TABLE_NAME, FIELD_EMAIL, FIELD_NAME, FIELD_DESCRIPTION)
    c = db.cursor()
    c.execute(q_str, [email, name, description])
    db.commit()

def select_all_requests(db):
    c = db.cursor()
    string = 'SELECT * FROM requests'
    c.execute(string)
    reqs = [Request(r[0], r[1], r[2], r[3]) for r in c.fetchall()]
    return reqs

TABLE_NAME = 'requests'
FIELD_EMAIL = 'email'
FIELD_NAME = 'name'
FIELD_DESCRIPTION = 'description'
