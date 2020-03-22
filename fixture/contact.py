from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def back_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def back_to_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") or wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def filling_birthday(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[18]").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='July']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)

    def fill_from(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.home_page)
        self.change_field_value("phone2", contact.phone2)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_form()
        # filling fields
        self.fill_from(contact)
        self.filling_birthday(contact)
        # complete create
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.back_to_home()
        self.cash_contact = None

    def delete_first_contact(self):
        self.delete_some_contact(0)

    def delete_some_contact(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # click "Delete"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # click "OK"
        wd.switch_to_alert().accept()
        # пришлось добавить т.к. иначе не успевает измениться current_url
        time.sleep(1)
        self.back_to_home()
        self.cash_contact = None

    def edit_by_id(self, contact, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % index).click()
        self.fill_from(contact)
        # save changes
        wd.find_element_by_xpath("(//input[@value='Update'])[2]").click()
        self.back_to_home()
        self.cash_contact = None

    def count(self):
        wd = self.app.wd
        self.back_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    cash_contact = None

    def get_list_contact(self):
        wd = self.app.wd
        if self.cash_contact is None:
            self.back_to_home()
            self.cash_contact = []
            for element in wd.find_elements_by_name("entry"):
                row = element.find_elements_by_tag_name("td")
                id = row[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = row[1].text
                firstname = row[2].text
                allphones = row[5].text
                self.cash_contact.append(Contact(last_name=lastname, first_name=firstname, all_phones_in_contact=allphones, id=id))
        return list(self.cash_contact)

    def get_phones_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        home_phone = wd.find_element_by_xpath("//input[@name='home']").get_attribute("value")
        mobile_phone = wd.find_element_by_xpath("//input[@name='mobile']").get_attribute("value")
        work_phone = wd.find_element_by_xpath("//input[@name='work']").get_attribute("value")
        second_phone = wd.find_element_by_xpath("//input[@name='phone2']").get_attribute("value")
        return Contact(home=home_phone, mobile=mobile_phone, work=work_phone, phone2=second_phone)

    def get_phones_from_details_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search('H: (.*)', text).group(1)
        mobile_phone = re.search('M: (.*)', text).group(1)
        work_phone = re.search('W: (.*)', text).group(1)
        second_phone = re.search('P: (.*)', text).group(1)
        return Contact(home=home_phone, mobile=mobile_phone, work=work_phone, phone2=second_phone)

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.back_to_home()
        contacts = wd.find_elements_by_name("entry")
        id = contacts[index].find_element_by_name("selected[]").get_attribute("value")
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.back_to_home()
        contacts = wd.find_elements_by_name("entry")
        id = contacts[index].find_element_by_name("selected[]").get_attribute("value")
        wd.find_element_by_xpath("//a[@href='view.php?id=%s']" % id).click()

