from selenium.webdriver.support.ui import Select
from model.contact import Contact

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

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

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

    def create(self, contact):
        wd = self.app.wd
        self.open_add_form()
        # filling fields
        self.fill_from(contact)
        self.filling_birthday(contact)
        # complete create
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.back_to_home()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click "Delete"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # click "OK"
        #wd.find_element_by_link_text("ОК").click()
        wd.switch_to_alert().accept()
        self.back_to_home()

    def edit_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_from(contact)
        # save changes
        wd.find_element_by_xpath("(//input[@value='Update'])[2]").click()

    def count(self):
        wd = self.app.wd
        self.back_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    def get_list_contact(self):
        wd = self.app.wd
        self.back_to_home()
        res = []
        for element in wd.find_elements_by_name("entry"):
            x = element.find_elements_by_tag_name("td")
            id = x[0].find_element_by_name("selected[]").get_attribute("value")
            lastname = x[1].text
            firstname = x[2].text
            res.append(Contact(last_name=lastname, first_name=firstname, id=id))
        return res
        # for element in wd.find_elements_by_css_selector("span.group"):
        #     text = element.text
        #     id = element.find_element_by_name("selected[]").get_attribute("value")
