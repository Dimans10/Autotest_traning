from model.contact import Contact
from random import randrange
import time

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name =u"Иван", middle_name =u"Иванович", last_name =u"Иванов",
                                   nickname = "Ivan!", company = "Booking Mashin", title = "Ivyshka",
                                   address = "Pyshkina st home Kolotyshkina 5", home = "123456789", mobile = "+987654321",
                                  work = "14946", fax = "228", email1 = "123@mail.ru", email2 = "321@mail.ru",
                                  email3 = "333@mail.ru", home_page = "ok.ru", bday = "16", bmonth = "July", byear = "1995"))
    old_contacts = app.contact.get_list_contact()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact(index)
    old_contacts[index:index + 1] = []
    new_contacts = app.contact.get_list_contact()
    assert old_contacts == new_contacts
