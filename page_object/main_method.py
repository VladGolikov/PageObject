from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainMethod:
    def __init__(self, browser) -> None:
        self.browser = browser

    def elem_by_xpath(self, selector):
        """Вовзращает элемент по XPATH"""
        return self.browser.find_element(By.XPATH, selector)

    def scrolling_to_elem(self, selector):
        """Прокручивает до элемента по XPATH"""
        elem = self.browser.find_element(By.XPATH, selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem)
        sleep(2)

    def element_visibility(self, selector, wait_time=1):
        """Проверяет что элемент виден на странице по XPATH"""
        return WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located((By.XPATH, selector)))

    def not_element_visibility(self, selector, wait_time=1):
        """Проверяет что элемент НЕ виден на странице по XPATH"""
        return WebDriverWait(self.browser, wait_time).until_not(EC.visibility_of_element_located((By.XPATH, selector)))

    def element_clickable(self, selector, wait_time=1):
        """Проверяет что элемент кликабельный на странице по XPATH"""
        return WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector)))

    def add_url_to_browser(self, added_url):
        """К текущему url добавляет продолжение"""
        self.browser.get(self.browser.current_url + added_url)

    def comparing_the_current_address(self, address):
        """Проверяет текущий адресс с пользовательским значением"""
        test_check_url = self.browser.current_url
        if test_check_url != address:
            raise ValueError(f'Тест находится на другой странице: {test_check_url}')

    def send_text_to_elem_by_xpath(self, selector, text_for_send, wait_time=1):
        """Вписывает текст в элемент типа input по XPATH"""
        elem = self.browser.find_element(By.XPATH, selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem)
        sleep(3)
        WebDriverWait(self.browser, wait_time).until(EC.visibility_of_element_located((By.XPATH, selector))).send_keys(
            text_for_send)

    def click_to_element(self, selector, wait_time=2):
        """Проверяет что элемент кликабельный и нажимает на него"""
        elem = self.browser.find_element(By.XPATH, selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem)
        WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector))).click()

    def get_link(self, link):
        self.browser.get(link)

    def check_text_and_compariso(self, selector, text_comparison='Your Account Has Been Created!'):
        text_elem = MainMethod(browser=self.browser).elem_by_xpath(selector=selector).text
        if text_elem != text_comparison:
            raise ValueError(f'Регистрация не успешна')

    def checking_price_of_elem_in_pounds(self, selector):
        """Прокручивает до элемента и проверяет что его цена в фунтах"""
        element = self.browser.find_element(By.XPATH, selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(2)
        if element.text[0] != '£':
            raise ValueError(f'Цена не изменилась на фунты стерлингов: {element.text}')
