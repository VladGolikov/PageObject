from page_object.administration_page import AdministrationPage as AP


def test_authorization_logout(browser):
    """Вход и выход в админку с проверкой"""

    AP(browser=browser).go_to_admin_page()
    AP(browser=browser).login_admin()
    AP(browser=browser).logout_admin()

