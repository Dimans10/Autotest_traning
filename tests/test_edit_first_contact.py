from model.contact import Contact
import time

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(first_name=u"Петр", middle_name=u"Петрович", last_name=u"Петров",
                                   nickname="Petr!", company="Petrs Mashin", title="Pet9",
                                   address="Pyshkina st home Kolotyshkina 6", home="987654321", mobile="+12345678",
                                   work="14946", fax="228", email1="111@mail.ru", email2="222@mail.ru",
                                   email3="333@mail.ru", home_page="vk.com", bday="16", bmonth="June", byear="1990"))
    app.contact.back_to_home_page()
    app.session.logout()
