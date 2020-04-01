from model.group import Group
import random

def test_delete_some_group(app, db):
    if len(db.get_list_group_from_db()) == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    old_groups = db.get_list_group_from_db()
    group = random.choice(old_groups)
    app.group.delete_some_by_id(group.id)
    new_groups = db.get_list_group_from_db()
    assert (len(old_groups) - 1 == len(new_groups))
    old_groups.remove(group)
    assert old_groups == new_groups