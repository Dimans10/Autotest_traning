from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first(Group(name="His name", header="His header", footer="His footer"))

def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="New name"))
