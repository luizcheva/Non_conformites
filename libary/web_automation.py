# flake8: noqa
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from datetime import datetime
from libary.requests_excel import BuscarDescricao


class WebAutomator:
    def __init__(self, senha_sesuite: str = ''):
        self.service = Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=self.service)
        self.login = os.getlogin()
        self.senha = senha_sesuite

    def wait_for_browser_close(self):
        while True:
            try:
                self.driver.title
            except Exception:
                self.driver.quit()
                break

    def open_sro(self, planta: int, item: str, lote: str, ordem: int | float, qtde: int, qtde_rep: int, obs: str, motivo_nc: str):
        buscar = BuscarDescricao()
        descricao = buscar.buscarItem(item)

        descricao_completa = motivo_nc + ' (Item: ' + item + ' - ' + descricao + ')'
    
        self.driver.maximize_window()
        self.driver.get('https://softexpert.straumann.com/softexpert/login')
        locator = (By.ID, "user")
        WebDriverWait(self.driver, 10).\
            until(EC.presence_of_element_located(locator))
        self.driver.find_element(By.XPATH, "//*[@id='user']").send_keys(
            self.login
        )
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(
            self.senha
        )
        self.driver.find_element(By.XPATH, "//*[@id='loginButton']").click()

        try:
            WebDriverWait(self.driver, 10).\
                until(EC.presence_of_element_located((By.ID, "alertConfirm")))
        except TimeoutException:
            pass

        is_log = self.driver.find_elements(By.ID, "alertConfirm")

        if len(is_log) > 0:
            self.driver.find_element(By.ID, "alertConfirm").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.ID, "dashboardTitle")
        ))

        self.driver.get(
            'https://softexpert.straumann.com/softexpert/workspace?page=8,202'
        )

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".sgProcCard")
        ))
        modulos = self.driver.find_elements(By.CSS_SELECTOR, ".sgProcCard")
        for opt in modulos:
            descricao = opt.text
            if 'S.RO' in descricao:
                WebDriverWait(self.driver, 2)
                opt.click()
                opt.find_element(By.TAG_NAME, "textarea").send_keys(descricao_completa)
                btns = opt.find_elements(By.TAG_NAME, "button")
                for btn in btns:
                    if 'Iniciar' in btn.accessible_name:
                        btn.click()
                        break
                break

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        frames = self.driver.find_elements(By.TAG_NAME, 'iframe')
        for frame in frames:
            print(frame)

        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
        self.driver.switch_to.frame(0)
        self.driver.switch_to.frame(3)

        WebDriverWait(self.driver, 10).\
                until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/form/div/div[1]/div/div/div/div[2]/div[1]/div/input")))

        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[1]/div/div/div/div[2]/div[1]/div/input").send_keys(planta)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[1]/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[1]/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "/html/body/div/div/form/div/div[2]/div/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "/html/body/div/div/form/div/div[7]/div/div[2]/div/div/div/textarea").send_keys(item)
        self.driver.find_element(By.XPATH, "//*[@id='value_1327']").send_keys(lote)
        self.driver.find_element(By.XPATH, "//*[@id='value_1328']").send_keys(ordem)
        self.driver.find_element(By.XPATH, "//*[@id='value_1329']").send_keys(qtde)
        self.driver.find_element(By.XPATH, "//*[@id='value_1330']").send_keys(qtde_rep)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[12]/div/div/div/div[2]/div[1]/div/input").send_keys('Peças')
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[12]/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[12]/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.TAB)
        data = datetime.now()
        data = data.strftime("%d%m%Y")
        self.driver.find_element(By.XPATH, "/html/body/div/div/form/div/div[13]/div/div[2]/div/div/input").send_keys(data)
        self.driver.find_element(By.XPATH, "//*[@id='value_1331']").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[14]/div/div/div/div[2]/div[1]/div/input").send_keys('Controle de Qualidade')
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[14]/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/div[14]/div/div/div/div[2]/div[1]/div/input").send_keys(Keys.TAB)
        self.driver.find_element(By.XPATH, "/html/body/div/div/form/div/div[15]/div/div[2]/div/div/div/textarea").send_keys('N/A')
        self.driver.find_element(By.XPATH, "/html/body/div/div/form/div/div[16]/div/div[2]/div/div/div/textarea").send_keys(obs)


if __name__ == '__main__':
    auto = WebAutomator()
    auto.open_sro()

    auto.wait_for_browser_close()
