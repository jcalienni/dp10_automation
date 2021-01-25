from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commons.Commons import Commons
import time

class PagePolicyContacts():

    def __init__(self, my_driver):
        self.driver = my_driver
        self.common = Commons(self.driver)
        self.contactos_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[2]')
        self.contactos_poliza_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/ul/li[1]/a/tab-heading/div')
        self.contactos_poliza_tab_text = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/ui-view/gw-policy-contacts-summary-table/div[1]/div[1]')
        self.contactos_cuenta_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/ul/li[2]/a/tab-heading/div')
        self.contactos_cuenta_tab_text = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/ui-view/gw-account-contacts/div[1]/div[1]')
        self.contactos_asociados_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/ul/li[3]/a/tab-heading/div')
        self.contactos_asociados_text = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/ui-view/gw-related-account-contacts/div[1]/div[1]')




    def go_to_contactos(self):
        self.common.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.contactos_mosaico)).click()

    def return_contact_policy_tab_title(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.contactos_poliza_tab, 'Contactos'))
        return self.driver.find_element(*self.contactos_poliza_tab).text

    def return_contact_policy_tab_text(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.contactos_poliza_tab_text, 'contactos'))
        return self.driver.find_element(*self.contactos_poliza_tab_text).text

    def return_contact_account_tab_title(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.contactos_cuenta_tab, 'Contactos'))
        return self.driver.find_element(*self.contactos_cuenta_tab).text

    def return_contact_account_tab_text(self):
        self.driver.find_element(*self.contactos_cuenta_tab).click()
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.contactos_cuenta_tab_text, 'contactos'))
        return self.driver.find_element(*self.contactos_cuenta_tab_text).text

    def return_asociated_contact_title(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.contactos_asociados_tab, 'Contactos'))
        return self.driver.find_element(*self.contactos_asociados_tab).text

    def return_asociated_contact_tab_text(self):
        self.driver.find_element(*self.contactos_asociados_tab).click()
        # WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.contactos_asociados_tab)).click()
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.contactos_asociados_text, 'contactos'))
        return self.driver.find_element(*self.contactos_asociados_text).text
