from model.group import Group
from fixture.db import Dbfixture

def test_group_app_list_and_db_list(app, db):
    web_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_list_group_from_db())
    assert sorted(web_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)