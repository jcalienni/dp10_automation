from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons
from selenium.webdriver.support.select import Select


class PageAccountClaims():
    CLAIMS_LOBS = ('Accidentes Personales', 'Automotores', 'Vida Colectivo')
    CLAIMS_STATUS = ('Borrador', 'Abierto', 'Cerrado')

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.account_claims_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[5]')
        self.account_claims_mosaic_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[5]/div[3]')
        self.account_claims_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[1]/h2/ng-transclude')
        self.account_claims_dropdown_filter = (By.ID, 'LOBSelect')
        self.account_claims_search_box = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[1]/div/span[2]/input')
        self.account_no_claims_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[3]/span')
        self.account_claims_table_product_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[1]/div')
        self.account_claims_table_claim_number_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[2]/div')
        self.account_claims_table_policy_number_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[3]/div')
        self.account_claims_table_date_of_loss_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[4]/div')
        self.account_claims_table_status_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[5]/div')
        self.account_claims_table_risk_unit_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[6]/div')
        self.account_claims_table_remove_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/thead/tr/th[7]/div')
        self.account_claims_dropdown_filter = (By.XPATH, '//*[@id="LOBSelect"]')
        self.account_claims_first_item = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]')
        self.account_claims_first_item_product = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]/td[1]')
        self.account_claims_first_item_claim_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]/td[2]/span/a')
        self.account_claims_first_item_policy_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]/td[3]/a')
        self.account_claims_first_item_date_of_loss = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]/td[4]')
        self.account_claims_first_item_status = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]/td[5]')
        self.account_claims_first_item_remove = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div/div/div[2]/table/tbody/tr[1]/td[7]/div/gw-tooltip/opener/div')

    def go_to_account_claims(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_claims_mosaic)).click()
        self.commons.check_gw_loader_not_visible()

    def return_account_claims_number(self):
        return int(self.driver.find_element(*self.account_claims_mosaic_number).text)

    def return_account_claims_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_claims_title))
        return self.driver.find_element(*self.account_claims_title).text

    def select_claims_filter_by_text(self, text):
        claims_filter = Select(self.driver.find_element(*self.account_claims_dropdown_filter))
        claims_filter.select_by_visible_text(text)

    def return_account_no_claims_label(self):
        return self.driver.find_element(*self.account_no_claims_label).text

    def return_account_open_transactions_search_placeholder(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_claims_search_box))
        return self.driver.find_element(*self.account_claims_search_box).get_attribute("placeholder")

    def return_account_claims_table_product_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_claims_table_product_title))
        return self.driver.find_element(*self.account_claims_table_product_title).text

    def return_account_claims_table_claim_number_title(self):
        return self.driver.find_element(*self.account_claims_table_claim_number_title).text

    def return_account_claims_table_policy_number_title(self):
        return self.driver.find_element(*self.account_claims_table_policy_number_title).text

    def return_account_claims_table_date_of_loss_title(self):
        return self.driver.find_element(*self.account_claims_table_date_of_loss_title).text

    def return_account_claims_table_status_title(self):
        return self.driver.find_element(*self.account_claims_table_status_title).text

    def return_account_claims_table_risk_unit_title(self):
        return self.driver.find_element(*self.account_claims_table_risk_unit_title).text

    def return_account_claims_table_remove_title(self):
        return self.driver.find_element(*self.account_claims_table_remove_title).text

    def select_account_claims_filter_by_text(self, text):
        open_quotes_filter = Select(self.driver.find_element(*self.account_claims_dropdown_filter))
        open_quotes_filter.select_by_visible_text(text)

    def check_presence_claims_table_first_item(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(self.account_claims_first_item))
            return True
        except:
            return False

    def return_account_claims_table_first_item_product_text(self):
        return self.driver.find_element(*self.account_claims_first_item_product).text

    def check_account_claims_first_item_claim_number_link(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_claims_first_item_claim_number))

    def check_account_claims_first_item_policy_number_link(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_claims_first_item_policy_number))

    def return_account_claims_first_item_date_of_loss_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_claims_first_item_date_of_loss))
        return self.driver.find_element(*self.account_claims_first_item_date_of_loss).text

    def return_account_claims_first_item_status_text(self):
        return self.driver.find_element(*self.account_claims_first_item_status).text

    def return_account_claims_first_item_remove_class(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_claims_first_item_remove))
        return self.driver.find_element(*self.account_claims_first_item_remove).get_attribute("class")

