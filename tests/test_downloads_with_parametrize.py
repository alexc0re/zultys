from locators.locators import ZultysLocators
import pytest

files = [ZultysLocators.FAX_DRIVER_WIN_32, ZultysLocators.FAX_DRIVER_WIN_64, ZultysLocators.FAX_DRIVER_SERVER_32,
         ZultysLocators.FAX_DRIVER_SERVER_64, ZultysLocators.PLATRINICS_SDK_LITE, ZultysLocators.MX_ARCHIVE,
         ZultysLocators.MX_ARCHIVE_VIEWER, ZultysLocators.ADMINISTRATION_UI]

ids = ['win_32_bit', 'win_64_bit', 'server_32_bit', 'server_64_bit', 'platinics_sdk_lite', 'mx_archive',
       'mx_archive_viewer', 'administration_ui']


@pytest.mark.parametrize('file', files, ids=ids)
def test_download(home_page, file):
    home_page.main_page_download(file)

