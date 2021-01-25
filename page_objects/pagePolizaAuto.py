from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from commons.Commons import Commons


class PagePolizaAuto():

    def __init__(self,my_driver):
        self.driver = my_driver
        self.common = Commons(self.driver)
        self.poliza_title = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[1]/div[1]/div/h1/ng-transclude')
        self.resumen_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[1]')
        self.resumen_detalles = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/div/div[1]/div/div/h2/span[1]')
        self.resumen_vehiculos_dropdown = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[1]/div/div/h2/span[1]')
        self.resumen_detalles_tipo_de_poliza = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/lseg-table-subsection/div/ng-transclude/table/tbody/tr[4]/td[2]')
        self.resumen_poliza_pack_dropdown = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/lseg-policy-pack-periods/div/div[1]/div/div/h2/span[1]')
        self.resumen_poliza_pack_number = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/lseg-policy-pack-periods/div/div[2]/div/table/tbody/tr/td[1]/a')
        self.resumen_vehiculos_table_marca = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[1]/div')
        self.resumen_vehiculos_table_modelo = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[2]/div')
        self.resumen_vehiculos_table_anio = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[3]/div')
        self.resumen_vehiculos_table_patente = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[4]/div')
        self.resumen_vehiculos_table_suma_aseg = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[5]/div')
        self.resumen_vehiculos_table_plan = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[6]/div')
        self.resumen_vehiculos_coberturas_dropdown = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/tbody/tr[1]/td[7]/span')

        self.resumen_conductores_dropdown = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[1]/div/div/h2/span[1]')
        self.resumen_registro_table_nombre = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[1]/div')
        self.resumen_registro_table_fecha_nacimiento = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[2]/div')
        self.resumen_registro_table_id = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[3]/div')
        self.resumen_registro_table_permiso = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[4]/div')
        self.resumen_registro_table_categoria = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/thead/tr/th[5]/div')
        self.resumen_registro_coberturas_dropdown = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[2]/div/gw-policy-coverages/div/div/div/div[2]/div/table/tbody/tr[1]/td[6]/span')

        self.resumen_transacciones = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[1]/div/div/h2/span[1]')
        self.resumen_transactions_table_policy = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[1]/div')
        self.resumen_transactions_table_endorse = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[2]/div')
        self.resumen_transactions_table_job = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[3]/div')
        self.resumen_transactions_table_status = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[4]/div')
        self.resumen_transactions_table_type = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[5]/div')
        self.resumen_transactions_table_period_status = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[6]/div')
        self.resumen_transactions_table_premium = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[7]/div')
        self.resumen_transactions_table_effective_date = (By.XPATH,'//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[3]/ui-view/div[3]/div/div/div[2]/div/div[2]/div/div/table/thead/tr/th[8]/div')

        self.documentos_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[4]')
        self.siniestros_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[5]')
        self.facturacion_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[6]')
        self.impresiones_mosaico = (By.XPATH, '//*[@id="page-inner"]/div/div/main/div/div[2]/div/ui-view/div/div[2]/div/div[7]')



    def go_to_poliza(self, entorno , poliza):
        self.driver.get(entorno +'policies/' + poliza + '/summary')

    def return_poliza_title (self):
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(self.poliza_title, 'Automotores'))
        self.common.check_gw_loader_not_visible()
        return self.driver.find_element(*self.poliza_title).text

    def return_policy_type(self):
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(self.resumen_detalles_tipo_de_poliza))
        return self.driver.find_element(*self.resumen_detalles_tipo_de_poliza).text

    def return_policy_pack_number(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.resumen_poliza_pack_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.resumen_poliza_pack_number, '30'))
        return self.driver.find_element(*self.resumen_poliza_pack_number).text

    def check_if_vehiculos_exist(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.resumen_vehiculos_dropdown))
        return self.driver.find_element(*self.resumen_vehiculos_dropdown).text

    def open_vehicles_dropdown(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.resumen_vehiculos_dropdown)).click()

    def return_vehicles_table_marca_title(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.resumen_vehiculos_table_marca, 'Marca'))
        return self.driver.find_element(*self.resumen_vehiculos_table_marca).text

    def return_vehicles_table_modelo_title(self):
        return self.driver.find_element(*self.resumen_vehiculos_table_modelo).text

    def return_vehicles_table_anio_title(self):
        return self.driver.find_element(*self.resumen_vehiculos_table_anio).text

    def return_vehicles_table_patente_title(self):
        return self.driver.find_element(*self.resumen_vehiculos_table_patente).text

    def return_vehicles_table_suma_aseg_title(self):
        return self.driver.find_element(*self.resumen_vehiculos_table_suma_aseg).text

    def return_vehicles_table_plan_title(self):
        return self.driver.find_element(*self.resumen_vehiculos_table_plan).text

    def open_close_vehicles_coverages_dropdown(self):
        WebDriverWait(self.driver, 1).until(EC.text_to_be_present_in_element(self.resumen_vehiculos_coberturas_dropdown, 'Mostrar coberturas'))
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.resumen_vehiculos_coberturas_dropdown)).click()
        WebDriverWait(self.driver, 1).until(EC.text_to_be_present_in_element(self.resumen_vehiculos_coberturas_dropdown, 'Ocultar coberturas'))
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.resumen_vehiculos_coberturas_dropdown)).click()

    def open_drivers_dropdown(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.resumen_conductores_dropdown)).click()

    def return_registro_table_nombre_title(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.resumen_registro_table_nombre, 'Nombre'))
        return self.driver.find_element(*self.resumen_vehiculos_table_marca).text

    def return_registro_table_fecha_nacimiento_title(self):
        return self.driver.find_element(*self.resumen_registro_table_fecha_nacimiento).text

    def return_registro_table_id_title(self):
        return self.driver.find_element(*self.resumen_registro_table_id).text

    def return_registro_table_permiso_title(self):
        return self.driver.find_element(*self.resumen_registro_table_permiso).text

    def return_registro_table_categoria_title(self):
        return self.driver.find_element(*self.resumen_registro_table_categoria).text

    def open_close_drivers_coverages_dropdown(self):
        WebDriverWait(self.driver, 1).until(EC.text_to_be_present_in_element(self.resumen_registro_coberturas_dropdown, 'Mostrar coberturas'))
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.resumen_registro_coberturas_dropdown)).click()
        WebDriverWait(self.driver, 1).until(EC.text_to_be_present_in_element(self.resumen_registro_coberturas_dropdown, 'Ocultar coberturas'))
        WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(self.resumen_registro_coberturas_dropdown)).click()

    def check_if_transacciones_exist(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.resumen_transacciones, 'Transacciones'))
        return self.driver.find_element(*self.resumen_transacciones).text

    def open_transactions_dropdown(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.resumen_transacciones)).click()

    def return_transactions_table_policy_title(self):
        WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(self.resumen_transactions_table_policy, 'Número de póliza'))
        return self.driver.find_element(*self.resumen_transactions_table_policy).text

    def return_transactions_table_endorse_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_endorse).text

    def return_transactions_table_job_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_job).text

    def return_transactions_table_status_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_status).text

    def return_transactions_table_type_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_type).text

    def return_transactions_table_period_status_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_period_status).text

    def return_transactions_table_premium_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_premium).text

    def return_transactions_table_effective_date_title(self):
        return self.driver.find_element(*self.resumen_transactions_table_effective_date).text






