import time, socket, MySQLdb, json
from time import gmtime, strftime
from myrequests import *
from postmarker.core import PostmarkClient

########
# Defs #
########
TABLE_NAME = 'results'
FIELD_ID = "result_id"
FIELD_PARAMS = "params"
FIELD_RESULT = "result"

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

while True:
    db = MySQLdb.connect("localhost","root","pass","morgdb")
    cursor = db.cursor()
    all_reqs = select_all_requests(db)
    if all_reqs:
        for info in all_reqs:
            mylist = {"email": info.email, "name": info.name, "description": info.description, "time": info.time, "complete_time": strftime("%Y-%m-%d %H:%M:%S", gmtime())}
            print(mylist["time"])
            done = "Done"
            q_str = "INSERT INTO results ({0}, {1}, {2}) values (%s, %s, %s)".format(FIELD_ID, FIELD_PARAMS, FIELD_RESULT)
            cursor.execute(q_str, [info.request_id, json.dumps(mylist), done])
            del_row = "delete from requests where id = %s"
            cursor.execute(del_row, [info.request_id])
            db.commit()
            postmark = PostmarkClient(server_token='a27b1880-5284-4389-b274-b74d22b2b22c')
            postmark.emails.send(
            From='dng4@wisc.edu',
            To='dng4@wisc.edu',
            Subject='Message',
            HtmlBody='<b>your request has been processed</b>')
    else:
        print('no requests')
    time.sleep(3)


#take all requests, store id into id of results table, requests info as json (json.stringify) into paramams, "Done" into result