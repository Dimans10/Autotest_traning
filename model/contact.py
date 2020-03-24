from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None, home_page=None, bday=None,
                 bmonth=None, byear=None, phone2=None, id=None, all_phones_in_contact=None, all_emails_in_contact=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.phone2 = phone2
        self.id = id
        self.all_phones_in_contact = all_phones_in_contact
        self.all_emails_in_contact = all_emails_in_contact

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.last_name, self.first_name, self.address, self.mobile, self.work, self.home, self.email1, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.last_name == other.last_name and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize