# -*- coding: utf-8 -*-
import pytest
import unittest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_new_contact(Contact(first_name =u"Иван", middle_name =u"Иванович", last_name =u"Иванов",
                                            nickname = "Ivan!", company = "Booking Mashin", title = "Ivyshka",
                                            address = "Pyshkina st home Kolotyshkina 5", home = "123456789", mobile = "+987654321",
                                            work = "14946", fax = "228", email1 = "123@mail.ru", email2 = "321@mail.ru",
                                            email3 = "333@mail.ru", home_page = "ok.ru", bday = "16", bmonth = "July", byear = "1995"))
        app.session.logout()

if __name__ == "__main__":
    unittest.main()
