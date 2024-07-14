import allure

from page_object.administration_page import AdministrationPage


@allure.step("Вход и выход в админку с проверкой")
def test_authorization_logout(browser):
    admin = AdministrationPage(browser)
    admin.go_to_admin_page()
    admin.login_admin()
    admin.logout_admin()

