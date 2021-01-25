from datetime import datetime as dt
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime


class Commons():

    def __init__(self,my_driver):
        self.driver = my_driver
        self.gw_loader = (By.CLASS_NAME, 'gw-loader__opacity')

    def scroll_top_of_the_page(self):
        self.driver.execute_script("window.scrollTo(0,0);")

    def take_screenshot(self, request):
        self.driver.get_screenshot_as_file('../dp10_automation/screenshots/ ' + dt.now().strftime('%Y-%m-%d_%H-%M-%S') + " - " + request + '.png')

    def check_gw_loader_not_visible(self):
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located(self.gw_loader))

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d/%m/%Y')
        except ValueError:
            raise ValueError(f"Formato de fecha {date_text} incorrecta, deberia ser DD/MM/YYYY")