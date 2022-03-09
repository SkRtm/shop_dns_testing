from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        
        except NoSuchElementException:
            return False

        return True

    def is_visible(self, method, locator):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((method, locator)))
        except TimeoutException:
            return False
        
        return True

    def are_visible(self, method, locator):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located((method, locator)))
        except TimeoutException:
            return False
        
        return True

    def get_element_by_text(self, elements, name):
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]