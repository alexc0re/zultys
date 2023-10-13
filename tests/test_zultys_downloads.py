from locators.locators import ZultysLocators


def test_download_win_32_bit(home_page):
    home_page.main_page_download(ZultysLocators.FAX_DRIVER_WIN_32)


def test_download_win_64_bit(home_page):
    home_page.main_page_download(ZultysLocators.FAX_DRIVER_WIN_64)


def test_download_server_32_bit(home_page):
    home_page.main_page_download(ZultysLocators.FAX_DRIVER_SERVER_32)


def test_download_server_64_bit(home_page):
    home_page.main_page_download(ZultysLocators.FAX_DRIVER_SERVER_64)


def test_download_platinics_sdk_lite(home_page):
    home_page.main_page_download(ZultysLocators.PLATRINICS_SDK_LITE)


def test_download_mx_archive(home_page):
    home_page.main_page_download(ZultysLocators.MX_ARCHIVE)


def test_download_mx_archive_viewer(home_page):
    home_page.main_page_download(ZultysLocators.MX_ARCHIVE_VIEWER)


def test_download_administration_ui(home_page):
    home_page.main_page_download(ZultysLocators.ADMINISTRATION_UI)


