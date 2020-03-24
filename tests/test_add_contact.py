# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def gen_random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join(random.choice(symbols) for x in range(random.randrange(maxlen)))

def gen_random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(symbols) for x in range(random.randrange(maxlen))) + (random.choice(["@mail.ru", "@yandex.ru", "@gmail.ru", "@rambler.ru"]))

testdata = [
    Contact(first_name =gen_random_string('firstname', 10), middle_name =gen_random_string('middlename', 10), last_name =gen_random_string('lastname', 10),
            nickname =gen_random_string('nickname', 10), company =gen_random_string('company', 10), title =gen_random_string('title', 10),
            address =gen_random_string('address', 10), home =gen_random_string('home', 10), mobile =gen_random_string('mobile', 10),
            work =gen_random_string('work', 10), fax =gen_random_string('fax', 10), email1 =gen_random_email(10),
            email2 =gen_random_email(10), email3 =gen_random_email(10), home_page =gen_random_string('home_page', 10),
            phone2 =gen_random_string('phone2', 10))
    for i in range(3)
]

@pytest.mark.parametrize("test_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, test_contact):
    old_contacts = app.contact.get_list_contact()
    app.contact.create(test_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list_contact()
    old_contacts.append(test_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

