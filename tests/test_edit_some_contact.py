from model.contact import Contact
from random import randrange
import time

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name =u"Иван", middle_name =u"Иванович", last_name =u"Иванов",
                                   nickname = "Ivan!", company = "Booking Mashin", title = "Ivyshka",
                                   address = "Pyshkina st home Kolotyshkina 5", home = "123456789", mobile = "+987654321",
                                  work = "14946", fax = "228", email1 = "123@mail.ru", email2 = "321@mail.ru",
                                  email3 = "333@mail.ru", home_page = "ok.ru", bday = "16", bmonth = "July", byear = "1995"))
    test_contact = Contact(first_name=u"Петр", last_name=u"Петров")
    old_contacts = app.contact.get_list_contact()
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    test_contact.id = id
    old_contacts[index] = test_contact
    app.contact.edit_by_id(test_contact, id)
    new_contacts = app.contact.get_list_contact()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_test(app):
    app.contact.open_contact_details_by_index(2)
    time.sleep(3)