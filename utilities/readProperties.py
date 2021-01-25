import configparser

config=configparser.RawConfigParser()
config.read("../dp10_automation/configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getUrlEnvironment(entorno):
        environment_url = config.get('environments', entorno)
        return environment_url




