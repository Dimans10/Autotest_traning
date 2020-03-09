from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Her name", header="Her header", footer="Her footer"))
    app.session.logout()