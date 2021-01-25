from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons
from selenium.webdriver.support.select import Select


class PageAccountOpenTransactions():
    OPEN_TRANSACTION_STATUS = ('Todo', 'Borrador')

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.account_open_transactions_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[4]')
        self.account_open_transactions_mosaic_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[4]/div[3]')
        self.account_open_transactions_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/h2/ng-transclude')
        self.account_open_transactions_dropdown_filter = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div/select')
        self.account_open_transactions_search_box = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div/input')
        self.account_open_transactions_table_policy_number_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[1]/div')
        self.account_open_transactions_table_endorse_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[2]/div')
        self.account_open_transactions_table_job_number_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[3]/div')
        self.account_open_transactions_table_transaction_status_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[4]/div')
        self.account_open_transactions_table_type_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[5]/div')
        self.account_open_transactions_table_period_status_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[6]/div')
        self.account_open_transactions_table_effective_date_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/thead/tr/th[8]/div')
        self.account_no_open_transactions_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/span/span')
        self.account_open_transactions_table_first_item = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/table/tbody/tr')

    def go_to_account_open_transactions(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_open_transactions_mosaic)).click()
        self.commons.check_gw_loader_not_visible()

    def return_number_open_transactions(self):
        return int(self.driver.find_element(*self.account_open_transactions_mosaic_number).text)

    def return_account_open_transactions_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_transactions_title))
        return self.driver.find_element(*self.account_open_transactions_title).text

    def select_open_transactions_filter_by_text(self, text):
        open_transactions_filter = Select(self.driver.find_element(*self.account_open_transactions_dropdown_filter))
        open_transactions_filter.select_by_visible_text(text)

    def return_account_open_transactions_search_placeholder(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_transactions_search_box))
        return self.driver.find_element(*self.account_open_transactions_search_box).get_attribute("placeholder")

    def return_account_open_transactions_table_policy_number_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_policy_number_title).text

    def return_account_open_transactions_table_endorse_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_endorse_title).text

    def return_account_open_transactions_table_job_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_job_number_title).text

    def return_account_open_transactions_table_transaction_status_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_transaction_status_title).text

    def return_account_open_transactions_table_type_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_type_title).text

    def return_account_open_transactions_table_period_status_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_period_status_title).text

    def return_account_open_transactions_table_effective_date_title(self):
        return self.driver.find_element(*self.account_open_transactions_table_effective_date_title).text

    def return_account_no_open_transactions_label(self):
        return self.driver.find_element(*self.account_no_open_transactions_label).text

    def check_presence_open_transactions_first_item(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_transactions_table_first_item))
