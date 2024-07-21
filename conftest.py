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
        "--url", action="store", default="http://192.168.5.8:8081"
    )
    parser.addoption(
        "--log_level", default="DEBUG"
    )
    parser.addoption(
        "--executor", action="store", default="192.168.5.8"
    )
    parser.addoption(
        "--vnc", action="store_true"
    )
    #оставлено для примера
    # parser.addoption(
    #     "--logs", action="store_true"
    # )
    # parser.addoption(
    #     "--video", action="store_true"
    #)
    parser.addoption(
        "--bv"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless_mode = request.config.getoption('--headless')
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    #оставлено для примера
    # logs = request.config.getoption("--logs")
    # video = request.config.getoption("--video")

    executor_url = f"http://{executor}:4444/wd/hub"

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

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

    # allure.attach(
    #     name=driver.session_id,
    #     body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
    #     attachment_type=allure.attachment_type.JSON)

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": request.node.name,
            "screenResolution": "1280x720",
            #оставлено для примера
            # "enableVideo": video,
            # "enableLog": logs,
            "sessionTimeout": "30m"
        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )

    driver.maximize_window()
    driver.get(url)
    driver.url = url
    driver.logger = logger
    logger.info("Browser %s started" % driver)

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML
        )

    driver.close()
    logger.info("Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
