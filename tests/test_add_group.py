# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="Her name", header="Her header", footer="Her footer"))
    app.group.back_to_home()
    app.session.logout()

def test_add__empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
    app.group.back_to_home()