from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons
from selenium.webdriver.support.select import Select


class PageAccountOpenQuotes():
    OPEN_QUOTE_STATUS = ('Cotizado', 'Borrador')

    def __init__(self, driver):
        self.driver = driver
        self.commons = Commons(self.driver)
        self.account_open_quotes_mosaic = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[3]')
        self.account_open_quotes_mosaic_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div/div/div[3]/div[3]')
        self.account_open_quotes_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/h2/ng-transclude')
        self.account_open_quotes_search_box = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div/input')
        self.account_open_quotes_table_created_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/thead/tr/th[1]/div')
        self.account_open_quotes_table_product_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/thead/tr/th[2]/div')
        self.account_open_quotes_table_job_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/thead/tr/th[3]/div')
        self.account_open_quotes_table_premium_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/thead/tr/th[5]/div')
        self.account_open_quotes_table_status_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/thead/tr/th[6]/div')
        self.account_no_open_quotes_label = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[2]/div')
        self.account_open_quotes_first_item = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/tbody/tr')
        self.account_open_quotes_first_item_creted_date = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[1]')
        self.account_open_quotes_first_item_job = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]/span[1]/a')
        self.account_open_quotes_first_item_status = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[6]')
        self.account_open_quotes_dropdown_filter = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/ui-view/div/div[1]/div/select')

    def go_to_account_open_quotes(self):
        self.commons.scroll_top_of_the_page()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_open_quotes_mosaic)).click()
        self.commons.check_gw_loader_not_visible()

    def return_account_open_quotes_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_quotes_title))
        return self.driver.find_element(*self.account_open_quotes_title).text

    def return_account_open_quotes_search_placeholder(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_quotes_search_box))
        return self.driver.find_element(*self.account_open_quotes_search_box).get_attribute("placeholder")

    def return_number_open_quotes(self):
        return int(self.driver.find_element(*self.account_open_quotes_mosaic_number).text)

    def check_presence_open_quote_first_item(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_quotes_first_item))

    def return_account_no_open_quotes_label(self):
        return self.driver.find_element(*self.account_no_open_quotes_label).text

    def return_account_open_quotes_table_created_title(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_quotes_table_created_title))
        return self.driver.find_element(*self.account_open_quotes_table_created_title).text

    def return_account_open_quotes_table_product_title(self):
        return self.driver.find_element(*self.account_open_quotes_table_product_title).text

    def return_account_open_quotes_table_job_title(self):
        return self.driver.find_element(*self.account_open_quotes_table_job_title).text

    def return_account_open_quotes_table_premium_title(self):
        return self.driver.find_element(*self.account_open_quotes_table_premium_title).text

    def return_account_open_quotes_table_status_title(self):
        return self.driver.find_element(*self.account_open_quotes_table_status_title).text

    def return_open_quotes_first_item_date_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.account_open_quotes_first_item_creted_date))
        return self.driver.find_element(*self.account_open_quotes_first_item_creted_date).text

    def check_open_quotes_first_item_job_link(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.account_open_quotes_first_item_job))

    def return_open_quotes_first_item_status_text(self):
        return self.driver.find_element(*self.account_open_quotes_first_item_status).text

    def select_open_quotes_filter_by_text(self, text):
        open_quotes_filter = Select(self.driver.find_element(*self.account_open_quotes_dropdown_filter))
        open_quotes_filter.select_by_visible_text(text)


