from time import sleep

from page_object.start_page import StartPage as SP
from page_object.main_method import MainMethod as MM


def test_switch_currency_catalog(browser):
    """Меняю валюту и проверяю на главное странице что она изменилась"""
    SP(browser=browser).change_currency_to_pounds()
    SP(browser=browser).go_to_catalog_desktops()
    sleep(5)
    MM(browser=browser).scrolling_to_elem(selector='//*[@id="product-list"]/div[4]/div')
    MM(browser=browser).checking_price_of_elem_in_pounds(selector='//*[@id="product-list"]/div[4]/div/div['
                                                                  '2]/div/div/span[1]')


def test_switch_currency_main(browser):
    """Проверка смены валюты на главной странице"""
    SP(browser=browser).change_currency_to_euro()

    SP(browser=browser).check_elem_price_in_euro(selector='//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
    MM(browser=browser).click_to_element(selector='//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    MM(browser=browser).scrolling_to_elem(selector='//*[@id="header-cart"]/div/button')
    sleep(2)
    SP(browser=browser).check_currency_added_elem(selector='//*[@id="header-cart"]/div/button')
