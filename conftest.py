import pytest
from fixture.application import Application
import json

fixture = None
target = None

@pytest.fixture()
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open (request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.isvalid():
        fixture = Application(browser=browser, home_url=target['home_url'])
    fixture.session.ensure_login(target['username'], target['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--target", action = "store", default = "target.json")