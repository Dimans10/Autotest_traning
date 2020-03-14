from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="N", header="H", footer="F"))
    app.group.delete_first()