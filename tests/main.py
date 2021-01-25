import pytest
import time

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from commons.Commons import Commons
from page_objects.pageLogin import PageLogin
from page_objects.pageAccountSummary import PageAccountSummary
from page_objects.pageAccountContacts import PageAccountContacts
from page_objects.pageAccountOpenQuotes import PageAccountOpenQuotes
from page_objects.pageAccountOpenTransactions import PageAccountOpenTransactions
from page_objects.pageAccountClaims import PageAccountClaims
from page_objects.pageAccountBilling import PageAccountBilling

from page_objects.pagePolizaAuto import PagePolizaAuto
from page_objects.pagePolicyContacts import PagePolicyContacts
from page_objects.pagePolicyNotes import PagePolicyNotes
from page_objects.pagePolicyDocuments import PagePolicyDocuments

from page_objects.pageClaimSummary import PageClaimSummary


class TestMain:
    logger = LogGen.loggen()
    logger.info("*****************************************************************************")

    # @pytest.mark.skip(reason="not needed")
    def test_login_page_title(self, setUp, environment, request):
        try:
            self.driver = setUp
            self.entorno = environment
            self.commons = Commons(self.driver)
            self.driver.get(ReadConfig.getUrlEnvironment(self.entorno) + 'accounts')
            actual_title = self.driver.title
            assert 'La Segunda Login' == actual_title
            self.logger.info ("******************* test_login_page_title PASSED *******************")
            self.driver.close()
        except Exception as e:
            self.logger.error("******************* test_login_page_title FAILED *******************")
            self.commons.take_screenshot(request.node.name)
            self.driver.close()
            raise e

    # @pytest.mark.skip(reason="not needed")
    def test_login(self, setUp, environment, request):
        try:
            self.driver = setUp
            self.entorno = environment
            self.commons = Commons(self.driver)
            self.driver.get(ReadConfig.getUrlEnvironment(self.entorno) + 'accounts')
            self.loginPage = PageLogin(self.driver)

            self.loginPage.login(ReadConfig.getUsername(), ReadConfig.getPassword())
            actual_title = self.driver.title
            assert 'Producer Engage' == actual_title
            self.logger.info("******************* test_login PASSED *******************")
            self.driver.close()
        except Exception as e:
            self.logger.error("******************* test_login FAILED *******************")
            self.commons.take_screenshot(request.node.name)
            self.driver.close()
            raise e

    # @pytest.mark.skip(reason="not needed")
    account_list = [100,101,102,103,104,105,109,117,167]
    @pytest.mark.parametrize('account_number', account_list)
    def test_smoke_account (self, setUp, environment, request, account_number):
        try:
            self.driver = setUp
            self.entorno = environment
            self.commons = Commons(self.driver)
            self.loginPage = PageLogin(self.driver)
            self.driver.get(ReadConfig.getUrlEnvironment(self.entorno) + 'accounts')
            self.accountsSummaryPage = PageAccountSummary(self.driver)
            self.accountsContactPage = PageAccountContacts(self.driver)
            self.accountOpenQuotesPage = PageAccountOpenQuotes(self.driver)
            self.accountOpenTransactionsPage = PageAccountOpenTransactions(self.driver)
            self.accountClaimsPage = PageAccountClaims(self.driver)
            self.accountBillingPage = PageAccountBilling(self.driver)

            self.loginPage.login(ReadConfig.getUsername(), ReadConfig.getPassword())
            self.accountsSummaryPage.go_to_account(ReadConfig.getUrlEnvironment(self.entorno), str(account_number))
            if self.accountsSummaryPage.return_account_summary_mosaic_text() != 'VISTAS RECIENTEMENTE':
                assert self.accountsSummaryPage.return_account_summary_mosaic_text() == 'RESUMEN'
                assert self.accountsSummaryPage.return_account_contacts_mosaic_text() == 'CONTACTOS'
                assert self.accountsSummaryPage.return_account_open_quotes_mosaic_text() == 'COTIZACIONES ABIERTAS'
                assert self.accountsSummaryPage.return_account_open_transactions_mosaic_text() == 'TRANSACCIONES ABIERTAS'
                assert self.accountsSummaryPage.return_account_claims_mosaic_text() == 'SINIESTROS'
                assert self.accountsSummaryPage.return_account_billing_mosaic_text() == 'FACTURACIÓN Y PAGO'
                self.accountsSummaryPage.click_edit_account_link()
                assert self.accountsSummaryPage.return_edit_account_title_text() == 'Editar detalles de contacto'
                self.accountsSummaryPage.click_cancel_edit_form_button()
                self.accountsSummaryPage.check_edit_form_closed()
                if self.accountsSummaryPage.return_account_personal_data_title() == 'Datos Personales':
                    #Cuenta persona
                    assert self.accountsSummaryPage.return_account_personal_data_official_id_type_title() in self.accountsSummaryPage.OFFICIAL_ID_TYPE
                elif self.accountsSummaryPage.return_account_personal_data_title() == 'Datos de la compañía':
                    #Cuenta empresa
                    assert self.accountsSummaryPage.return_account_personal_data_company_name_title() == 'Razón Social'
                    assert self.accountsSummaryPage.return_account_personal_data_fiscal_id_type_title() in self.accountsSummaryPage.FISCAL_ID_TYPE
                assert self.accountsSummaryPage.return_account_summary_open_transactions_title() == 'Transacciones abiertas'
                assert self.accountsSummaryPage.return_account_summary_open_transactions_quotes_title() == 'Cotizaciones'
                assert self.accountsSummaryPage.return_account_summary_open_transactions_changes_title() == 'Cambios'
                assert self.accountsSummaryPage.return_account_summary_open_transactions_cancellations_title() == 'Cancelaciones'
                assert self.accountsSummaryPage.return_account_summary_open_transactions_renewals_title() == 'Renovaciones'
                assert self.accountsSummaryPage.return_account_summary_involved_agencies_title() == 'Agencias Intervinientes'
                self.accountsSummaryPage.check_account_summary_involved_agencies_item()
                assert self.accountsSummaryPage.return_account_summary_status_title() == 'Estado de la cuenta'
                assert self.accountsSummaryPage.return_account_summary_status_value() in self.accountsSummaryPage.ACCOUNT_STATUS
                if self.accountsSummaryPage.return_account_summary_status_value() == 'ACTIVA':
                    active_account = True
                else:
                    active_account = False
                assert self.accountsSummaryPage.return_account_summary_issued_policies_title() == 'Pólizas emitidas'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_product_title() == 'Producto'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_policy_type_title() == 'Tipo de póliza'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_status_title() == 'Estado'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_policy_number_title() == 'Número de póliza'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_insured_title() == 'Asegurado'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_effective_date_title() == 'Inicio de vigencia'
                assert self.accountsSummaryPage.return_account_summary_issued_policies_table_expiration_date_title() == 'Fin de vigencia'
                if self.accountsSummaryPage.check_if_account_summary_has_issued_policies():
                    assert self.accountsSummaryPage.return_account_summary_issued_policies_table_first_policy_type_text() in self.accountsSummaryPage.POLICY_TYPE
                    account_has_issued_policies = True
                else:
                    account_has_issued_policies = False
                    assert self.accountsSummaryPage.return_account_summary_issued_policies_table_no_policies_label_text() == 'No hay pólizas en esta cuenta'
                if self.accountsSummaryPage.check_policy_status_all_canceled():
                    account_all_policies_cancelled = True
                else:
                    account_all_policies_cancelled = False

                self.accountsContactPage.go_to_account_contacts()
                assert 'Contactos de cuenta' in self.accountsContactPage.return_account_contacts_tab_title()
                assert self.accountsContactPage.return_account_contacts_tab_text() == 'Solo contactos asociados con esta cuenta.'
                assert self.accountsContactPage.return_account_associated_contacts_tab_title() == 'Contactos asociados'
                assert 'Estos contactos se encuentran en cuentas que tienen algún tipo de relación con la cuenta' in self.accountsContactPage.return_account_associated_contacts_tab_text()
                assert str(account_number) in self.accountsContactPage.return_account_associated_contacts_tab_text()

                self.accountOpenQuotesPage.go_to_account_open_quotes()
                assert self.accountOpenQuotesPage.return_account_open_quotes_title() == 'Cotizaciones'
                assert self.accountOpenQuotesPage.return_account_open_quotes_search_placeholder() == 'Buscar cotizaciones'
                assert self.accountOpenQuotesPage.return_account_open_quotes_table_created_title() == 'Creada'
                assert self.accountOpenQuotesPage.return_account_open_quotes_table_product_title() == 'Producto'
                assert self.accountOpenQuotesPage.return_account_open_quotes_table_job_title() == 'Solicitud'
                assert self.accountOpenQuotesPage.return_account_open_quotes_table_premium_title() == 'Prima'
                assert self.accountOpenQuotesPage.return_account_open_quotes_table_status_title() == 'Estado'
                if self.accountOpenQuotesPage.return_number_open_quotes() == 0:
                    assert self.accountOpenQuotesPage.return_account_no_open_quotes_label() == 'No hay cotizaciones abiertas para esta cuenta.'
                else:
                    self.accountOpenQuotesPage.check_presence_open_quote_first_item()
                    self.commons.validate_date(self.accountOpenQuotesPage.return_open_quotes_first_item_date_text())
                    assert self.accountOpenQuotesPage.return_open_quotes_first_item_status_text() in self.accountOpenQuotesPage.OPEN_QUOTE_STATUS
                    self.accountOpenQuotesPage.check_open_quotes_first_item_job_link()
                    self.accountOpenQuotesPage.select_open_quotes_filter_by_text('Se emitieron en los últimos 30 días')
                    self.accountOpenQuotesPage.select_open_quotes_filter_by_text('Abierta, no contratada')
                    self.accountOpenQuotesPage.select_open_quotes_filter_by_text('Abierta, contratada')
                self.accountOpenTransactionsPage.go_to_account_open_transactions()
                assert self.accountOpenTransactionsPage.return_account_open_transactions_title() == 'Transacciones de póliza'
                self.accountOpenTransactionsPage.select_open_transactions_filter_by_text('Borrador')
                self.accountOpenTransactionsPage.select_open_transactions_filter_by_text('Todo')
                assert self.accountOpenTransactionsPage.return_account_open_transactions_search_placeholder() == 'Buscar transacciones'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_policy_number_title() == 'Número de póliza'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_endorse_title() == 'Endoso'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_job_title() == 'Solicitud de trabajo'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_transaction_status_title() == 'Estado de la transacción'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_type_title() == 'Tipo'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_period_status_title() == 'Estado de período'
                assert self.accountOpenTransactionsPage.return_account_open_transactions_table_effective_date_title() == 'Inicio de vigencia'
                if self.accountOpenTransactionsPage.return_number_open_transactions() == 0:
                    assert self.accountOpenTransactionsPage.return_account_no_open_transactions_label() == 'No se encontraron órdenes de trabajo que coincidan con estos filtros'
                else:
                    self.accountOpenTransactionsPage.check_presence_open_transactions_first_item()

                self.accountClaimsPage.go_to_account_claims()
                assert self.accountClaimsPage.return_account_claims_title() == 'Siniestros'
                assert self.accountClaimsPage.return_account_claims_table_product_title() == 'Producto'
                assert self.accountClaimsPage.return_account_claims_table_claim_number_title() == 'Número de siniestro'
                assert self.accountClaimsPage.return_account_claims_table_policy_number_title() == 'Número de póliza'
                assert self.accountClaimsPage.return_account_claims_table_date_of_loss_title() == 'Fecha del siniestro'
                assert self.accountClaimsPage.return_account_claims_table_status_title() == 'Estado'
                assert self.accountClaimsPage.return_account_claims_table_risk_unit_title() == 'Unidad de riesgo'
                assert self.accountClaimsPage.return_account_claims_table_remove_title() == 'Eliminar'

                if self.accountClaimsPage.return_account_claims_number() == 0 and self.accountClaimsPage.check_presence_claims_table_first_item() == False:
                    assert self.accountClaimsPage.return_account_no_claims_label() == 'No hay siniestros'
                else:
                    assert self.accountClaimsPage.return_account_open_transactions_search_placeholder() == 'Buscar'
                    self.accountClaimsPage.check_presence_claims_table_first_item()
                    assert self.accountClaimsPage.return_account_claims_table_first_item_product_text() in self.accountClaimsPage.CLAIMS_LOBS
                    self.accountClaimsPage.check_account_claims_first_item_claim_number_link()
                    self.accountClaimsPage.check_account_claims_first_item_policy_number_link()
                    self.commons.validate_date(self.accountClaimsPage.return_account_claims_first_item_date_of_loss_text())
                    assert self.accountClaimsPage.return_account_claims_first_item_status_text() in self.accountClaimsPage.CLAIMS_STATUS
                    if self.accountClaimsPage.return_account_claims_first_item_status_text() == 'Borrador':
                        assert self.accountClaimsPage.return_account_claims_first_item_remove_class() == 'gw-action-icon__wrap ng-isolate-scope gw-action-icon__wrap_noborder'
                    else:
                        assert self.accountClaimsPage.return_account_claims_first_item_remove_class() == 'gw-action-icon__wrap ng-isolate-scope gw-action-icon__wrap_disabled gw-action-icon__wrap_noborder'

                self.accountBillingPage.go_to_account_billing()
                assert self.accountBillingPage.return_account_billing_primary_payer_title() == 'Pagador principal'
                assert self.accountBillingPage.return_account_billing_producer_codes_title() == 'Códigos de agente'
                assert self.accountBillingPage.return_account_billing_status_title() == 'Estado'
                assert self.accountBillingPage.return_account_billing_billing_tab_text() == 'Facturación'
                assert self.accountBillingPage.return_account_billing_automatic_payments_tab_text() == 'Débitos automáticos'
                if account_has_issued_policies:
                    assert self.accountBillingPage.return_account_billing_automatic_payment_status_text() == 'No suscripto al débito automático'
                    assert self.accountBillingPage.return_account_billing_primary_payer_name_title() == 'Nombre'
                    assert self.accountBillingPage.return_account_billing_primary_payer_address_title() == 'Domicilio'
                    assert self.accountBillingPage.return_account_billing_primary_payer_phone_title() == 'Teléfono'
                    assert self.accountBillingPage.return_account_billing_customer_payment_summary_title() == 'Resumen de pagos del cliente'
                    assert self.accountBillingPage.return_account_billing_customer_payment_summary_amount_title() == 'Monto total'
                    assert self.accountBillingPage.return_account_billing_customer_payment_summary_payment_title() == 'Total pagado'
                    assert self.accountBillingPage.return_account_billing_customer_payment_summary_balance_title() == 'Saldo'
                    assert self.accountBillingPage.return_account_billing_other_policies_billed_to_account_title() == 'Otras pólizas facturadas a esta cuenta'
                    assert self.accountBillingPage.return_account_billing_policies_owned_by_account_title() == 'Pólizas pertenecientes a esta cuenta'
                    if not account_all_policies_cancelled:
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_policy_number_title() == 'Número de póliza'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_product_title() == 'Producto'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_effective_date_title() == 'Fecha de vigencia'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_expiration_date_title() == 'Fecha de vencimiento'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_adjusted_amount_title() == 'Monto'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_paid_title() == 'Pagado'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_balance_title() == 'Saldo'
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_table_status_title() == 'Estado'
                        self.accountBillingPage.check_presence_account_billing_policies_owned_by_account_first_item()
                        assert self.accountBillingPage.return_account_billing_policies_owned_by_account_first_item_product() in self.accountBillingPage.POLICY_LOBS
                        self.commons.validate_date(self.accountBillingPage.return_account_billing_policies_owned_by_account_first_item_effective_date())
                        self.commons.validate_date(self.accountBillingPage.return_account_billing_policies_owned_by_account_first_item_expiration_date())
                        if self.accountBillingPage.return_account_billing_customer_payment_summary_balance_value() != '$ 0,00':
                            self.accountBillingPage.go_to_account_billing_automatic_payments_tab()
                            self.accountBillingPage.check_presence_account_billing_automatic_payments_first_item()
                            assert self.accountBillingPage.return_account_billing_automatic_payments_first_item_lob() in self.accountBillingPage.POLICY_LOBS
                            assert self.accountBillingPage.return_account_billing_automatic_payments_first_item_status() in self.accountBillingPage.POLICY_STATUS
                            self.commons.validate_date(self.accountBillingPage.return_account_billing_automatic_payments_first_item_expiration_date())
                            print(self.accountBillingPage.return_account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link_text())
                            assert self.accountBillingPage.return_account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link_text() in self.accountBillingPage.ADD_AUTOMATIC_PAYMENT_LINKS
                            if self.accountBillingPage.return_account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link_text() == 'Configurar débitos automáticos':
                                assert "No adherido" in self.accountBillingPage.return_account_billing_automatic_payments_first_item_no_payment_information_text()
                                assert "a débito automático" in self.accountBillingPage.return_account_billing_automatic_payments_first_item_no_payment_information_text()
                            elif self.accountBillingPage.return_account_billing_automatic_payments_first_item_enable_disable_automatic_payment_link_text() == 'Desadherir débito automático':
                                assert self.accountBillingPage.return_account_billing_automatic_payments_first_item_payment_information_entity_text() in self.accountBillingPage.PAYMENT_ENITITES
                                if 'Débito en cuenta' in self.accountBillingPage.return_account_billing_automatic_payments_first_item_payment_information_text():
                                    assert 'CBU terminado en' in self.accountBillingPage.return_account_billing_automatic_payments_first_item_payment_information_text()
                                else:
                                    assert 'Tarjeta terminada en' in self.accountBillingPage.return_account_billing_automatic_payments_first_item_payment_information_text()
                elif not active_account:
                    assert self.accountBillingPage.return_account_billing_inactive_popup_title() == 'Cuenta no existente en sistema de facturación'
                    self.accountBillingPage.close_account_billing_inactive_popup()
                    assert self.accountBillingPage.return_account_billing_inactive_primary_payer_info_text() == 'La información del pagador principal estará disponible cuando se emita una póliza'
                    assert self.accountBillingPage.return_account_billing_inactive_no_billing_data_text() == 'No se encontraron datos de facturación para esta cuenta; consulte nuevamente en las próximas 24 horas'
                    self.accountBillingPage.go_to_account_billing_automatic_payments_tab()
                    assert self.accountBillingPage.return_account_billing_automatic_payments_no_invoices_info_text() == 'No hay flujos de factura en esta cuenta'

            self.logger.info("******************* test_smoke_account (" + str(account_number) + ") PASSED *******************")
            self.driver.close()
        except Exception as e:
            self.logger.error("******************* test_smoke_account (" + str(account_number) + ") FAILED *******************")
            self.commons.take_screenshot(request.node.name)
            self.driver.close()
            raise e

    # @pytest.mark.skip(reason="not needed")
    @pytest.mark.parametrize('poliza , pack',[
        ('4-65000000', 'null'),
        ('4-65000001', 'null'),
        ('4-65000002', 'null'),
        ('4-65000003', 'null'),
        ('4-65000004', 'null'),
        ('44-45000000', 'null'),
        ('44-45000003', 'null'),
        ('44-45000004', 'null'),
        ('4-65000095', 'null'),
    ])
    def test_smoke_policy_auto(self, setUp, environment, request, poliza, pack):
        try:
            self.driver = setUp
            self.entorno = environment
            self.commons = Commons(self.driver)
            self.loginPage = PageLogin(self.driver)
            self.driver.get(ReadConfig.getUrlEnvironment(self.entorno) + 'accounts')
            self.polizaAutoPage = PagePolizaAuto(self.driver)
            self.policyContactsPage = PagePolicyContacts(self.driver)
            self.policyNotesPage = PagePolicyNotes(self.driver)
            self.policyDocumentsPage = PagePolicyDocuments(self.driver)

            self.loginPage.login(ReadConfig.getUsername(), ReadConfig.getPassword())
            self.polizaAutoPage.go_to_poliza(ReadConfig.getUrlEnvironment(self.entorno), poliza)
            assert self.polizaAutoPage.return_poliza_title() == 'Automotores (' + poliza + ')'
            if pack != 'null':
                assert pack == self.polizaAutoPage.return_policy_pack_number()
            if self.polizaAutoPage.return_policy_type() == 'Automotores' or self.polizaAutoPage.return_policy_type() == 'Motovehículos':
                assert 'Vehículos' in self.polizaAutoPage.check_if_vehiculos_exist()
                self.polizaAutoPage.open_vehicles_dropdown()
                assert 'Marca' in self.polizaAutoPage.return_vehicles_table_marca_title()
                assert 'Modelo' in self.polizaAutoPage.return_vehicles_table_modelo_title()
                assert 'Año' in self.polizaAutoPage.return_vehicles_table_anio_title()
                assert 'Patente' in self.polizaAutoPage.return_vehicles_table_patente_title()
                assert 'Suma Aseg.' in self.polizaAutoPage.return_vehicles_table_suma_aseg_title()
                assert 'Plan de Cobertura' in self.polizaAutoPage.return_vehicles_table_plan_title()
                self.polizaAutoPage.open_close_vehicles_coverages_dropdown()
            elif self.polizaAutoPage.return_policy_type() == 'Registro de Conductores':
                assert 'Conductores cubiertos' in self.polizaAutoPage.check_if_vehiculos_exist()
                self.polizaAutoPage.open_drivers_dropdown()
                assert 'Nombre' in self.polizaAutoPage.return_registro_table_nombre_title()
                assert 'Fec. Nac.' in self.polizaAutoPage.return_registro_table_fecha_nacimiento_title()
                assert 'Identificación' in self.polizaAutoPage.return_registro_table_id_title()
                assert 'Permiso de conducir' in self.polizaAutoPage.return_registro_table_permiso_title()
                assert 'Categorías' in self.polizaAutoPage.return_registro_table_categoria_title()
                self.polizaAutoPage.open_close_drivers_coverages_dropdown()
            else:
                raise Exception("No se reconoce el tipo de póliza: "+ self.polizaAutoPage.return_policy_type())
            assert 'Transacciones de póliza' == self.polizaAutoPage.check_if_transacciones_exist()
            self.polizaAutoPage.open_transactions_dropdown()
            assert 'Número de póliza' == self.polizaAutoPage.return_transactions_table_policy_title()
            assert 'Endoso' == self.polizaAutoPage.return_transactions_table_endorse_title()
            assert 'Solicitud de trabajo' == self.polizaAutoPage.return_transactions_table_job_title()
            assert 'Estado de la transacción' == self.polizaAutoPage.return_transactions_table_status_title()
            assert 'Tipo' == self.polizaAutoPage.return_transactions_table_type_title()
            assert 'Estado de período' == self.polizaAutoPage.return_transactions_table_period_status_title()
            assert 'Prima' == self.polizaAutoPage.return_transactions_table_premium_title()
            assert 'Inicio de vigencia' == self.polizaAutoPage.return_transactions_table_effective_date_title()

            self.policyContactsPage.go_to_contactos()
            assert 'Contactos de póliza' in self.policyContactsPage.return_contact_policy_tab_title()
            assert 'Solo contactos asociados con esta póliza.' in self.policyContactsPage.return_contact_policy_tab_text()
            assert 'Contactos de cuenta' == self.policyContactsPage.return_contact_account_tab_title()
            assert 'Solo contactos asociados con esta cuenta.' in self.policyContactsPage.return_contact_account_tab_text()
            assert 'Contactos asociados' == self.policyContactsPage.return_asociated_contact_title()
            assert 'Estos contactos se encuentran en cuentas que tienen algún tipo de relación con la cuenta' in self.policyContactsPage.return_asociated_contact_tab_text()

            self.policyNotesPage.go_to_notes()
            assert 'Nota' in self.policyNotesPage.return_add_note_button_text()
            assert 'La creación de notas no genera actividades para el sector de suscripciones' in self.policyNotesPage.return_note_information_label_text()
            if self.policyNotesPage.return_number_of_notes() == '0':
                assert 'No hay notas asociadas con esta póliza.' in self.policyNotesPage.return_no_note_information_label_text()
            else:
                self.policyNotesPage.check_visibility_of_search_notes()

            self.policyDocumentsPage.go_to_policy_documents()
            if self.driver.execute_script("return window.innerWidth;") > 1200:
                assert self.policyDocumentsPage.return_upload_document_text_1200px() == 'Arrastrar y soltar los archivos acá o'
            else:
                assert self.policyDocumentsPage.return_upload_document_text_480px() == 'Toque para cargar'
            if self.policyDocumentsPage.return_number_of_documents() == '0':
                assert 'No hay documentos asociados con esta póliza' == self.policyDocumentsPage.return_no_documents_text()
            else:
                assert 'Buscar documentos' == self.policyDocumentsPage.return_documents_search_box_text()
                assert 'Nombre' == self.policyDocumentsPage.return_documents_table_header_name_text()
                assert 'Fecha de creación' == self.policyDocumentsPage.return_documents_table_header_date_text()
                assert 'Tipo de documento' == self.policyDocumentsPage.return_documents_table_header_type_text()
                assert 'Autor' == self.policyDocumentsPage.return_documents_table_header_author_text()

            self.logger.info("******************* test_smoke_policy (" + poliza + ") PASSED *******************")
            self.driver.close()
        except Exception as e:
            self.logger.error("******************* test_smoke_policy (" + poliza + ") FAILED *******************")
            self.commons.take_screenshot(request.node.name)
            self.driver.close()
            raise e

    # @pytest.mark.skip(reason="not needed")
    @pytest.mark.parametrize('claim_number', [
        ('4-3000000'),
        ('4-3000001'),
        ('4-3000002'),
        ('44-3000000'),
    ])
    def test_smoke_claim(self, setUp, environment, request, claim_number):
        try:
            self.driver = setUp
            self.entorno = environment
            self.commons = Commons(self.driver)
            self.loginPage = PageLogin(self.driver)
            self.driver.get(ReadConfig.getUrlEnvironment(self.entorno) + 'accounts')
            self.claimSummaryPage = PageClaimSummary(self.driver)

            self.loginPage.login(ReadConfig.getUsername(), ReadConfig.getPassword())
            self.claimSummaryPage.go_to_claim(ReadConfig.getUrlEnvironment(self.entorno), claim_number)
            assert self.claimSummaryPage.return_claim_summary_mosaic_text() == 'RESUMEN'
            assert self.claimSummaryPage.return_claim_notes_mosaic_text() == 'NOTAS'
            assert self.claimSummaryPage.return_claim_documents_mosaic_text() == 'DOCUMENTOS'
            assert self.claimSummaryPage.return_claim_payments_mosaic_text() == 'PAGOS'
            assert self.claimSummaryPage.return_claim_services_mosaic_text() == 'SERVICIOS'
            assert "Detalles del siniestro: " + claim_number in self.claimSummaryPage.return_claim_title_text()
            assert self.claimSummaryPage.return_claim_status_text() in self.claimSummaryPage.CLAIM_STATUS
            self.claimSummaryPage.check_claim_back_button_exists()
            assert self.claimSummaryPage.return_claim_loss_cause() in self.claimSummaryPage.CLAIM_LOSS_CAUSE
            assert self.claimSummaryPage.return_claim_date_of_loss_title() == 'Fecha y hora'
            assert self.claimSummaryPage.return_claim_reported_by_title() == 'Denunciante'
            assert self.claimSummaryPage.return_claim_loss_location_title() == 'Lugar'
            assert self.claimSummaryPage.return_claim_how_reported_title() == 'Reportado en'
            assert self.claimSummaryPage.return_claim_what_happened_title() == '¿Qué sucedió?'
            assert self.claimSummaryPage.return_claim_adjuster_title() == 'Tramitadores'
            assert self.claimSummaryPage.return_claim_involved_vehicles_title() == 'Vehículos involucrados'
            assert self.claimSummaryPage.return_claim_parties_involved_title() == 'Partes implicadas'
            if self.claimSummaryPage.check_if_claim_has_exposures():
                assert self.claimSummaryPage.return_claim_adjuster_table_name_column_title() == 'Nombre'
                assert self.claimSummaryPage.return_claim_adjuster_table_segment_column_title() == 'Segmento'
                assert self.claimSummaryPage.return_claim_adjuster_table_incident_column_title() == 'Incidente'
                assert self.claimSummaryPage.return_claim_adjuster_table_state_column_title() == 'Estado'
            else:
                assert self.claimSummaryPage.return_claim_adjuster_table_no_exposures_label_text() == 'No se encontraron exposiciones'
            self.claimSummaryPage.verify_claim_has_involved_vehicles()
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_make_column_title() == 'Marca'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_model_column_title() == 'Modelo'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_year_column_title() == 'Año'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_license_column_title() == 'Patente'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_loss_party_column_title() == 'Parte vinculada'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_damage_column_title() == 'Daños'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_damage_type_column_title() == 'Tipo de daño'
            assert self.claimSummaryPage.return_claim_involved_vehicles_table_first_item_loss_party_text() in self.claimSummaryPage.VEHICLE_LOSS_PARTY
            self.claimSummaryPage.verify_claim_has_parties_involved()
            assert self.claimSummaryPage.return_claim_parties_involved_table_name_column_title() == 'Nombre'
            assert self.claimSummaryPage.return_claim_parties_involved_table_involvement_column_title() == 'Implicación'
            assert self.claimSummaryPage.return_claim_first_party_involved_popup_name() == self.claimSummaryPage.return_claim_parties_involved_table_first_item_name_value_text()

            self.logger.info("******************* test_smoke_claim (" + claim_number + ") PASSED *******************")
            self.driver.close()
        except Exception as e:
            self.logger.error("******************* test_smoke_claim (" + claim_number + ") FAILED *******************")
            self.commons.take_screenshot(request.node.name)
            self.driver.close()
            raise e