from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons

class PagePolicyDocuments():
    def __init__(self, driver):
        self.driver = driver
        self.common = Commons(self.driver)
        self.gw_loader = (By.CLASS_NAME, 'gw-loader__opacity')
        self.policy_documents_mosaic = (By.CLASS_NAME, 'gw-tile-content.ng-binding')
        self.policy_documents_no_docs_text = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[2]/div[2]/span')
        self.policy_documents_upload_text_1200px = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[1]/div[1]/gw-file-upload-viewer/div/div[1]/div[3]/div/span[1]')
        self.policy_documents_upload_text_480px = (By.CLASS_NAME, 'gw-file-upload-message_tapable.ng-binding')
        self.policy_documents_table_search_box = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[1]/div[2]/div/span/input')
        self.policy_documents_table_column_name = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[2]/div[1]/table/thead/tr/th[1]/div')
        self.policy_documents_table_column_date = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[2]/div[1]/table/thead/tr/th[2]/div')
        self.policy_documents_table_column_type = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[2]/div[1]/table/thead/tr/th[3]/div')
        self.policy_documents_table_column_author = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div/div/div/div[2]/div[1]/table/thead/tr/th[4]/div')

    def go_to_policy_documents(self):
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(self.gw_loader))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.policy_documents_mosaic))
        self.common.scroll_top_of_the_page()
        self.driver.find_elements(*self.policy_documents_mosaic)[3].click()

    def return_number_of_documents(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(self.gw_loader))
        return self.driver.find_elements(*self.policy_documents_mosaic)[3].text

    def return_no_documents_text(self):
        return self.driver.find_element(*self.policy_documents_no_docs_text).text

    def return_upload_document_text_1200px(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.policy_documents_upload_text_1200px))
        return self.driver.find_element(*self.policy_documents_upload_text_1200px).text

    def return_upload_document_text_480px(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.policy_documents_upload_text_480px))
        return self.driver.find_element(*self.policy_documents_upload_text_480px).text

    def return_documents_search_box_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.policy_documents_table_search_box))
        return self.driver.find_element(*self.policy_documents_table_search_box).get_attribute('placeholder')

    def return_documents_table_header_name_text(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.policy_documents_table_column_name))
        return self.driver.find_element(*self.policy_documents_table_column_name).text

    def return_documents_table_header_date_text(self):
        return self.driver.find_element(*self.policy_documents_table_column_date).text

    def return_documents_table_header_type_text(self):
        return self.driver.find_element(*self.policy_documents_table_column_type).text

    def return_documents_table_header_author_text(self):
        return self.driver.find_element(*self.policy_documents_table_column_author).text


