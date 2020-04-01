# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app, db, json_group):
    test_group = json_group
    old_groups = db.get_list_group_from_db()
    app.group.create(test_group)
    new_groups = db.get_list_group_from_db()
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

