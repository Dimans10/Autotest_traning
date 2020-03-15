# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    test_group = Group(name="Her name", header="Her header", footer="Her footer")
    app.group.create(test_group)
    new_groups = app.group.get_group_list()
    assert(len(old_groups) + 1 == len(new_groups))
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add__empty_group(app):
    old_groups = app.group.get_group_list()
    test_group = Group(name="", header="", footer="")
    app.group.create(test_group)
    new_groups = app.group.get_group_list()
    assert(len(old_groups) + 1 == len(new_groups))
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
