from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons
from selenium.webdriver.common.action_chains import ActionChains


class PageClaimSummary():
    CLAIM_STATUS = ('ABIERTO', 'CERRADO')
    CLAIM_LOSS_CAUSE = ('Cristales', 'Robo de Ruedas', 'Accidente con daños a objetos', 'Accidente con Lesionados / Fallecidos', 'Daños al Vehículo asegurado y/o a otros vehículos', 'Solo daños al Vehículo asegurado', 'Daños multiples', 'Robo de partes del vehículo', 'Robo Total', 'Daños por Granizo', 'Destruccion Total', 'Incendio Parcial', 'Incendio total', 'Lesion, Muerte y Daños materiales', 'Lesiones y Daños materiales', 'Lesiones y muerte', 'Muerte', 'Robo Aparecido', 'Robo Recuperado', '')
    VEHICLE_LOSS_PARTY = ('Asegurado', 'Terceros')

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.actions = ActionChains(self.driver)
        self.claim_summary_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[2]/div/div[1]')
        self.claim_notes_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[2]/div/div[2]')
        self.claim_documents_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[2]/div/div[3]')
        self.claim_payments_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[2]/div/div[4]')
        self.claim_services_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[2]/div/div[5]')
        self.claim_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[1]/h1/ng-transclude/div')
        self.claim_status = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[1]/h1/ng-transclude/div/div[2]')
        self.claim_back_button = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[1]/h1/ng-transclude/div/gw-button/button')
        self.claim_loss_cause = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[1]/div/div[1]/h2')
        self.claim_date_of_loss_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[1]/div/div[1]/div[1]/lseg-icon-box/div/p/span[1]')
        self.claim_reported_by_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[1]/div/div[1]/div[2]/lseg-icon-box/div/p/span[1]')
        self.claim_loss_location_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[1]/div/div[2]/div[1]/lseg-icon-box/div/p/span[1]')
        self.claim_how_reported_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[1]/div/div[2]/div[2]/lseg-icon-box/div/p/span[1]')
        self.claim_references_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[2]/div/lseg-table-subsection/div/div')
        self.claim_references_policy_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[2]/div/lseg-table-subsection/div/ng-transclude/table/tbody/tr[1]/td[1]')
        self.claim_what_happened_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/section/div[2]/div/div[1]/div/div[4]/div/div[1]')
        self.claim_adjuster_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[1]/div/div/h1/ng-transclude/span[1]')
        self.claim_adjuster_no_exposures_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/div/span')
        self.claim_adjuster_table_first_item = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/table/tbody/tr')
        self.claim_adjuster_table_name_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/table/thead/tr/th[1]')
        self.claim_adjuster_table_segment_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/table/thead/tr/th[2]')
        self.claim_adjuster_table_incident_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/table/thead/tr/th[3]')
        self.claim_adjuster_table_state_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div[2]/table/thead/tr/th[4]')
        self.claim_involved_vehicles_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[1]/div[1]/div/div/h1/ng-transclude/span[1]')
        self.claim_involved_vehicles_table_make_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[1]/div')
        self.claim_involved_vehicles_table_model_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[2]/div')
        self.claim_involved_vehicles_table_year_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[3]/div')
        self.claim_involved_vehicles_table_license_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[4]/div')
        self.claim_involved_vehicles_table_loss_party_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[5]/div')
        self.claim_involved_vehicles_table_damage_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[6]/div')
        self.claim_involved_vehicles_table_damage_type_column = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/thead/tr/th[7]/div')
        self.claim_involved_vehicles_table_first_item = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/tbody/tr')
        self.claim_involved_vehicles_table_first_item_loss_party_value = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[3]/section/section/div/div/div[2]/div/div[1]/table/tbody/tr/td[5]')
        self.claim_parties_involved_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/div/div/div[3]/div[1]/div/div[6]/div/div/div[1]/div[1]/div/div/h1/ng-transclude/span[1]')
        self.claim_parties_involved_table_first_item = (By.XPATH, '//*[@id="partiesInvolved"]/tbody/tr[1]')
        self.claim_parties_involved_table_name_column = (By.XPATH, '//*[@id="partiesInvolved"]/thead/tr/th[1]/div')
        self.claim_parties_involved_table_involvement_column = (By.XPATH, '//*[@id="partiesInvolved"]/thead/tr/th[2]/div')
        self.claim_parties_involved_table_first_item_name_value = (By.XPATH, '//*[@id="partiesInvolved"]/tbody/tr[1]/td[1]/a')
        self.claim_party_involved_popup_close_button = (By.XPATH, '/html/body/div[3]/div/div[3]/gw-button')
        self.claim_party_involved_popup_name = (By.XPATH, '/html/body/div[3]/div/div[2]/div[1]')

    def go_to_claim(self, environment, claim_number):
        self.driver.get(environment + 'claims/' + claim_number)
        self.commons.check_gw_loader_not_visible()

    def return_claim_summary_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_summary_mosaic))
        return self.driver.find_element(*self.claim_summary_mosaic).text

    def return_claim_notes_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_notes_mosaic))
        return self.driver.find_element(*self.claim_notes_mosaic).text

    def return_claim_documents_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_documents_mosaic))
        return self.driver.find_element(*self.claim_documents_mosaic).text

    def return_claim_payments_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_payments_mosaic))
        return self.driver.find_element(*self.claim_payments_mosaic).text

    def return_claim_services_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_services_mosaic))
        return self.driver.find_element(*self.claim_services_mosaic).text

    def return_claim_title_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_title))
        return self.driver.find_element(*self.claim_title).text

    def return_claim_status_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_status))
        return self.driver.find_element(*self.claim_status).text

    def check_claim_back_button_exists(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.claim_back_button))

    def return_claim_loss_cause(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_loss_cause))
        return self.driver.find_element(*self.claim_loss_cause).text

    def return_claim_date_of_loss_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_date_of_loss_title))
        return self.driver.find_element(*self.claim_date_of_loss_title).text

    def return_claim_reported_by_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_reported_by_title))
        return self.driver.find_element(*self.claim_reported_by_title).text

    def return_claim_loss_location_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_loss_location_title))
        return self.driver.find_element(*self.claim_loss_location_title).text

    def return_claim_how_reported_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_how_reported_title))
        return self.driver.find_element(*self.claim_how_reported_title).text

    def return_claim_what_happened_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_what_happened_title))
        return self.driver.find_element(*self.claim_what_happened_title).text

    def return_claim_adjuster_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_adjuster_title))
        return self.driver.find_element(*self.claim_adjuster_title).text

    def return_claim_involved_vehicles_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_involved_vehicles_title))
        return self.driver.find_element(*self.claim_involved_vehicles_title).text

    def return_claim_parties_involved_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.claim_parties_involved_title))
        return self.driver.find_element(*self.claim_parties_involved_title).text

    def check_if_claim_has_exposures(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.claim_adjuster_title)).click()
        try:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.claim_adjuster_table_first_item))
            return True
        except:
            WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.claim_adjuster_no_exposures_label))
            return False

    def return_claim_adjuster_table_name_column_title(self):
        return self.driver.find_element(*self.claim_adjuster_table_name_column).text

    def return_claim_adjuster_table_segment_column_title(self):
        return self.driver.find_element(*self.claim_adjuster_table_segment_column).text

    def return_claim_adjuster_table_incident_column_title(self):
        return self.driver.find_element(*self.claim_adjuster_table_incident_column).text

    def return_claim_adjuster_table_state_column_title(self):
        return self.driver.find_element(*self.claim_adjuster_table_state_column).text

    def return_claim_adjuster_table_no_exposures_label_text(self):
        return self.driver.find_element(*self.claim_adjuster_no_exposures_label).text

    def verify_claim_has_involved_vehicles(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.claim_involved_vehicles_title)).click()
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.claim_involved_vehicles_table_first_item))

    def return_claim_involved_vehicles_table_make_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_make_column).text

    def return_claim_involved_vehicles_table_model_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_model_column).text

    def return_claim_involved_vehicles_table_year_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_year_column).text

    def return_claim_involved_vehicles_table_license_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_license_column).text

    def return_claim_involved_vehicles_table_loss_party_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_loss_party_column).text

    def return_claim_involved_vehicles_table_damage_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_damage_column).text

    def return_claim_involved_vehicles_table_damage_type_column_title(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_damage_type_column).text

    def return_claim_involved_vehicles_table_first_item_loss_party_text(self):
        return self.driver.find_element(*self.claim_involved_vehicles_table_first_item_loss_party_value).text

    def verify_claim_has_parties_involved(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.claim_parties_involved_title)).click()
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(self.claim_parties_involved_table_first_item))

    def return_claim_parties_involved_table_name_column_title(self):
        return self.driver.find_element(*self.claim_parties_involved_table_name_column).text

    def return_claim_parties_involved_table_first_item_name_value_text(self):
        return self.driver.find_element(*self.claim_parties_involved_table_first_item_name_value).text

    def return_claim_parties_involved_table_involvement_column_title(self):
        return self.driver.find_element(*self.claim_parties_involved_table_involvement_column).text

    def return_claim_first_party_involved_popup_name(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.claim_parties_involved_table_first_item_name_value)).click()
        name = self.driver.find_element(*self.claim_party_involved_popup_name).text
        self.actions.move_to_element(self.driver.find_element(*self.claim_party_involved_popup_close_button)).perform()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.claim_party_involved_popup_close_button)).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element(self.claim_party_involved_popup_close_button))
        return name