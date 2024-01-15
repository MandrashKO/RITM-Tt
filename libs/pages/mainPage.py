from libs.pages.page import Page

class Main:
    elemButton = None

    _elemButton_ = '//div[@class="card mt-4 top-card" and contains(.,"Elements")]'

class MainPage(Page):

    def go2elements(self):
        self.main = Main()
        self.main.elemButton = self.findElement(xpath=self.main._elemButton_)
        self.main.elemButton.click()

