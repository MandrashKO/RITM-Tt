from libs.pages.page import Page

class Checkbox:
    catalogZone = None
    hometoggleButton = None
    homelistisOpen = None
    downloadlistisOpen = None
    downloadstoggleButton = None
    wordFile = None
    checkboxwordfile = None
    text_result = None

    _catalogZone_ = "//div[@class='col-12 mt-4 col-md-6']"
    _hometoggleButton_ = "//button[@class='rct-collapse rct-collapse-btn']/parent::*[contains(.,'Home')]//button"
    _downloadstoggleButton_ = "//button[@class='rct-collapse rct-collapse-btn']/parent::*[contains(.,'Downloads')]//button"
    _listisOpen_ = "//..//parent::li[contains(@class, 'expanded')]"
    _wordFile_ = "//label[@for='tree-node-wordFile']"
    _checkboxwordfile_ = {"class": ["rct-icon rct-icon-check"]}
    _result_ = {"id": ["result"]}
    confirm = ["you", "have", "selected",":", "wordfile"]


class CheckboxPage(Page):

    def find_catalogZone(self):
        self.checkbox = Checkbox()
        self.checkbox.catalogZone = self.findElement(xpath=self.checkbox._catalogZone_)


    def openHomeList(self):
        self.checkbox.hometoggleButton = self.findElement(xpath=self.checkbox._hometoggleButton_,element=self.checkbox.catalogZone)
        self.click(elem=self.checkbox.hometoggleButton)
        try:
            self.checkbox.homelistisOpen = self.findElement(xpath=self.checkbox._listisOpen_, element=self.checkbox.hometoggleButton)
        except Exception as e:
            raise f"Не удалось открыть список Home: {e}"
        if self.checkbox.homelistisOpen is not None:
            return True
    def openDownloadList(self):
        self.checkbox.downloadstoggleButton = self.findElement(xpath=self.checkbox._downloadstoggleButton_,element=self.checkbox.catalogZone)
        self.click(elem=self.checkbox.downloadstoggleButton)
        try:
            self.checkbox.downloadlistisOpen = self.findElement(xpath=self.checkbox._listisOpen_, element=self.checkbox.downloadstoggleButton)
        except Exception as e:
            raise f"Не удалось открыть список Downloads: {e}"
        if self.checkbox.homelistisOpen is not None:
            return True

    def selectFile(self):
        self.checkbox.wordFile = self.findElement(xpath=self.checkbox._wordFile_,element=self.checkbox.downloadlistisOpen)
        self.click(elem=self.checkbox.wordFile)


    def confirmationEvaluation(self):
        args = self.findElements(xpath="//*", element=self.checkbox.wordFile)
        try:
            self.checkbox.checkboxwordfile = self.selectElement(args, self.checkbox._checkboxwordfile_)
        except:
            pass
        args_result = self.findElements(xpath="//*", element=self.checkbox.catalogZone)
        try:
            self.checkbox.result = self.selectElement(args_result, self.checkbox._result_)
            self.checkbox.text_result = self.text(self.checkbox.result).split()
        except:
            pass
        if self.checkbox.checkboxwordfile is not None and all([txt.lower() in self.checkbox.confirm for txt in self.checkbox.text_result]):
            return True

    def Test(self):
        return self.confirmationEvaluation()
