from time import sleep
from page_object.main_method import MainMethod as MM


from page_object.administration_page import AdministrationPage as AP


def test_add_new_product_in_admin_panel(browser):
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).login_admin()
    AP(browser=browser).go_to_my_product()
    AP(browser=browser).add_new_product()


def test_dell_product_in_admin_panel(browser):
    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).login_admin()
    AP(browser=browser).go_to_my_product()
    AP(browser=browser).dell_product()


def test_new_user_registration(browser):
    MM(browser=browser).get_link(link='http://172.16.16.249:8081/index.php?route=account/register')
    MM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-firstname"]',
                                                   text_for_send="Vlad")
    MM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-lastname"]',
                                                   text_for_send="Golikov")
    MM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-email"]',
                                                   text_for_send="234@mail.ru")
    MM(browser=browser).send_text_to_elem_by_xpath(selector='//*[@id="input-password"]',
                                                   text_for_send="12345678!Qq")
    MM(browser=browser).click_to_element(selector='//*[@id="form-register"]/div/div/input')
    MM(browser=browser).click_to_element(selector='//*[@id="form-register"]/div/button')
    MM(browser=browser).elem_by_xpath(selector='//*[@id="content"]/h1')
    sleep(5)
    MM(browser=browser).check_text_and_compariso(selector='//*[@id="content"]/h1')
