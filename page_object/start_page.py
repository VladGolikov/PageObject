from time import sleep
from selenium.webdriver.common.by import By
from page_object.main_method import MainMethod as MM


class StartPage:
    def __init__(self, browser) -> None:
        self.browser = browser

    def checking_the_shopping_cart(self):
        span_elem = MM(browser=self.browser).elem_by_xpath(selector='//*[@id="header-cart"]/div/button')
        if span_elem.text != '0 item(s) - $0.00':
            raise ValueError(f'Корзина уже заполнена: {span_elem.text}')

    def adding_product(self, index=1):
        elem = self.browser.find_element(By.XPATH,
                                         f'//*[@id="content"]/div[2]/div[{index}]/div/div[2]/form/div/button[1]')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem)
        sleep(2)
        elem.click()

    def scrolling_the_page_to_the_shopping_cart(self):
        MM(browser=self.browser).scrolling_to_elem

    def check_cart(self, index):
        span_elem = self.browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
        if index == 1:
            if span_elem.text != '1 item(s) - $602.00':
                raise ValueError(f'Корзина уже заполнена: {span_elem.text}')
        elif index == 2:
            if span_elem.text != '1 item(s) - $123.20':
                raise ValueError(f'Корзина уже заполнена: {span_elem.text}')

    def change_currency_to_euro(self):
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-currency"]/div/a')
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-currency"]/div/ul/li[1]/a')

    def change_currency_to_pounds(self):
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-currency"]/div/a')
        MM(browser=self.browser).click_to_element(selector='//*[@id="form-currency"]/div/ul/li[2]/a')

    def check_elem_price_in_euro(self, selector):
        """Проверка цены в евро на главной странице"""
        element = self.browser.find_element(By.XPATH, selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(2)
        if element.text != '472.33€':
            raise ValueError(f'Цена не изменилась на евро: {element.text}')

    def check_currency_added_elem(self, selector):
        """Проверка на главной странице цена в корзине в евро"""
        element = self.browser.find_element(By.XPATH, selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(2)

        if element.text != '1 item(s) - 472.33€':
            raise ValueError(f'Цена не изменилась на евро в корзине на главной: {element.text}')

    def go_to_catalog_desktops(self):
        MM(browser=self.browser).click_to_element(selector='//*[@id="narbar-menu"]/ul/li[1]/a')
        MM(browser=self.browser).click_to_element(selector='//*[@id="narbar-menu"]/ul/li[1]/div/a')
