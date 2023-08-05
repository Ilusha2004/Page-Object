import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: ['--browser_name=safari'\n'--browser_name=chrome'\n'--browser_name=firefox'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None

    if browser_name == "safari":
        options = webdriver.safari.options.Options()
        browser = webdriver.Safari(options=options)
        print("\nStarting Safari..")
    elif browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        print("\nStarting Сhrome..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        print("\nStarting Firefox..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or safari")

    yield browser
    print("\nquit..")
    browser.quit()
