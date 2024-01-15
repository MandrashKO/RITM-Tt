from libs.pages.mainPage import MainPage
from libs.pages.elementsPage import ElementsPage
from libs.pages.checkboxPage import CheckboxPage


def pytest_generate_tests(metafunc):
    site = 'https://demoqa.com'
    metafunc.parametrize("site",[site])
    metafunc.parametrize("setup_driver", [{'browser': 'Chrome'}, {'browser': 'Firefox'}], indirect=True)


def test_ui(setup_driver, site):
    page = MainPage(setup_driver)
    page.getPage(site)
    assert "https://demoqa.com" in page.current_url()
    page.go2elements()
    assert "elements" in page.current_url()
    page = ElementsPage(setup_driver)
    page.go2checkbox()
    assert "checkbox" in page.current_url()
    page = CheckboxPage(setup_driver)
    page.find_catalogZone()
    confirmation = page.openHomeList()
    assert confirmation, "Не открылся список Home"
    confirmation = page.openDownloadList()
    assert confirmation, "Не открылся список Downloads"
    page.selectFile()
    confirmation = page.Test()
    assert confirmation, "Чекбокс файла Word File.doc не выбран. Не появилось сообщение 'You have selected:wordFile'"

