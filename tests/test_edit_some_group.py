from model.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    test_group = Group(name="His name", header="His header", footer="His footer")
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    test_group.id = old_groups[index].id
    old_groups[index] = test_group
    app.group.edit_some(index, test_group)
    new_groups = app.group.get_group_list()
    assert (len(old_groups) == len(new_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="N", header="H", footer="F"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(name="New name"))
#     new_groups = app.group.get_group_list()
#     assert (len(old_groups) == len(new_groups))
