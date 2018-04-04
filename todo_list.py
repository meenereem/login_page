class Task:
    def __init__(self, task_id, email, task):
        self.email = email
        self.task = task
        self.task_id = task_id

def add_todo_task(db, email, task):
    q_str = "INSERT INTO todo_list ({1}, {2}) values (%s, %s)".format(TABLE_NAME, FIELD_EMAIL, FIELD_TASK)
    print(q_str)
    c = db.cursor()
    c.execute(q_str, [email, task])
    db.commit()

def select_all_tasks(db, email):
    c = db.cursor()
    string = 'SELECT {0}, {1}, {2} FROM todo_list WHERE {3}=%s'.format(TASK_ID, FIELD_EMAIL, FIELD_TASK,FIELD_EMAIL)
    c.execute(string, [email])
    tasks = [Task(r[0], r[1], r[2]) for r in c.fetchall()]
    return tasks

def delete_selected_task(db, task_id, email):
    c = db.cursor()
    d = db.cursor()
    string = 'SELECT {0}, {1}, {2} FROM todo_list WHERE {3}=%s'.format(TASK_ID, FIELD_EMAIL, FIELD_TASK, TASK_ID)
    c.execute(string, [task_id])
    useremail = [Task(r[0], r[1], r[2]) for r in c.fetchall()]
    if str(useremail[0].task_id) == str(task_id) and useremail[0].email == email:
        d.execute('delete from todo_list where task_id = %s', [task_id])
        db.commit()

TABLE_NAME = 'todo_list'
FIELD_EMAIL = 'email'
FIELD_TASK = 'task'
TASK_ID = "task_id"
    