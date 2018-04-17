from time import gmtime, strftime
class Request:
    def __init__(self, request_id, KeyPhrase, TargetTerms, sepKP, time, in_progress):
        self.request_id = request_id
        self.KeyPhrase = KeyPhrase
        self.TargetTerms = TargetTerms
        self.sepKP = sepKP
        self.time = time
        self.in_progress = in_progress

def submit_request(db, KeyPhrase, TargetTerms, sepKP):
    print(KeyPhrase)
    q_str = "INSERT INTO requests ({1}, {2}, {3}, {4}, {5}) values (%s, %s, %s, %s, %s)".format(TABLE_NAME, FIELD_KP, FIELD_TargetTerms, FIELD_SEPKP, FIELD_TIME, IN_PROGRESS)
    c = db.cursor()
    t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    c.execute(q_str, [KeyPhrase, TargetTerms, sepKP, t, "False"])
    db.commit()

def select_all_requests(db):
    c = db.cursor()
    string = 'SELECT * FROM requests'
    c.execute(string)
    reqs = [Request(r[0], r[1], r[2], r[3], r[4], r[5]) for r in c.fetchall()]
    return reqs

TABLE_NAME = 'requests'
FIELD_KP = 'KeyPhrase'
FIELD_TargetTerms = 'TargetTerms'
FIELD_SEPKP = 'sepKP'
FIELD_TIME = 'time'
IN_PROGRESS = 'in_progress'
