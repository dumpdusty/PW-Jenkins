from playwright.sync_api import sync_playwright, expect

class Assertions:


    def verify_page_title(self,page, title):
        expect(page).to_have_title(title)

    def verify_text(self, page, loc, text):
        expect(page.locator(loc)).to_have_text(text)

    def verify_element_visible(self, page, loc):
        expect(page.locator(loc)).to_be_visible()    