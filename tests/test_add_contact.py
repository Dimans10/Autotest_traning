# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, json_contact):
    test_contact = json_contact
    old_contacts = app.contact.get_list_contact()
    app.contact.create(test_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list_contact()
    old_contacts.append(test_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

