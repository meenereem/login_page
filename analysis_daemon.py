import time, socket, MySQLdb
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
    if all_reqs != None:
        for info in all_reqs:
            mylist = [info.email, info.name, info.description]
            done = "Done"
            q_str = "INSERT INTO results ({0}, {1}, {2}) values (%s, %s, %s)".format(FIELD_ID, FIELD_PARAMS, FIELD_RESULT)
            cursor.execute(q_str, [info.request_id, mylist, done])
            del_row = "delete from results where id = %s"
            cursor.execute(del_row, [info.request_id])
            cursor.commit()
            # print(info.request_id)
            # print(info.email)
            # print(info.name)
            # print(info.description)
    else:
        print('no requests')
    time.sleep(30)

########
# Defs #
########
TABLE_NAME = 'results'
FIELD_ID = "result_id"
FIELD_PARAMS = "params"
FIELD_RESULT = "result"
#take all requests, store id into id of results table, requests info as json (json.stringify) into paramams, "Done" into result