from time import sleep
import pyautogui

from page_object.main_method import MainMethod as MM


class AdministrationPage:
    def __init__(self, browser) -> None:
        self.browser = browser

    def check_elem_on_page(self):
        """Проверка элементов на странице авторизации под администратором"""
        MM(browser=self.browser).element_visibility(selector='//*[@id="header"]/div/a')
        MM(browser=self.browser).element_clickable(selector='//*[@id="input-username"]')
        MM(browser=self.browser).element_clickable(selector='//*[@id="input-password"]')
        MM(browser=self.browser).element_clickable(selector='//*[@id="form-login"]/div[3]/button')
        MM(browser=self.browser).element_visibility(selector='//*[@id="footer"]')

    def go_to_admin_page(self):
        """Переход на страницу аминистратора с главной страницы"""
        MM(browser=self.browser).add_url_to_browser(added_url='administration/')
        MM(browser=self.browser).comparing_the_current_address(address='http://172.16.16.249:8081/administration/')

    def login_admin(self):
        """Авторизация на странице администратора"""
        MM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-username"]', text_for_send='user')
        MM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-password"]', text_for_send='bitnami')
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-login"]/div[3]/button')
        sleep(2)
        MM(browser=self.browser).element_visibility(selector='//*[@id="nav-logout"]/a')

    def logout_admin(self):
        """Выход из панели администратора с основной страницы администратора"""
        MM(browser=self.browser).click_to_element(selector='//*[@id="nav-logout"]')
        sleep(3)
        MM(browser=self.browser).comparing_the_current_address(
            address='http://172.16.16.249:8081/administration/index.php?route=common/login')

    def go_to_my_product(self):
        """Переход с главной страницы аминистратора к товарам администратора"""
        MM(browser=self.browser).click_to_element(selector='//*[@id="menu-catalog"]')
        MM(browser=self.browser).click_to_element(selector='//*[@id="collapse-1"]/li[2]')

    def add_new_product(self):
        """Добавление нового продукта в панеле администратора из вкладки 'Products'"""
        MM(browser=self.browser).click_to_element(selector='//*[@id="content"]/div[1]/div/div/a')
        MM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-name-1"]',
                                                            text_for_send='New Product')
        MM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-meta-title-1"]',
                                                            text_for_send='New Product')
        MM(browser=self.browser).send_text_to_elem_by_xpath(selector='/html/body',
                                                            text_for_send='Тестовое добавление нового товара')
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-product"]/ul/li[2]/a')
        MM(browser=self.browser).send_text_to_elem_by_xpath(selector='//*[@id="input-model"]',
                                                            text_for_send='Test_model')
        MM(browser=self.browser).click_to_element(selector='//*[@id="content"]/div[1]//button')

    def dell_product(self):
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-product"]/div[1]/table/tbody/tr/td[1]/input')
        pyautogui.press('enter')
