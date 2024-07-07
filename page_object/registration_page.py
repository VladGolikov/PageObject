from page_object.main_method import MainMethod as MM


class RegistrationPage:
    def __init__(self, browser) -> None:
        self.browser = browser

    def check_elem_on_page(self):
        MM(browser=self.browser).element_visibility(selector='//*[@id="input-firstname"]')
        MM(browser=self.browser).element_visibility(selector='//*[@id="input-password"]')
        MM(browser=self.browser).element_visibility(selector='//*[@id="account-register"]/ul/li[3]/a')
        MM(browser=self.browser).element_clickable(selector='//*[@id="logo"]')
        MM(browser=self.browser).element_clickable(selector='//*[@id="input-newsletter"]')
