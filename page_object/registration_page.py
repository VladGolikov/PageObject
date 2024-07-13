from page_object.base import Base


class RegistrationPage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.base = Base(browser)

    def check_elem_on_page(self):
        self.base.element_visibility(selector='//*[@id="input-firstname"]')
        self.base.element_visibility(selector='//*[@id="input-password"]')
        self.base.element_visibility(selector='//*[@id="account-register"]/ul/li[3]/a')
        self.base.element_clickable(selector='//*[@id="logo"]')
        self.base.element_clickable(selector='//*[@id="input-newsletter"]')
