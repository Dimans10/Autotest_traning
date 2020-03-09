from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="His name", header="His header", footer="His footer"))
    app.session.logout()