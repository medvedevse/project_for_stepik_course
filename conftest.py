import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language',
                     action="store",
                     default="en",
                     help="Choose es or fr language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language == "es":
        print("\nstart Chrome..")
        options = Options()

        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif user_language == "fr":
        print("\nstart Chrome..")
        options = Options()

        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif user_language == "en":
        print("\nstart Chrome..")
        options = Options()

        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language es or fr should be choose")

    yield browser
    print('\nqiut browser..')
    browser.quit()