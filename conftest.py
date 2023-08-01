import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en-gb")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "en-gb":
        browser = webdriver.Safari()
        print("\nstart en-gb")
    else:
        raise pytest.UsageError("--language should be: en-gb")
    yield browser
    print("\nquit..")
    browser.quit()
