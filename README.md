# GuideWire Digital Portal Testing Automation

Respositorio para almacenar los scripts de automatización de pruebas para los distintos módulos de GuideWire Digital.

Deberán generarse carpetas por para organizar los scripts.

### Instalacion

1. Dependencias globales
    * Instalar [python](https://www.python.org/downloads/) 3.7.4
    * Instalar [pip](https://pip.pypa.io/en/stable/installing/) para instalacion de librerias
    
2. Proyecto	
	* Instalacion de librerias requeridas:
	```$ pip install -r requirements.txt```

### Ejecucion de scripts:  

-v agrega mas información en el output.  
-n designa la cantidad de test en paralelo a ejecutarse.  
--html=reports\report.html genera reporte html en carpeta /reports del proyecto.  
--env para indicar por linea de comando en que ambiente ejecutar los scripts (UAT/DEV/PROD/TE). Si no se indica, por defecto se ejecuta en UAT  
--alluredir=./allureReport se utiliza para indicar la carpeta donde se guardan los datos necesarios para el repote de allure  

*  Ejecución modulo completo
    ```$ pytest -v tests/main.py```

*  Ejecución modulo completo en ambiente DEV
    ```$ pytest -v --env=DEV tests/main.py```

*  Ejecucion de tests en paralelo:
    ```$ pytest -v -n 2 tests/main.py```

*  Generacion de reporte allure:
    ```$ pytest -v --alluredir=./allureReport tests/main.py```

*  Generacion de reporte html:
    ```$ pytest -v --html=reports\report.html tests/main.py```

*  Ejecucion de test especifico dentro de un modulo:
    ```$ pytest -v tests/main.py::TestMain::test_X```