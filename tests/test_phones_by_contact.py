# -*- coding: utf-8 -*-
from model.contact import Contact
import re
from random import randrange

def test_add_contact(app):
    test_contact = Contact(first_name =u"Иван", last_name =u"Иванов")
    contacts = app.contact.get_list_contact()
    index = randrange(len(contacts))
    contact_phones_from_home_page = contacts[index]
    contact_phones_from_edit_page = app.contact.get_phones_from_edit_page(index)
    assert contact_phones_from_home_page.home == clear(contact_phones_from_edit_page.home)
    assert contact_phones_from_home_page.mobile == clear(contact_phones_from_edit_page.mobile)
    assert contact_phones_from_home_page.work == clear(contact_phones_from_edit_page.work)
    assert contact_phones_from_home_page.phone2 == clear(contact_phones_from_edit_page.phone2)

def clear(s):
    return re.sub("[() -]", "", s)