from model.group import Group
import random
import string

def ren_random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ ' '*10
    return prefix + ''.join(random.choice(symbols) for x in range(random.randrange(maxlen)))

testdata = [Group(name="", header="", footer="")] + [
    Group(name=ren_random_string("name", 10), header=ren_random_string("header", 10), footer=ren_random_string("footer", 5))
    for i in range(3)
    # пример создания данных с перебором списка возможных значений каждого из полей
    # for name in ['', ren_random_string("name", 10)]
    # for header in ['', ren_random_string("header", 10)]
    # for footer in ['', ren_random_string("footer", 5)]
]

constant_data = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]