import pymysql.cursors
from model.group import Group

connection = pymysql.connect(host="127.0.0.1", database= "addressbook", user= "root", password= "")

class Dbfixture:
    def __init__(self, host, db, user, password):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=db, user=user, password=password)

    def get_list_group_from_db(self):
        groups = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def destroy(self):
        self.connection.close()
