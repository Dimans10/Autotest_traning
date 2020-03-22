# -*- coding: utf-8 -*-
from model.contact import Contact
import re
from random import randrange

# def test_phones_on_home_page(app):
#     contacts = app.contact.get_list_contact()
#     index = randrange(len(contacts))
#     contact_phones_from_home_page = contacts[index]
#     contact_phones_from_edit_page = app.contact.get_phones_from_edit_page(index)
#     #print(contact_phones_from_home_page.all_phones_in_contact)
#     #print(merge_all_phones_by_edit_page(contact_phones_from_edit_page))
#     assert contact_phones_from_home_page.all_phones_in_contact == merge_all_phones_by_edit_page(contact_phones_from_edit_page)

def test_all_info_by_contact_in_home_page(app):
        contacts = app.contact.get_list_contact()
        index = randrange(len(contacts))
        contact_phones_from_home_page = contacts[index]
        contact_info_from_edit_page = app.contact.get_info_from_edit_page(index)
        assert contact_phones_from_home_page.first_name == contact_info_from_edit_page.first_name
        assert contact_phones_from_home_page.last_name == contact_info_from_edit_page.last_name
        assert contact_phones_from_home_page.address == contact_info_from_edit_page.address
        assert contact_phones_from_home_page.all_phones_in_contact == merge_all_phones_by_edit_page(contact_info_from_edit_page)
        assert contact_phones_from_home_page.all_emails_in_contact == merge_all_emails_by_edit_page(contact_info_from_edit_page)

def test_phones_on_details_page(app):
    contacts = app.contact.get_list_contact()
    index = randrange(len(contacts))
    contact_phones_from_edit_page = app.contact.get_info_from_edit_page(index)
    contact_phones_from_details_page = app.contact.get_phones_from_details_page(index)
    assert contact_phones_from_edit_page.home == contact_phones_from_details_page.home
    assert contact_phones_from_edit_page.mobile == contact_phones_from_details_page.mobile
    assert contact_phones_from_edit_page.work == contact_phones_from_details_page.work
    assert contact_phones_from_edit_page.phone2 == contact_phones_from_details_page.phone2

def merge_all_phones_by_edit_page(contact):
    return '\n'.join(map(lambda x: clear(x),
                          filter(lambda x: x is not None,
                                                     (filter(lambda x: x != '', [contact.home, contact.mobile, contact.work, contact.phone2])))))

def merge_all_emails_by_edit_page(contact):
    return '\n'.join(filter(lambda x: x != '' and x is not None, [contact.email1, contact.email2, contact.email3]))

def clear(s):
    return re.sub("[() -]", "", s)
