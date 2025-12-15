import re
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
from os import getenv

load_dotenv()
USER = getenv('ARG_USER')
PASSWORD = getenv('ARG_PWD')

def run(playwright: Playwright) -> None:
    DOWNLOAD_PATH = './documents/'
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Acceso
    page.goto("https://maps.uautonoma.cl/Argos/AWV/#shortcut/private//datablock/Admisi%C3%B3n%20USAR")
    page.locator("#loginUsername").click()
    page.locator("#loginUsername").press("CapsLock")
    page.locator("#loginUsername").fill(USER)
    page.locator("#loginPassword").click()
    page.locator("#loginPassword").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    # Filtrado
    page.locator("#fo-DD_P_Academico").get_by_role("combobox").select_option("22")
    page.locator("#fo-DD_vers_program").get_by_role("combobox").select_option("8") # Versión 004
    page.locator("#fo-DD_Sede").get_by_role("combobox").select_option("1")
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("157")
    page.get_by_role("checkbox", name="Todas las fechas").check()
    page.get_by_text("Ver reporte").click()
    # Primer export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").uncheck()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Apply").click()
    download = download_info.value
    download.save_as(DOWNLOAD_PATH + 'DI172_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("179")
    page.locator("#fo-DD_vers_program").get_by_role("combobox").select_option("6") # Versión 002
    page.get_by_text("Ver reporte").click()
    # Segundo export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("listitem").nth(2).click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").click()
    with page.expect_download() as download1_info:
        page.get_by_role("button", name="Apply").click()
    download1 = download1_info.value
    download1.save_as(DOWNLOAD_PATH + 'DI194_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("128")
    page.locator("#fo-DD_vers_program").get_by_role("combobox").select_option("5") # Volver a versión 001
    page.locator(".form-element-btn").click()
    # Tercer export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").uncheck()
    with page.expect_download() as download2_info:
        page.get_by_role("button", name="Apply").click()
    download2 = download2_info.value
    download2.save_as(DOWNLOAD_PATH + 'DI143_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("53")
    page.locator(".form-element-btn").click()
    # Cuarto export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").click()
    with page.expect_download() as download3_info:
        page.get_by_role("button", name="Apply").click()
    download3 = download3_info.value
    download3.save_as(DOWNLOAD_PATH + 'DI025_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").click()
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("92")
    page.locator(".form-element-btn").click()
    # Quinto export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").uncheck()
    with page.expect_download() as download4_info:
        page.get_by_role("button", name="Apply").click()
    download4 = download4_info.value
    download4.save_as(DOWNLOAD_PATH + 'DI107_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("136")
    page.get_by_text("Ver reporte").click()
    # Sexto export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").uncheck()
    with page.expect_download() as download5_info:
        page.get_by_role("button", name="Apply").click()
    download5 = download5_info.value
    download5.save_as(DOWNLOAD_PATH + 'DI151_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("127")
    page.get_by_text("Ver reporte").click()
    # Séptimo export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("listitem").nth(2).click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").uncheck()
    with page.expect_download() as download6_info:
        page.get_by_role("button", name="Apply").click()
    download6 = download6_info.value
    download6.save_as(DOWNLOAD_PATH + 'DI142_413.csv')
    # Cambio de programa
    page.locator("#fo-DD_Programa").get_by_role("combobox").select_option("151")
    page.get_by_text("Ver reporte").click()
    # Octavo export
    page.locator(".cogBtn").click()
    page.get_by_text("Export All to CSV").click()
    page.get_by_role("checkbox", name="ID_BANNER").check()
    page.get_by_role("checkbox", name="RUT").uncheck()
    with page.expect_download() as download7_info:
        page.get_by_role("button", name="Apply").click()
    download7 = download7_info.value
    download7.save_as(DOWNLOAD_PATH + 'DI166_413.csv')
    page.get_by_text("Sign Out").click()
    page.get_by_role("button", name="Yes").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
