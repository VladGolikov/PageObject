import allure

from page_object.start_page import StartPage


@allure.step("Проверка добавления товара в корзину")
def test_add_to_cart(browser):
    page = StartPage(browser)
    page.checking_the_shopping_cart()
    index = page.adding_product()
    page.scrolling_the_page_to_the_shopping_cart()
    page.check_cart(index=index)
