

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create_new(self, group):
        wd = self.app.wd
        self.open_group_page()
        # create new group
        wd.find_element_by_name("new").click()
        # fill group from
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # complete create
        wd.find_element_by_name("submit").click()

    def back_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()