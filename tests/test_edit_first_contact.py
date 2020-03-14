from model.contact import Contact
import time

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name =u"Иван", middle_name =u"Иванович", last_name =u"Иванов",
                                   nickname = "Ivan!", company = "Booking Mashin", title = "Ivyshka",
                                   address = "Pyshkina st home Kolotyshkina 5", home = "123456789", mobile = "+987654321",
                                  work = "14946", fax = "228", email1 = "123@mail.ru", email2 = "321@mail.ru",
                                  email3 = "333@mail.ru", home_page = "ok.ru", bday = "16", bmonth = "July", byear = "1995"))
        app.contact.back_to_home()
    app.contact.edit_first(Contact(first_name=u"Петр", middle_name=u"Петрович", last_name=u"Петров",
                                   nickname="Petr!", company="Petrs Mashin", title="Pet9",
                                   address="Pyshkina st home Kolotyshkina 6", home="987654321", mobile="+12345678",
                                   work="14946", fax="228", email1="111@mail.ru", email2="222@mail.ru",
                                   email3="333@mail.ru", home_page="vk.com", bday="16", bmonth="June", byear="1990"))
    app.contact.back_to_home_page()
