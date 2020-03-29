import pytest
from fixture.application import Application

fixture = None

@pytest.fixture()
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if fixture is None:
        fixture = Application(browser=browser, home_url=url)
    else:
        if not fixture.isvalid():
            fixture = Application(browser=browser, home_url=url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--url", action = "store", default = "http://localhost/addressbook/")