from base_page import BasePage
from locators import AllNavLinks
from locators import CategoryLabels


class MainPage(BasePage):
    
    def get_all_links_from_main_categories(self):
        return self.browser.find_elements(*AllNavLinks.MAIN_NAV_LINKS)

    def get_text_from_all_main_categories_links(self): 
        main_links = self.get_all_links_from_main_categories()
        return [link.text for link in main_links]

    def should_be_right_names_of_links(self):
        self.get_all_links_from_main_categories()
        actual_main_links_text = self.get_text_from_all_main_categories_links()
        expected_main_links_text = AllNavLinks.MAIN_NAV_LINKS_TEXT
        for name_link in actual_main_links_text:
            assert name_link in expected_main_links_text,\
            f"Actual names of categories doesnt equal to expected names of categories. Incorrect name is {name_link}"

    def should_be_visible_all_main_category_links(self):
        assert self.are_visible(*AllNavLinks.MAIN_NAV_LINKS)

    def get_all_links_from_sub_categories(self):
        return self.browser.find_elements(*AllNavLinks.SUB_NAV_LINKS)

    def get_text_from_all_sub_categories_links(self):
        sub_links = self.get_all_links_from_sub_categories()
        return [link.text for link in sub_links]

    def should_be_right_names_of_sub_links(self):
        self.get_all_links_from_sub_categories()
        actual_sub_links_text = self.get_text_from_all_sub_categories_links()
        expected_sub_links_text = AllNavLinks.SUB_NAV_LINKS_TEXT
        for name_link in actual_sub_links_text:
            assert name_link in expected_sub_links_text,\
            f"Actual names of categories doesnt equal to expected names of categories. Incorrect name is {name_link}"

    def should_be_visible_all_sub_category_links(self):
        assert self.are_visible(*AllNavLinks.SUB_NAV_LINKS),\
        "Some links are not visible on page"

    def get_main_category_link_by_name(self, name):
        elements = self.get_all_links_from_main_categories()
        return self.get_element_by_text(elements, name)

    def go_to_all_main_categories(self):
        elements = self.get_all_links_from_main_categories()
        for element in elements:
            element.click()
            self.browser.back()

    def check_categories(self):
        category_labels_expected = CategoryLabels.CATEGORY_LABEL_TEXT
        for category_label_expected in category_labels_expected:
            category_label_actual = self.browser.find_element(*CategoryLabels.CATEGORY_LABEL).text
            assert category_label_actual == category_label_expected,\
                f"Expected {category_label_expected}, not {category_label_actual}"