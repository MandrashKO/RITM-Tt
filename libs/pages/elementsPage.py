from libs.pages.page import Page

class Elements:
    elemlistButtons = None
    checkboxButton = None

    _elemlistButtons_ = '//ul[@class="menu-list"]'
    _checkboxButton_ = {'id': ['item-1']}

class ElementsPage(Page):

    def go2checkbox(self):
        self.elements = Elements()
        self.elements.elemlistButtons = self.findElements(xpath=f"{self.elements._elemlistButtons_}//*")
        self.elements.checkboxButton = self.selectElement(self.elements.elemlistButtons,self.elements._checkboxButton_)
        self.elements.checkboxButton.click()
