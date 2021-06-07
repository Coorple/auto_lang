import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_btn_diff_lang(browser):
    browser.get(link)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) == 1
    time.sleep(5)
