import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.parametrize("name, test_case", [("desktop-impact-items-F7T6E", 'first'),
                                             ("desktop-impact-items-F7T6E", 'second'),
                                             ("desktop-impact-items-F7T6E", 'third')])
def test_counters_screenshot(name, test_case):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        counter_element = page.locator(f".{name}")
        counter_element.screenshot(path=f"output/{name}_{test_case}.png")
        browser.close()
