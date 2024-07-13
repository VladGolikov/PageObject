import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options
import logging
import datetime
import allure
import json


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
    # parser.addoption(
    #     "--log_level", default="INFO"
    # )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless_mode = request.config.getoption('--headless')
    url = request.config.getoption("--url")
    # log_level = request.config.getoption("--log_level")
    # logger = logging.getLogger(request.node.name)
    # file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    # file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    # logger.addHandler(file_handler)
    # logger.setLevel(level=log_level)
    #
    # logger.info(f"Test {request.node.name} startet at {datetime.datetime.now()}")

    # allure.attach(
    #     name=browser_name.session_id,
    #     body=json.dumps(browser_name.capabilities, indent=4, ensure_ascii=False),
    #     attachment_type=allure.attachment_type.JSON)

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

    # if request.node.status == "failed":
    #     allure.attach(
    #         name="failure_screenshot",
    #         body=browser_name.get_screenshot_as_png(),
    #         attachment_type=allure.attachment_type.PNG
    #     )
    #     allure.attach(
    #         name="page_source",
    #         body=browser_name.page_source,
    #         attachment_type=allure.attachment_type.HTML
    #     )

    # logger.info("Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
    return driver
