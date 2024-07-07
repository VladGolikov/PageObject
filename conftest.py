import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="choose browser"
    )
    parser.addoption(
        "--headless", action="store_true", help="headless_mode"
    )
    parser.addoption(
        "--url", action="store", default="http://172.16.16.249:8081"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless_mode = request.config.getoption('--headless')
    url = request.config.getoption("--url")

    if browser_name == 'firefox':
        options = FFOptions()
        if headless_mode:
            options.add_argument('--headless')
        options.binary_location = 'p'
        driver = webdriver.Firefox(options=options)
    elif browser_name == 'chrome':
        options = Options()
        if headless_mode:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f'Browser {browser_name} not supported')

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
