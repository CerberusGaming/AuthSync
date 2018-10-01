from AuthSync.LDAP.Models.Groups import Group
from AuthSync.LDAP.Models.Users import User
from AuthSync.App.LDAP import LDAPConn, LDAPAttrs
from AuthSync import AppConfig


class LDAP:
    def __init__(self):
        # LDAP base objects
        self.__attrs__ = LDAPAttrs
        self.__ldap__ = LDAPConn

        # LDAP base DN
        self.__basedn__ = str(AppConfig.get("LDAP_BASEDN", "")).lstrip("\"").rstrip("\"")

        # LDAP User DN and base filter
        self.__userdn__ = str(AppConfig.get("LDAP_USERBASE", "")).lstrip("\"").rstrip("\"")
        self.__userfilter__ = str(AppConfig.get("LDAP_USERFILTER", "()"))

        # LDAP Group DN and filter
        self.__groupdn__ = str(AppConfig.get("LDAP_GROUPBASE", "")).lstrip("\"").rstrip("\"")
        self.__groupfilter__ = str(AppConfig.get("LDAP_GROUPFILTER", "()"))

    def create_user(self):
        pass

    def read_user(self, filter: str = None):
        if filter is not None:
            filter = "(&" + filter + self.__userfilter__ + ")"
        else:
            filter = self.__userfilter__
        if self.__ldap__.search(self.__userdn__, filter, attributes=self.__attrs__):
            return self.__ldap__.response
        else:
            return None

    def update_user(self):
        pass

    def delete_user(self):
        pass

    def create_group(self):
        pass

    def read_group(self, filter: str = None):
        if filter is not None:
            filter = "(&" + filter + self.__groupfilter__ + ")"
        else:
            filter = self.__groupfilter__
        if self.__ldap__.search(self.__groupdn__, filter, attributes=self.__attrs__):
            return self.__ldap__.response
        else:
            return None

    def update_group(self):
        pass

    def delete_group(self):
        pass
