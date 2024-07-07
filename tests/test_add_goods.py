from page_object.start_page import StartPage as SP


def test_add_to_cart(browser):
    """проверка добавления товара в корзину"""
    SP(browser).checking_the_shopping_cart()
    index = SP(browser).adding_product()
    SP(browser).scrolling_the_page_to_the_shopping_cart()
    SP(browser).check_cart(index=index)
