from model.group import Group
import string
import random
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/group.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def ren_random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ ' '*10
    return prefix + ''.join(random.choice(symbols) for x in range(random.randrange(maxlen)))

testdata = [Group(name="", header="", footer="")] + [
    Group(name=ren_random_string("name", 10), header=ren_random_string("header", 10), footer=ren_random_string("footer", 5))
    for i in range(n)
]

path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(path_file, "w") as write_file:
    jsonpickle.set_encoder_options("json", indent=2)
    write_file.write(jsonpickle.encode(testdata))
