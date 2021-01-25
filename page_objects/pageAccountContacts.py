from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons


class PageAccountContacts():

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.account_contacts_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[2]/div[2]')
        self.account_contacts_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/ul/li[1]/a/tab-heading/div')
        self.account_contacts_tab_text = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/ui-view/gw-account-contacts/div[1]/div[1]')
        self.account_associated_contacts_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/ul/li[2]/a/tab-heading/div')
        self.account_associated_contacts_tab_text = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/ui-view/gw-related-account-contacts/div[1]/div[1]')

    def go_to_account_contacts(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_contacts_mosaic)).click()

    def return_account_contacts_tab_title(self):
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(self.account_contacts_tab, 'Contactos de cuenta'))
        return self.driver.find_element(*self.account_contacts_tab).text

    def return_account_contacts_tab_text(self):
        self.driver.find_element(*self.account_contacts_tab).click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(self.account_contacts_tab_text, 'Solo'))
        return self.driver.find_element(*self.account_contacts_tab_text).text

    def return_account_associated_contacts_tab_title(self):
        return self.driver.find_element(*self.account_associated_contacts_tab).text

    def return_account_associated_contacts_tab_text(self):
        self.driver.find_element(*self.account_associated_contacts_tab).click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(self.account_associated_contacts_tab_text, 'algún tipo'))
        return self.driver.find_element(*self.account_associated_contacts_tab_text).text


