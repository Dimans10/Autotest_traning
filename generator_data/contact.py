from model.contact import Contact
import random
import string
import getopt
import sys
import os
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(path_file, "w") as write_file:
    jsonpickle.set_encoder_options("json", indent=2)
    write_file.write(jsonpickle.encode(testdata))