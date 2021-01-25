from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons
from selenium.webdriver.support.select import Select


class PageAccountBilling():
    POLICY_LOBS = ('Accidentes Personales', 'Automotores', 'Vida Colectivo')
    POLICY_STATUS = ('Vencido', 'En vigencia', 'A renovar')
    ADD_AUTOMATIC_PAYMENT_LINKS = ('Desadherir débito automático', 'Configurar débitos automáticos')
    PAYMENT_ENITITES = ('Débito en cuenta', 'MASTERCARD', 'WILLINER ADHERENTE', 'WILLINER TAPERITAS', 'WILLINER RAFAELA', 'DEL CENTRO', 'COYSPU', 'JBS - SWIFT', 'ELEBAR', 'JOHN DEERE', 'MARCOS JUAREZ', 'AGRONACION', 'GALICIA RURAL', 'TDF', 'QIDA', 'PATAGONIA', 'DINERS CLUB', 'CREDICLUB', 'AMEX', 'VISA', 'CABAL', 'NARANJA')

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.account_billing_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[6]/div[1]')
        self.account_billing_primary_payer = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[1]/lseg-table-subsection[1]/div/div/div/div[1]')
        self.account_billing_primary_name = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[1]/lseg-table-subsection[1]/div/ng-transclude/table/tbody/tr[1]/td[1]')
        self.account_billing_primary_address = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[1]/lseg-table-subsection[1]/div/ng-transclude/table/tbody/tr[2]/td[1]')
        self.account_billing_primary_phone = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[1]/lseg-table-subsection[1]/div/ng-transclude/table/tbody/tr[3]/td[1]')
        self.account_billing_producer_codes = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[2]/lseg-table-subsection[1]/div/div/div/div[1]')
        self.account_billing_status = (By.XPATH,  '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[2]/lseg-table-subsection[2]/div/div/div/div[1]')
        self.account_billing_automatic_payment_status = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[1]/lseg-table-subsection[2]/div/ng-transclude/table/tbody/tr/td')
        self.account_billing_billing_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[2]/ul/li[1]')
        self.account_billing_automatic_payments_tab = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[2]/ul/li[2]')
        self.account_billing_customer_payment_summary = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[1]')
        self.account_billing_customer_payment_summary_amount = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[2]/div[1]/div[1]/label')
        self.account_billing_customer_payment_summary_payment = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[2]/div[1]/div[2]/label')
        self.account_billing_customer_payment_summary_balance = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[2]/div[1]/div[4]/label')
        self.account_billing_customer_payment_summary_balance_value = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[2]/div[1]/div[4]/span')
        self.account_billing_policies_owned_by_account = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[1]')
        self.account_billing_policies_owned_by_account_table_policy_number = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[1]/div')
        self.account_billing_policies_owned_by_account_table_product = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[2]/div')
        self.account_billing_policies_owned_by_account_table_effective_date = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[3]/div')
        self.account_billing_policies_owned_by_account_table_expiration_date = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[4]/div')
        self.account_billing_policies_owned_by_account_table_adjusted_amount = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[5]/div')
        self.account_billing_policies_owned_by_account_table_paid = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[6]/div')
        self.account_billing_policies_owned_by_account_table_balance = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[7]/div')
        self.account_billing_policies_owned_by_account_table_status = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/thead/tr/th[8]/div')
        self.account_billing_policies_owned_by_account_first_item = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/tbody/tr[1]')
        self.account_billing_policies_owned_by_account_first_item_product = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/tbody/tr[1]/td[2]')
        self.account_billing_policies_owned_by_account_first_item_effective_date = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/tbody/tr[1]/td[3]')
        self.account_billing_policies_owned_by_account_first_item_expiration_date = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[3]/div/div[2]/table/tbody/tr[1]/td[4]')
        self.account_billing_inactive_popup = (By.XPATH, '/html/body/div[3]/div/div[1]')
        self.account_billing_inactive_popup_close_button = (By.XPATH, '/html/body/div[3]/div/div[3]/div/gw-button/button')
        self.account_billing_inactive_primary_payer_info = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/div[1]/div/div[1]/lseg-table-subsection/div/ng-transclude/div/span')
        self.account_billing_inactive_no_billing_data_info = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[2]/div/span')
        self.account_billing_acutomatic_payments_no_invoice_info = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[2]/div/span')
        self.account_billing_automatic_payments_first_item = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]')
        self.account_billing_automatic_payments_first_item_lob = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]/lseg-card/div/lseg-card-container/ng-transclude/div/div[2]/div[1]')
        self.account_billing_automatic_payments_first_item_status = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]/lseg-card/div/lseg-card-container/ng-transclude/div/div[3]/div[2]/div')
        self.account_billing_automatic_payments_first_item_expiration_date = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info/lseg-card/div/lseg-card-container/ng-transclude/div/div[4]/div/div[1]/span[2]/strong')
        self.account_billing_automatic_payments_first_item_payment_information = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]/lseg-card/div/lseg-card-container/ng-transclude/div/div[4]/div/div[2]/div[2]/div')
        self.account_billing_automatic_payments_first_item_no_payment_information = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]/lseg-card/div/lseg-card-container/ng-transclude/div/div[4]/div/div[2]/div[2]/span')
        self.account_billing_automatic_payments_first_item_payment_information_entity = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]/lseg-card/div/lseg-card-container/ng-transclude/div/div[4]/div/div[2]/div[2]/div/span[1]')
        self.account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/gw-account-payment/div/div/div/div[1]/lseg-gateway-billing-payment-line-info[1]/lseg-card/div/lseg-card-container/ng-transclude/div/div[4]/div/div[3]/a')
        self.account_billing_other_policies_billed_to_account = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/gw-account-billing-payment/div/ui-view/div/div[1]/div[4]/div/div[1]')


    def go_to_account_billing(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_billing_mosaic)).click()
        self.commons.check_gw_loader_not_visible()

    def return_account_billing_primary_payer_title(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.account_billing_primary_payer))
        return self.driver.find_element(*self.account_billing_primary_payer).text

    def return_account_billing_primary_payer_name_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_primary_name))
        return self.driver.find_element(*self.account_billing_primary_name).text

    def return_account_billing_primary_payer_address_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_primary_address))
        return self.driver.find_element(*self.account_billing_primary_address).text

    def return_account_billing_primary_payer_phone_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_primary_phone))
        return self.driver.find_element(*self.account_billing_primary_phone).text

    def return_account_billing_producer_codes_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_producer_codes))
        return self.driver.find_element(*self.account_billing_producer_codes).text

    def return_account_billing_status_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_status))
        return self.driver.find_element(*self.account_billing_status).text

    def return_account_billing_automatic_payment_status_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_automatic_payment_status))
        return self.driver.find_element(*self.account_billing_automatic_payment_status).text

    def return_account_billing_billing_tab_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_billing_tab))
        return self.driver.find_element(*self.account_billing_billing_tab).text

    def return_account_billing_automatic_payments_tab_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_automatic_payments_tab))
        return self.driver.find_element(*self.account_billing_automatic_payments_tab).text

    def return_account_billing_customer_payment_summary_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_customer_payment_summary))
        return self.driver.find_element(*self.account_billing_customer_payment_summary).text

    def return_account_billing_policies_owned_by_account_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account).text

    def return_account_billing_other_policies_billed_to_account_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_other_policies_billed_to_account))
        return self.driver.find_element(*self.account_billing_other_policies_billed_to_account).text

    def return_account_billing_customer_payment_summary_amount_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_customer_payment_summary_amount))
        return self.driver.find_element(*self.account_billing_customer_payment_summary_amount).text

    def return_account_billing_customer_payment_summary_payment_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_customer_payment_summary_payment))
        return self.driver.find_element(*self.account_billing_customer_payment_summary_payment).text

    def return_account_billing_customer_payment_summary_balance_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_customer_payment_summary_balance))
        return self.driver.find_element(*self.account_billing_customer_payment_summary_balance).text

    def return_account_billing_customer_payment_summary_balance_value(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_customer_payment_summary_balance_value))
        return self.driver.find_element(*self.account_billing_customer_payment_summary_balance_value).text

    def return_account_billing_policies_owned_by_account_table_policy_number_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_policy_number))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_policy_number).text

    def return_account_billing_policies_owned_by_account_table_product_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_product))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_product).text

    def return_account_billing_policies_owned_by_account_table_effective_date_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_effective_date))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_effective_date).text

    def return_account_billing_policies_owned_by_account_table_expiration_date_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_expiration_date))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_expiration_date).text

    def return_account_billing_policies_owned_by_account_table_adjusted_amount_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_adjusted_amount))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_adjusted_amount).text

    def return_account_billing_policies_owned_by_account_table_paid_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_paid))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_paid).text

    def return_account_billing_policies_owned_by_account_table_balance_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_balance))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_balance).text

    def return_account_billing_policies_owned_by_account_table_status_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_table_status))
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_table_status).text

    def check_presence_account_billing_policies_owned_by_account_first_item(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_policies_owned_by_account_first_item))

    def return_account_billing_policies_owned_by_account_first_item_product(self):
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_first_item_product).text

    def return_account_billing_policies_owned_by_account_first_item_effective_date(self):
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_first_item_effective_date).text

    def return_account_billing_policies_owned_by_account_first_item_expiration_date(self):
        return self.driver.find_element(*self.account_billing_policies_owned_by_account_first_item_expiration_date).text

    def return_account_billing_inactive_popup_title(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.account_billing_inactive_popup))
        return self.driver.find_element(*self.account_billing_inactive_popup).text

    def close_account_billing_inactive_popup(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_billing_inactive_popup_close_button)).click()

    def return_account_billing_inactive_primary_payer_info_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_inactive_primary_payer_info))
        return self.driver.find_element(*self.account_billing_inactive_primary_payer_info).text

    def return_account_billing_inactive_no_billing_data_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_inactive_no_billing_data_info))
        return self.driver.find_element(*self.account_billing_inactive_no_billing_data_info).text

    def go_to_account_billing_automatic_payments_tab(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_billing_automatic_payments_tab)).click()

    def return_account_billing_automatic_payments_no_invoices_info_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_acutomatic_payments_no_invoice_info))
        return self.driver.find_element(*self.account_billing_acutomatic_payments_no_invoice_info).text

    def check_presence_account_billing_automatic_payments_first_item(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_billing_automatic_payments_first_item))

    def return_account_billing_automatic_payments_first_item_lob(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_lob).text

    def return_account_billing_automatic_payments_first_item_status(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_status).text

    def return_account_billing_automatic_payments_first_item_expiration_date(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_expiration_date).text

    def return_account_billing_automatic_payments_first_item_payment_information_text(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_payment_information).text

    def return_account_billing_automatic_payments_first_item_no_payment_information_text(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_no_payment_information).text

    def return_account_billing_automatic_payments_first_item_payment_information_entity_text(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_payment_information_entity).text

    def return_account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link_text(self):
        return self.driver.find_element(*self.account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link).text