from time import sleep
from page_object.base import Base
from page_object.administration_page import AdministrationPage


def test_add_new_product_in_admin_panel(browser):
    admin = AdministrationPage(browser)
    admin.go_to_admin_page()
    admin.login_admin()
    admin.go_to_my_product()
    admin.add_new_product()


def test_dell_product_in_admin_panel(browser):
    admin = AdministrationPage(browser)
    admin.go_to_admin_page()
    admin.login_admin()
    admin.go_to_my_product()
    admin.dell_product()


def test_new_user_registration(browser):
    base = Base(browser)
    base.get_link(link='http://172.16.16.249:8081/index.php?route=account/register')
    base.send_text_to_elem_by_xpath(selector='//*[@id="input-firstname"]',
                                                   text_for_send="Vlad")
    base.send_text_to_elem_by_xpath(selector='//*[@id="input-lastname"]',
                                                   text_for_send="Golikov")
    base.send_text_to_elem_by_xpath(selector='//*[@id="input-email"]',
                                                   text_for_send="234@mail.ru")
    base.send_text_to_elem_by_xpath(selector='//*[@id="input-password"]',
                                                   text_for_send="12345678!Qq")
    base.click_to_element(selector='//*[@id="form-register"]/div/div/input')
    base.click_to_element(selector='//*[@id="form-register"]/div/button')
    base.elem_by_xpath(selector='//*[@id="content"]/h1')
    sleep(5)
    base.check_text_and_compariso(selector='//*[@id="content"]/h1')
