# -*- coding: utf-8 -*-
import pytest
from group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group(name="Her name", header="Her header", footer="Her footer"))
    app.session.logout()

def test_add__empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.session.logout()