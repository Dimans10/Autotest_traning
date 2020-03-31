import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database= "addressbook", user= "root", password= "")

class Dbfixture:
    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=db, user=user, password=password)

    def destroy(self):
        self.connection.close()
