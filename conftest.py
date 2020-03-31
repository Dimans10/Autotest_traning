import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.db import Dbfixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open (config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.isvalid():
        fixture = Application(browser=browser, home_url=web_config['home_url'])
    fixture.session.ensure_login(web_config['username'], web_config['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

@pytest.fixture(scope="session", autouse=True)
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = Dbfixture(host=db_config["host"] , db=db_config["db"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--target", action = "store", default = "target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_data_test_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_data_test_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_data_test_module(module):
    return importlib.import_module("data.%s" % module).constant_data

def load_data_test_json(name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % name)) as f:
        return jsonpickle.decode(f.read())