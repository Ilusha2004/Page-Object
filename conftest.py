import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "en":
        browser = webdriver.Safari()
        print("\nstart  en")
    else:
        raise pytest.UsageError("--language should be english")
    yield browser
    print("\nquit..")
    browser.quit()
