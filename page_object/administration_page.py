from time import sleep
import pyautogui

from page_object.base import Base


class AdministrationPage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.base = Base(browser)

    def check_elem_on_page(self):
        """Проверка элементов на странице авторизации под администратором"""

        self.base.element_visibility(selector='//*[@id="header"]/div/a')
        self.base.element_clickable(selector='//*[@id="input-username"]')
        self.base.element_clickable(selector='//*[@id="input-password"]')
        self.base.element_clickable(selector='//*[@id="form-login"]/div[3]/button')
        self.base.element_visibility(selector='//*[@id="footer"]')

    def go_to_admin_page(self):
        """Переход на страницу аминистратора с главной страницы"""
        # elf.logger.debug("Возвращаю текст элемента по селектору: ")
        self.base.add_url_to_browser(added_url='administration/')
        self.base.comparing_the_current_address(address='http://192.168.5.8:8081/administration/')

    def login_admin(self):
        """Авторизация на странице администратора"""
        self.base.send_text_to_elem_by_xpath(selector='//*[@id="input-username"]', text_for_send='user')
        sleep(2)
        self.base.send_text_to_elem_by_xpath(selector='//*[@id="input-password"]', text_for_send='bitnami')
        self.base.click_to_element(selector='//*[@id="form-login"]/div[3]/button')
        sleep(2)
        self.base.element_visibility(selector='//*[@id="nav-logout"]/a')

    def logout_admin(self):
        """Выход из панели администратора с основной страницы администратора"""
        self.base.click_to_element(selector='//*[@id="nav-logout"]')
        sleep(3)
        self.base.comparing_the_current_address(
            address='http://192.168.5.8:8081/administration/index.php?route=common/login')

    def go_to_my_product(self):
        """Переход с главной страницы аминистратора к товарам администратора"""
        self.base.click_to_element(selector='//*[@id="menu-catalog"]')
        self.base.click_to_element(selector='//*[@id="collapse-1"]/li[2]')

    def add_new_product(self):
        """Добавление нового продукта в панеле администратора из вкладки 'Products'"""
        self.base.click_to_element(selector='//*[@id="content"]/div[1]/div/div/a')
        self.base.send_text_to_elem_by_xpath(selector='//*[@id="input-name-1"]',
                                             text_for_send='New Product')
        self.base.send_text_to_elem_by_xpath(selector='//*[@id="input-meta-title-1"]',
                                             text_for_send='New Product')
        self.base.send_text_to_elem_by_xpath(selector='/html/body',
                                             text_for_send='Тестовое добавление нового товара')
        self.base.click_to_element(selector='//*[@id="form-product"]/ul/li[2]/a')
        self.base.send_text_to_elem_by_xpath(selector='//*[@id="input-model"]',
                                             text_for_send='Test_model')
        self.base.click_to_element(selector='//*[@id="content"]/div[1]//button')

    def dell_product(self):
        self.base.click_to_element(selector='//*[@id="form-product"]/div[1]/table/tbody/tr/td[1]/input')
        pyautogui.press('enter')
