from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="His name", header="His header", footer="His footer"))
    new_groups = app.group.get_group_list()
    assert (len(old_groups) == len(new_groups))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert (len(old_groups) == len(new_groups))
