import time

from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://tabby.ai'
        super().__init__(web_driver, url)

    search_field = WebElement(css_selector='input.w-full')

    menu = WebElement(css_selector='.text-text-light')

