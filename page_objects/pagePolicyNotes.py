from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from commons.Commons import Commons
import time

class PagePolicyNotes():
    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.notes_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[3]')
        self.notes_mosaico_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[3]/div[3]')
        self.add_note_button = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[1]/div/div/gw-button/button/ng-transclude')
        self.select_note_tema = (By.ID, 'Topic')
        self.add_note_asunto = (By.XPATH, '/html/body/div/div/div/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[3]/ng-form/div/div/gw-pl-input-ctrl/div/div/div/input')
        self.add_note_body = (By.ID, 'note-body')
        self.add_note_agregar_button = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[3]/ng-form/div/div/div[3]/gw-button[2]/button/ng-transclude')
        self.note_asunto = (By.CSS_SELECTOR, "div[class='gw-subject ng-binding']")
        self.note_body = (By.CSS_SELECTOR, "div[class='gw-description ng-binding']")
        self.note_tema = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[4]/div/div/div[2]/div[2]/div/div/ng-transclude')
        self.add_note_information_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[2]/label')
        self.no_note_information_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[3]/span')
        self.search_note_box = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[1]/div/div/span/span/input')



    def go_to_notes(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.notes_mosaico)).click()

    def return_add_note_button_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.add_note_button))
        return self.driver.find_element(*self.add_note_button).text

    def return_note_information_label_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.add_note_information_label))
        return self.driver.find_element(*self.add_note_information_label).text

    def return_no_note_information_label_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.no_note_information_label))
        return self.driver.find_element(*self.no_note_information_label).text

    def return_number_of_notes(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.notes_mosaico_number))
        return self.driver.find_element(*self.notes_mosaico_number).text

    def check_visibility_of_search_notes(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.search_note_box))

    def add_note(self, Tema, Asunto, Body):
        self.commons.check_gw_loader_not_visible()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_note_button)).click()
        tema = Select(self.driver.find_element(*self.select_note_tema))
        tema.select_by_visible_text(Tema)
        self.driver.find_element(*self.add_note_asunto).send_keys(Asunto)
        self.driver.find_element(*self.add_note_body).send_keys(Body)
        self.driver.find_element(*self.add_note_agregar_button).click()

    def return_note_asunto(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.gw_loader))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.note_asunto))
        return self.driver.find_elements(*self.note_asunto)[0].text

    def return_note_body(self):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.gw_loader))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.note_body))
        return self.driver.find_elements(*self.note_body)[0].text

    def return_note_tema(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.gw_loader))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.note_tema))
        return self.driver.find_element(*self.note_tema).text



