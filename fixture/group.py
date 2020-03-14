
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def back_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def back_to_home(self):
        wd = self.app.wd
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

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # create new group
        wd.find_element_by_name("new").click()
        # fill group from
        self.fill_form(group)
        # complete create
        wd.find_element_by_name("submit").click()
        self.back_to_group_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # click "delete groups"
        wd.find_element_by_name("delete").click()
        self.back_to_group_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        self.fill_form(group)
        wd.find_element_by_xpath("//input[@value='Update']").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return  len(wd.find_elements_by_name("selected[]"))