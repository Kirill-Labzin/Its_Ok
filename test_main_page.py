from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_should_be_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
