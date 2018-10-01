from AuthSync.App.LDAP import LDAPConn
from AuthSync import AppConfig


class LDAPUser:
    pass


class LDAPGroup:
    pass


class LDAP:
    def __init__(self):
        self.__ldap__ = LDAPConn
        self.__basedn__ = AppConfig.get("LDAP_BASEDN", None)
        self.__userdn__ = AppConfig.get("LDAP_USERBASE", None)
        self.__groupdn__ = AppConfig.get("LDAP_GROUPBASE", None)

    def create_user(self):
        pass

    def read_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass

    def create_group(self):
        pass

    def read_group(self):
        pass

    def update_group(self):
        pass

    def delete_group(self):
        pass
