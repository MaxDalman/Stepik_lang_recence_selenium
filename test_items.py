import pytest
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_basket_language(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button_basket = browser.find_element_by_css_selector("#add_to_basket_form [type='submit']")
    assert button_basket, 'doesnt have btn.'