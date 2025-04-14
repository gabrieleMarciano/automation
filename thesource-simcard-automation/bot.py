
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class SimcardBot:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.navegador, 30)

    def login(self):
        self.navegador.get('https://thesource.vizada.com')
        self.wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(self.email)
        self.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(self.senha)
        self.wait.until(EC.element_to_be_clickable((By.NAME, "_finish"))).click()

    def processar_simcard(self, simcard, designacao):
        try:
            nav = self.navegador
            wait = self.wait

            nav.get('https://thesource.vizada.com')
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/thesource/portal/portfolio.ts']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/thesource/inmarsat/m2m/summary.ts']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/table[1]/tbody/tr[3]/th/a'))).click()

            campo_busca = wait.until(EC.presence_of_element_located((By.NAME, "iccId")))
            campo_busca.clear()
            campo_busca.send_keys(simcard)
            campo_busca.send_keys(Keys.RETURN)

            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/form/table[3]/tbody/tr/td[5]/a'))).click()

            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="billData.invoiceReference"]'))).send_keys("CELPA")
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="billData.comments"]'))).send_keys("gmarciano")
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/form/input[1]'))).click()

            Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="companyId"]')))).select_by_index(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/form/input[2]'))).click()

            Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="packageTypeId"]')))).select_by_index(1)
            Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="marketSectorId"]')))).select_by_index(15)
            Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="package.homeCountry"]')))).select_by_index(34)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/form/input[2]'))).click()

            campo_tag = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="package.tag"]')))
            campo_tag.clear()
            campo_tag.send_keys(designacao)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/form/input[2]'))).click()

            Select(wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gprsService.qualityOfService"]')))).select_by_index(0)
            checkbox = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainarea"]/table/tbody/tr/td[2]/form/table/tbody/tr/td/table[2]/tbody/tr[7]/td[2]/input')))
            if not checkbox.is_selected():
                checkbox.click()

            wait.until(EC.element_to_be_clickable((By.NAME, "_finish"))).click()

        except Exception as e:
            print(f"Erro ao processar o SIMCARD {simcard}: {e}")

    def fechar(self):
        self.navegador.quit()
