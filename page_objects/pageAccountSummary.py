from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons


class PageAccountSummary():
    OFFICIAL_ID_TYPE = ('DNI', 'LE', 'LC', 'Pasaporte')
    FISCAL_ID_TYPE = ('CUIT', 'CUIL')
    ACCOUNT_STATUS = ('ACTIVA', 'PENDIENTE')
    POLICY_TYPE = ('Individual', 'Colectivo', 'Registro de Conductores', 'Automotores', 'Motovehículos', 'Obligaciones Laborales', 'Seguros Opcionales', 'Decreto 1567/74')

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.account_summary_mosaic = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[1]/div[2]')
        self.account_contacts_mosaic = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[2]/div[2]')
        self.account_open_quotes_mosaic = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[3]/div[2]')
        self.account_open_transactions_mosaic = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[4]/div[2]')
        self.account_claims_mosaic = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[5]/div[2]')
        self.account_billing_mosaic = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[6]/div[2]')
        self.account_summary_edit_link = (By.CSS_SELECTOR, "a.lseg-account-summary-edit-link.ng-binding.ng-scope")
        self.account_summary_edit_form_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/ng-form/div/div[1]/h2/ng-transclude')
        self.account_summary_edit_form_cancel_button = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/ng-form/div/div[3]/gw-button[1]/button')
        self.account_summary_edit_form_save_button = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/ng-form/div/div[3]/gw-button[2]/button')
        self.account_summary_personal_data = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[1]/lseg-table-subsection/div/div/div/div[1]')
        self.account_summary_personal_data_company_name = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[1]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[1]/td[1]')
        self.account_summary_personal_data_official_id_type_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[1]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[1]/td[1]')
        self.account_summary_personal_data_fiscal_id_type_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[1]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[2]/td[1]')
        self.account_summary_open_transactions_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[2]/lseg-table-subsection/div/div/div/div[1]')
        self.account_summary_open_transactions_quotes_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[2]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[1]/td[1]')
        self.account_summary_open_transactions_changes_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[2]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[2]/td[1]')
        self.account_summary_open_transactions_cancellations_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[2]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[3]/td[1]')
        self.account_summary_open_transactions_renewals_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[2]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[4]/td[1]')
        self.account_summary_involved_agencies_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[3]/lseg-table-subsection[1]/div/div/div/div[1]')
        self.account_summary_involved_agencies_items = (By.CLASS_NAME, "lseg-account-summary-agency.ng-binding")
        self.account_summary_status = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[3]/lseg-table-subsection[2]/div/div/div/div[1]')
        self.account_summary_status_value = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div[3]/lseg-table-subsection[2]/div/ng-transclude/table/tbody/tr/td')
        self.account_summary_issued_policies_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[1]/h2')
        self.account_summary_issued_policies_table_product_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[1]/div')
        self.account_summary_issued_policies_table_policy_type_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[2]/div')
        self.account_summary_issued_policies_table_status_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[3]/div')
        self.account_summary_issued_policies_table_policy_number_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[4]/div')
        self.account_summary_issued_policies_table_insured_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[6]/div')
        self.account_summary_issued_policies_table_effective_date_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[8]/div')
        self.account_summary_issued_policies_table_expiration_date_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/thead/tr/th[9]/div')
        self.account_summary_issued_policies_table_first_policy = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/tbody/tr[1]')
        self.account_summary_issued_policies_table_no_policies_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/div/span[1]')
        self.account_summary_issued_policies_table_first_policy_type = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]')
        self.account_summary_issued_policies_table_list = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div[2]/div/table/tbody/tr/td[3]')

    def go_to_account(self, environment, account_number):
        self.driver.get(environment + 'accounts/' + account_number + '/summary')
        self.commons.check_gw_loader_not_visible()

    def return_account_summary_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_mosaic))
        return self.driver.find_element(*self.account_summary_mosaic).text

    def return_account_contacts_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_contacts_mosaic))
        return self.driver.find_element(*self.account_contacts_mosaic).text

    def return_account_open_quotes_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_quotes_mosaic))
        return self.driver.find_element(*self.account_open_quotes_mosaic).text

    def return_account_open_transactions_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_transactions_mosaic))
        return self.driver.find_element(*self.account_open_transactions_mosaic).text

    def return_account_claims_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_claims_mosaic))
        return self.driver.find_element(*self.account_claims_mosaic).text

    def return_account_billing_mosaic_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_mosaic))
        return self.driver.find_element(*self.account_billing_mosaic).text

    def click_edit_account_link(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_edit_link))
        self.driver.find_element(*self.account_summary_edit_link).click()

    def return_edit_account_title_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_edit_form_title))
        return self.driver.find_element(*self.account_summary_edit_form_title).text

    def click_cancel_edit_form_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_edit_form_cancel_button))
        self.driver.find_element(*self.account_summary_edit_form_cancel_button).click()

    def click_save_edit_form_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_edit_form_save_button))
        self.driver.find_element(*self.account_summary_edit_form_cancel_button).click()

    def check_edit_form_closed(self):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.account_summary_edit_form_title))
        return True

    def return_account_personal_data_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_personal_data))
        return self.driver.find_element(*self.account_summary_personal_data).text

    def return_account_personal_data_official_id_type_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_personal_data_official_id_type_title))
        return self.driver.find_element(*self.account_summary_personal_data_official_id_type_title).text

    def return_account_personal_data_fiscal_id_type_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_personal_data_fiscal_id_type_title))
        return self.driver.find_element(*self.account_summary_personal_data_fiscal_id_type_title).text

    def return_account_personal_data_company_name_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_personal_data_company_name))
        return self.driver.find_element(*self.account_summary_personal_data_company_name).text

    def return_account_summary_open_transactions_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_open_transactions_title))
        return self.driver.find_element(*self.account_summary_open_transactions_title).text

    def return_account_summary_open_transactions_quotes_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_open_transactions_quotes_title))
        return self.driver.find_element(*self.account_summary_open_transactions_quotes_title).text

    def return_account_summary_open_transactions_changes_title(self):
        return self.driver.find_element(*self.account_summary_open_transactions_changes_title).text

    def return_account_summary_open_transactions_cancellations_title(self):
        return self.driver.find_element(*self.account_summary_open_transactions_cancellations_title).text

    def return_account_summary_open_transactions_renewals_title(self):
        return self.driver.find_element(*self.account_summary_open_transactions_renewals_title).text

    def return_account_summary_involved_agencies_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_involved_agencies_title))
        return self.driver.find_element(*self.account_summary_involved_agencies_title).text

    def check_account_summary_involved_agencies_item(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_involved_agencies_items))

    def return_account_summary_status_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_status))
        return self.driver.find_element(*self.account_summary_status).text

    def return_account_summary_status_value(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_status_value))
        return self.driver.find_element(*self.account_summary_status_value).text

    def return_account_summary_issued_policies_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_issued_policies_title))
        return self.driver.find_element(*self.account_summary_issued_policies_title).text

    def return_account_summary_issued_policies_table_product_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_issued_policies_table_product_title))
        return self.driver.find_element(*self.account_summary_issued_policies_table_product_title).text

    def return_account_summary_issued_policies_table_policy_type_title(self):
        return self.driver.find_element(*self.account_summary_issued_policies_table_policy_type_title).text

    def return_account_summary_issued_policies_table_status_title(self):
        return self.driver.find_element(*self.account_summary_issued_policies_table_status_title).text

    def return_account_summary_issued_policies_table_policy_number_title(self):
        return self.driver.find_element(*self.account_summary_issued_policies_table_policy_number_title).text

    def return_account_summary_issued_policies_table_insured_title(self):
        return self.driver.find_element(*self.account_summary_issued_policies_table_insured_title).text

    def return_account_summary_issued_policies_table_effective_date_title(self):
        return self.driver.find_element(*self.account_summary_issued_policies_table_effective_date_title).text

    def return_account_summary_issued_policies_table_expiration_date_title(self):
        return self.driver.find_element(*self.account_summary_issued_policies_table_expiration_date_title).text

    def check_if_account_summary_has_issued_policies(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(self.account_summary_issued_policies_table_first_policy))
            return True
        except:
            return False

    def return_account_summary_issued_policies_table_no_policies_label_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_issued_policies_table_no_policies_label))
        return self.driver.find_element(*self.account_summary_issued_policies_table_no_policies_label).text

    def return_account_summary_issued_policies_table_first_policy_type_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_summary_issued_policies_table_first_policy_type))
        return self.driver.find_element(*self.account_summary_issued_policies_table_first_policy_type).text

    def check_policy_status_all_canceled(self):
        for i in range(len(self.driver.find_elements(*self.account_summary_issued_policies_table_list))):
            if self.driver.find_elements(*self.account_summary_issued_policies_table_list)[i].text != "Canceladas":
                return False
        return True