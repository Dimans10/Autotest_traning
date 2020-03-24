# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest
import string

def ren_random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join(random.choice(symbols) for x in range(random.randrange(maxlen)))

testdata = [Group(name="", header="", footer="")] + [
    Group(name=ren_random_string("name", 10), header=ren_random_string("header", 10), footer=ren_random_string("footer", 5))
    for i in range(5)
    # пример создания данных с перебором списка возможных значений каждого из полей
    # for name in ['', ren_random_string("name", 10)]
    # for header in ['', ren_random_string("header", 10)]
    # for footer in ['', ren_random_string("footer", 5)]
]

@pytest.mark.parametrize("test_group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, test_group):
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
