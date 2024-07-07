from page_object.main_method import MainMethod as MM
from page_object.administration_page import AdministrationPage as AP
from page_object.registration_page import RegistrationPage as RP


def test_main_page(browser):
    """Проверка элементов на главной странице"""
    MM(browser=browser).element_visibility(selector='//*[@id="logo"]/a/img')
    MM(browser=browser).element_clickable(selector='//*[@id="narbar-menu"]/ul/li[6]')
    MM(browser=browser).element_visibility(selector='//*[@id="content"]/div[2]/div[3]/div/div[1]')
    MM(browser=browser).not_element_visibility(selector='//*[@id="test"]')
    MM(browser=browser).element_clickable(selector='//*[@id="search"]/input')


def test_catalog(browser):
    """Проверка элементов в каталоге"""
    MM(browser=browser).add_url_to_browser(added_url='index.php?route=product/category&language'
                                                     '=en-gb&path=25_28')
    MM(browser=browser).element_visibility(selector='//*[@id="logo"]')
    MM(browser=browser).comparing_the_current_address(address='http://172.16.16.249:8081/index.php?route=product'
                                                              '/category&language=en-gb&path=25_28')
    MM(browser=browser).element_clickable(selector='//*[@id="header-cart"]/div/button')

    MM(browser=browser).element_clickable(selector='//*[@id="product-list"]/div/div/div[1]')
    MM(browser=browser).element_clickable(selector='//*[@id="search"]/input')
    MM(browser=browser).element_visibility(selector='//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span')


def test_goods_cart(browser):
    """Проверка элементов на странице карточки товара"""
    MM(browser=browser).add_url_to_browser(added_url='index.php?route=product/product&language=en'
                                                     '-gb&product_id=49&path=57')
    MM(browser=browser).comparing_the_current_address(address='http://172.16.16.249:8081/index.php?route=product'
                                                              '/product&language=en-gb&product_id=49&path=57')
    MM(browser=browser).element_visibility(selector='//*[@id="header-cart"]/div/button')
    MM(browser=browser).element_visibility(selector='//*[@id="content"]/div[1]/div[1]/div/div/a[5]/img')
    MM(browser=browser).element_clickable(selector='//*[@id="button-cart"]')
    MM(browser=browser).element_visibility(selector='//*[@id="content"]/ul/li[2]/a')
    MM(browser=browser).not_element_visibility(selector='//*[@id="test"]/input[3]')


def test_admin_page(browser):
    """Проверка элементов на странице логина"""
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).check_elem_on_page()


def test_register_user(browser):
    """Проверка элементов на странице регистрации пользователя"""
    MM(browser=browser).add_url_to_browser(added_url='index.php?route=account/register')
    MM(browser=browser).comparing_the_current_address(address='http://172.16.16.249:8081/index.php?route=account'
                                                              '/register')
    RP(browser=browser).check_elem_on_page()
