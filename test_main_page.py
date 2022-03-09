from main_page import MainPage
import pytest
from locators import AllNavLinks


def test_main_links(browser):
    link = "https://www.dns-shop.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_right_names_of_links()


def test_visibility(browser):
    link = "https://www.dns-shop.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_visible_all_main_category_links()


def test_sub_links(browser):
    link = "https://www.dns-shop.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_right_names_of_sub_links()

def test_visibility_sub(browser):
    link = "https://www.dns-shop.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_visible_all_sub_category_links()


def test_main_nav_link(browser):
    link = "https://www.dns-shop.ru/"
    page = MainPage(browser, link)
    page.open()
    page.get_main_category_link_by_name("Бытовая техника").click()

@pytest.mark.parametrize("name", AllNavLinks.MAIN_NAV_LINKS_TEXT)
def test_go_to_all_main_categories(browser_session, name):
    link = "https://www.dns-shop.ru/"
    page = MainPage(browser_session, link)
    page.open()
    page.get_main_category_link_by_name(name).click()
    page.check_categories()

