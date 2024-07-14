import allure

from page_object.base import Base
from page_object.administration_page import AdministrationPage
from page_object.registration_page import RegistrationPage


@allure.step("Проверка элементов на главной странице")
def test_main_page(browser):
    base = Base(browser)
    base.element_visibility(selector='//*[@id="logo"]/a/img')
    base.element_clickable(selector='//*[@id="narbar-menu"]/ul/li[6]')
    base.element_visibility(selector='//*[@id="content"]/div[2]/div[3]/div/div[1]')
    base.not_element_visibility(selector='//*[@id="test"]')
    base.element_clickable(selector='//*[@id="search"]/input')


@allure.step("Проверка элементов в каталоге")
def test_catalog(browser):
    base = Base(browser)
    base.add_url_to_browser(added_url='index.php?route=product/category&language'
                                      '=en-gb&path=25_28')
    base.element_visibility(selector='//*[@id="logo"]')
    base.comparing_the_current_address(address='http://192.168.5.8:8081/index.php?route=product'
                                               '/category&language=en-gb&path=25_28')
    base.element_clickable(selector='//*[@id="header-cart"]/div/button')

    base.element_clickable(selector='//*[@id="product-list"]/div/div/div[1]')
    base.element_clickable(selector='//*[@id="search"]/input')
    base.element_visibility(selector='//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span')


@allure.step("Проверка элементов на странице карточки товара")
def test_goods_cart(browser):
    base = Base(browser)
    base.add_url_to_browser(added_url='index.php?route=product/product&language=en'
                                      '-gb&product_id=49&path=57')
    base.comparing_the_current_address(address='http://192.168.5.8:8081/index.php?route=product'
                                               '/product&language=en-gb&product_id=49&path=57')
    base.element_visibility(selector='//*[@id="header-cart"]/div/button')
    base.element_visibility(selector='//*[@id="content"]/div[1]/div[1]/div/div/a[5]/img')
    base.element_clickable(selector='//*[@id="button-cart"]')
    base.element_visibility(selector='//*[@id="content"]/ul/li[2]/a')
    base.not_element_visibility(selector='//*[@id="test"]/input[3]')


@allure.step("Проверка элементов на странице логина")
def test_admin_page(browser):
    admin = AdministrationPage(browser)
    admin.go_to_admin_page()
    admin.check_elem_on_page()


@allure.step("Проверка элементов на странице регистрации пользователя")
def test_register_user(browser):
    base = Base(browser)
    register = RegistrationPage(browser)
    base.add_url_to_browser(added_url='index.php?route=account/register')
    base.comparing_the_current_address(address='http://192.168.5.8:8081/index.php?route=account'
                                               '/register')
    register.check_elem_on_page()
