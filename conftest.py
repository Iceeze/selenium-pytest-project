import argparse
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser: argparse.ArgumentParser) -> None:
    parser.addoption("--language", action="store", default="en", help="Выберите язык отображения")


@pytest.fixture(scope="function")
def browser(request: pytest.fixture) -> webdriver.Chrome:
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
