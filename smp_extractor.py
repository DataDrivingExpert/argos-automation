import re
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("SMP_USER") or None
PASSWORD = os.getenv("SMP_PWD") or None
DOWNLOAD_PATH = "./documents/"

assert USER is not None and PASSWORD is not None, "Faltan las variables de entorno"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://smp.uautonoma.cl/auth/login")
    page.get_by_role("button", name="Iniciar Sesión Universidad").click()
    page.get_by_role("textbox", name="Escriba su correo electrónico").click()
    page.get_by_role("textbox", name="Escriba su correo electrónico").fill(USER)
    page.get_by_role("button", name="Siguiente").click()
    page.get_by_role("textbox", name="Escriba la contraseña para").click()
    page.get_by_role("textbox", name="Escriba la contraseña para").fill(PASSWORD)
    page.get_by_role("button", name="Iniciar sesión").click()
    page.get_by_role("button", name="No").click()
    page.locator("a").nth(1).click()
    page.get_by_role("menuitem", name=" REPORTERÍA").click()
    page.get_by_role("menuitem", name="Matricula Total").click()
    page.get_by_role("button", name="(*)Seleccione Período").click()
    page.get_by_role("option", name="- BLOQUE 01 - 2025").click()
    page.get_by_role("button", name="Seleccione Sede").click()
    page.get_by_role("option", name="CAMPUS VIRTUAL").click()
    page.get_by_role("button", name="Seleccione Nivel").click()
    page.get_by_role("option", name="FORMACIÓN CONTINUA").click()
    page.get_by_role("button", name="Seleccione Estatus Plan").click()
    page.get_by_role("option", name="ACTIVO").click()
    page.get_by_role("button", name="Seleccione Carrera").click()
    # PROGRAMA DI194_413
    page.get_by_role("option", name="I194 - DIP EN BIG DATA AND").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI194_413 - DIP EN BIG DATA").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download = download_info.value
    download.save_as(DOWNLOAD_PATH + "DI194_413.xlsx")
    page.get_by_role("button", name="Seleccione Carrera").click()
    # Programa 172_413
    page.get_by_role("option", name="I172 - DIP EN CIBERSEG Y").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI172_413 - DIP EN CIBERSEG Y").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download1_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download1 = download1_info.value
    download1.save_as(DOWNLOAD_PATH + "DI172_413.xlsx")
    page.get_by_role("button", name="Seleccione Carrera").click()
    # Programa DI143_413
    page.get_by_role("option", name="I143 - DIP EN GESTIÓN Y").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI143_413 - DIP EN GESTIÓN Y").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download2_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download2 = download2_info.value
    download2.save_as(DOWNLOAD_PATH + "DI143_413.xlsx")
    page.get_by_role("button", name="Seleccione Carrera").click()
    # PROGRAMA 025_413
    page.get_by_role("option", name="I025 - DIP EN GESTIÓN DE CONV").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI025_413 - DIP EN GESTIÓN DE").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download3_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download3 = download3_info.value
    download3.save_as(DOWNLOAD_PATH + "DI025_413.xlsx")
    # Programa 107_413
    page.get_by_role("button", name="Seleccione Carrera").click()
    page.get_by_role("option", name="I107 - DIP EN COMPETENCIAS").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI107_413 - DIP EN").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download4_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download4 = download4_info.value
    download4.save_as(DOWNLOAD_PATH + "DI107_413.xlsx")
    # Programa 151_413
    page.get_by_role("button", name="Seleccione Carrera").click()
    page.get_by_role("option", name="I151 - DIP EN EV. AUTENT Y").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI151_413 - DIP EN EV. AUTENT").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download5_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download5 = download5_info.value
    download5.save_as(DOWNLOAD_PATH + "DI151_413.xlsx")
    # Programa 142_413
    page.get_by_role("button", name="Seleccione Carrera").click()
    page.get_by_role("option", name="I142 - DIP FOM Y MED LECTORA").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI142_413 - DIP FOM Y MED").click()
    page.get_by_text("CAMPUS VIRTUALCAMPUS VIRTUALFORMACIÓN CONTINUAFORMACIÓN CONTINUAI142 - DIP FOM").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download6_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download6 = download6_info.value
    download6.save_as(DOWNLOAD_PATH + "DI142_413.xlsx")
    # Programa 142_413
    page.get_by_role("button", name="Seleccione Carrera").click()
    page.get_by_role("option", name="I166 - DIP EN INNOV EN LA").click()
    page.get_by_role("button", name="Seleccione Programa").click()
    page.get_by_role("option", name="DI166_413 - DIP EN INNOV EN").click()
    page.get_by_role("button", name="Aplicar").click()
    with page.expect_download() as download7_info:
        page.get_by_role("button", name="Exportar Excel").click()
    download7 = download7_info.value
    download7.save_as(DOWNLOAD_PATH + "DI166_413.xlsx")
    page.locator("#salir-tooltip").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
