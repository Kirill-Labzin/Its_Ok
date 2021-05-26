from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

timer = 2
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_go_to_add_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_basket()
    page.solve_quiz_and_get_code()
    time.sleep(timer)
