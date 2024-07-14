from time import sleep

import allure

from page_object.start_page import StartPage
from page_object.base import Base


@allure.step("Меняю валюту и проверяю на главное странице что она изменилась")
def test_switch_currency_catalog(browser):
    page = StartPage(browser)
    base = Base(browser)
    page.change_currency_to_pounds()
    page.go_to_catalog_desktops()
    sleep(5)
    base.scrolling_to_elem(selector='//*[@id="product-list"]/div[4]/div')
    base.checking_price_of_elem_in_pounds(selector='//*[@id="product-list"]/div[4]/div/div['
                                                   '2]/div/div/span[1]')


@allure.step("Проверка смены валюты на главной странице")
def test_switch_currency_main(browser):
    page = StartPage(browser)
    base = Base(browser)
    page.change_currency_to_euro()
    page.check_elem_price_in_euro(selector='//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    base.click_to_element(selector='//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    base.scrolling_to_elem(selector='//*[@id="header-cart"]/div/button')
    sleep(2)
    page.check_currency_added_elem(selector='//*[@id="header-cart"]/div/button')
