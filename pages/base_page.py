class BasePage:

    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def fill_input_data(self, loc, text_data):
        self.page.locator(loc).fill(text_data)

    def clear_input_data(self, loc):
        self.page.locator(loc).clear()

        # # TODO: check if next line will work
        # self.page.clear(loc)

    def click_on_elem(self, loc):
        self.page.click(loc)

    def get_text(self, loc):
        text = self.page.locator(loc).text_content()
        return text

    def get_all_text(self, loc):
        text = self.page.locator(loc).all_text_contents()
        return text