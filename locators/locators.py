from selenium.webdriver.common.by import By


class ZultysLocators:
    FAX_DRIVER_WIN_64 = (By.XPATH, '//a[contains(@href,"Zultys_Fax_2.2_x64.msi")]')
    FAX_DRIVER_WIN_32 = (By.XPATH, '//a[contains(@href,"Zultys_Fax_2.2_x86.msi")]')
    FAX_DRIVER_SERVER_32 = (By.XPATH, '//a[contains(@href,"Zultys_Fax_2.2_x86_Server.msi")]')
    FAX_DRIVER_SERVER_64 = (By.XPATH, '//a[contains(@href,"Zultys_Fax_2.2_x64_Server.msi")]')

    PLATRINICS_SDK_LITE = (By.XPATH, '//a[contains(@href,"bt_plantronicsplugin.msi")]')
    MX_ARCHIVE = (By.XPATH, '//a[contains(@href,"mxdataarch_setup.exe")]')
    MX_ARCHIVE_VIEWER = (By.XPATH, '//a[contains(@href,"arcaccess_setup.exe")]')
    ADMINISTRATION_UI = (By.XPATH, '//a[contains(@href,"admin_setup.exe")]')



