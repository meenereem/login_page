#Sqlite connections
# cursor = db.cursor()
# cursor.execute('''
#     CREATE TABLE user_sessions(id INTEGER PRIMARY KEY, email TEXT unique, token TEXT unique)
# ''')
# cursor.execute('''
#     CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT unique, password TEXT)
# ''')
# cursor.execute('''
#     CREATE TABLE todo_list(task_id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, task TEXT)
# ''')
# cursor.execute('''
#     DROP TABLE todo_list
# ''')
# db.commit()
# db.close()

#Mysql connections
# CREATE TABLE user_sessions
# (
#     id INT unsigned NOT NULL AUTO_INCREMENT,
#     email VARCHAR(200) NOT NULL,
#     token VARCHAR(200) NOT NULL,
#     PRIMARY KEY (id)   
# );

# CREATE TABLE users
# (
#     id INT unsigned NOT NULL AUTO_INCREMENT,
#     email VARCHAR(200) NOT NULL,
#     password VARCHAR(200) NOT NULL,
#     PRIMARY KEY (id)   
# );

# CREATE TABLE todo_list
# (
#     task_id INT unsigned NOT NULL AUTO_INCREMENT,
#     email VARCHAR(200) NOT NULL,
#     task VARCHAR(200) NOT NULL,
#     PRIMARY KEY (task_id)   
# );

# CREATE TABLE requests
# (
#     id INT unsigned NOT NULL AUTO_INCREMENT,
#     email VARCHAR(200) NOT NULL,
#     name VARCHAR(200) NOT NULL,
#     description VARCHAR(200) NOT NULL,
#     PRIMARY KEY (id)   
# );

# CREATE TABLE results
# (
#     result_id VARCHAR(200) NOT NULL,
#     params VARCHAR(200) NOT NULL,
#     result VARCHAR(200) NOT NULL
# );
