import time, socket, MySQLdb, json
from requests import *

class Analyze:
    def __init__(self, result_id, params, result):
        self.result_id = result_id
        self.params = params
        self.result = result

HOST = '127.0.0.1' 
PORT = 3306
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
    print('connected')
except:
    print("Cannot connect to the server")

db = MySQLdb.connect("localhost","root","pass","morgdb")
print('connected')
cursor = db.cursor()

while True:
    all_reqs = select_all_requests(db)
    if all_reqs:
        for info in all_reqs:
            mylist = {"email": info.email, "name": info.name, "description": info.description}
            done = "Done"
            q_str = "INSERT INTO results ({0}, {1}, {2}) values (%s, %s, %s)".format(FIELD_ID, FIELD_PARAMS, FIELD_RESULT)
            cursor.execute(q_str, [info.request_id, json.dumps(mylist), done])
            del_row = "delete from requests where id = %s"
            cursor.execute(del_row, [info.request_id])
            db.commit()
    else:
        str = "SELECT NOW()"
        print(cursor.execute(str))
        print('no requests')
    time.sleep(3)

########
# Defs #
########
TABLE_NAME = 'results'
FIELD_ID = "result_id"
FIELD_PARAMS = "params"
FIELD_RESULT = "result"
#take all requests, store id into id of results table, requests info as json (json.stringify) into paramams, "Done" into result