import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setUp(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        option = Options()
        option.add_argument("--headless")
        option.add_argument('--no-sandbox')
        option.add_argument("--window-size=1220,800")
        driver = webdriver.Chrome(executable_path='../dp10_automation/chromedriver', options=option)
    return driver

@pytest.fixture()
def environment(env):
    if env == 'DEV':
        entorno = 'DEV'
    elif env == 'TE':
        entorno = 'TE'
    elif env == 'PROD':
        entorno = 'PROD'
    else:
        entorno = 'UAT'
    return entorno


def pytest_addoption(parser): # obtiene el valor de la linea de comando
    parser.addoption("--browser")
    parser.addoption("--env")

@pytest.fixture()
def browser(request):  # retorna el valor del browser al setup
    return request.config.getoption("--browser")

@pytest.fixture()
def env(request):  # retorna el valor del environment al setup
    return request.config.getoption("--env")


########### pytest HTML Report ################

# Agrega informacion de environment en el rerpote HTML
def pytest_configure(config):
    config._metadata['Project Name'] = 'Digital Portal'
    config._metadata['Module Name'] = 'Producer'
    config._metadata['Tester'] = 'Testcac'

# Elimina y modifica informacion en html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)