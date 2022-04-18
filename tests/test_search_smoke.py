import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize('req, expected_result',
                         [('helmii', 'Helmii'),('silky', 'Silky Skin'),
                          ('skin', 'Silky Skin')
                          ])
def test_search(web_browser, req, expected_result):

    """Test search field"""

    page = MainPage(web_browser)

    page.search_field.wait_to_be_clickable()

    page.search_field.click()

    page.search_field.send_keys(req)

    assert page.menu.get_text() == expected_result
