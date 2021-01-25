from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageLogin():

    def __init__(self,my_driver):
        self.username = (By.ID, 'username')
        self.password = (By.NAME, 'password')
        self.login_b = (By.XPATH, '//*[@id="loginForm"]/section/p[1]/button')
        self.logout_b = (By.XPATH,'//*[@id="page-inner"]/div/div/header/div[1]/div/div[2]/div/div/gw-auth-status/div/div/a/span')
        # self.query_button = 'submit_search'
        self.driver = my_driver

    def login(self, user, pwd):
        username_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.username))
        username_box.send_keys(user)
        password_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.password))
        password_box.send_keys(pwd)
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_b))
        login_button.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.logout_b))
        # self.driver.find_element(*self.query_top).send_keys(item)
        # self.driver.find_element(*self.query_button).click()
        # self.driver.find_element_by_id(self.query_top).send_keys(item)
        # self.driver.find_element_by_name(self.query_button).click()