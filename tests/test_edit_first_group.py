from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    app.group.edit_first(Group(name="His name", header="His header", footer="His footer"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    app.group.edit_first(Group(name="New name"))
