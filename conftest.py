import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None

    if language == "en":
        browser = webdriver.Safari()      # If you user of MacOS
        # browser = webdriver.Chrome()    # If not Choose Chrome or other webdrivers
        print(f"\nstart {language}")
    else:
        raise pytest.UsageError("--language should be: en")

    yield browser
    print("\nquit..")
    browser.quit()
