# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app, json_tests):
    test_group = json_tests
    old_groups = app.group.get_group_list()
    app.group.create(test_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add__empty_group(app):
#     old_groups = app.group.get_group_list()
#     test_group = Group(name="", header="", footer="")
#     app.group.create(test_group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == app.group.count()
#     old_groups.append(test_group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
