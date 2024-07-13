from page_object.administration_page import AdministrationPage


def test_authorization_logout(browser):
    """Вход и выход в админку с проверкой"""
    admin = AdministrationPage(browser)
    admin.go_to_admin_page()
    admin.login_admin()
    admin.logout_admin()

