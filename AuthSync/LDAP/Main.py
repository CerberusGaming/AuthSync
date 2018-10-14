from AuthSync.LDAP.Models.Groups import Group
from AuthSync.LDAP.Models.Users import User
from AuthSync.App.LDAP import LDAPConn, LDAPAttrs
from AuthSync import AppConfig
from ldap3 import MODIFY_REPLACE
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups
from ldap3.extend.microsoft.removeMembersFromGroups import ad_remove_members_from_groups


class LDAP:
    def __init__(self):
        # LDAP base objects
        self.__attrs__ = LDAPAttrs
        self.__ldap__ = LDAPConn

        # LDAP base DN
        self.__basedn__ = str(AppConfig.get("LDAP_BASEDN", "")).lstrip("\"").rstrip("\"")

        # LDAP User DN and base filter
        self.__userdn__ = str(AppConfig.get("LDAP_USERBASE", "")).lstrip("\"").rstrip("\"")
        self.__userfilter__ = str(AppConfig.get("LDAP_USERFILTER", "()")).lstrip("\"").rstrip("\"")

        # LDAP Group DN and filter
        self.__groupdn__ = str(AppConfig.get("LDAP_GROUPBASE", "")).lstrip("\"").rstrip("\"")
        self.__groupfilter__ = str(AppConfig.get("LDAP_GROUPFILTER", "()")).lstrip("\"").rstrip("\"")

        self.__bind_sid__ = self.__get_bind_user_sid__()

    def __get_bind_user_sid__(self):
        username = self.__ldap__.user
        self.__ldap__.search(self.__basedn__, "(sAMAccountName=" + username + ")", attributes='objectsid')
        entries = self.__ldap__.entries
        if len(entries) > 0:
            return entries[0].objectsid
        else:
            return None

    def create_user(self):
        pass

    def read_user(self, filter: str = None):
        users = []
        if filter is not None:
            filter = "(&" + filter + self.__userfilter__ + ")"
        else:
            filter = self.__userfilter__
        if self.__ldap__.search(self.__userdn__, filter, attributes=self.__attrs__):
            for entry in self.__ldap__.response:
                users.append(User(entry))
            return users
        else:
            return None

    def update_user(self, dn, changes):
        _changes = {}
        for field, value in changes.items():
            if not isinstance(value, list):
                value = [value]
            _changes[field] = (MODIFY_REPLACE, value)
        response = self.__ldap__.modify(dn, _changes)
        return response

    def delete_user(self, dn):
        response = self.__ldap__.delete(dn)
        return response

    def create_group(self, name, joomla_id=None):
        attrs = {
            'cn': str(name),
            'groupType': '-2147483646',
            'objectCategory': 'CN=Group,CN=Schema,CN=Configuration,' + str(self.__basedn__),
        }
        if joomla_id is not None:
            attrs['joomlaID'] = str(joomla_id)
        new_group = self.__ldap__.add(
            dn=str('cn=' + str(name) + ',' + str(self.__groupdn__)),
            object_class=['group'],
            attributes=attrs
        )
        return new_group

    def read_group(self, filter: str = None):
        groups = []
        if filter is not None:
            filter = "(&" + filter + self.__groupfilter__ + ")"
        else:
            filter = self.__groupfilter__
        if self.__ldap__.search(self.__groupdn__, filter, attributes=self.__attrs__):
            for entry in self.__ldap__.response:
                groups.append(Group(entry))

            return groups
        else:
            return None

    def update_group(self, dn, changes):
        _changes = {}
        for field, value in changes.items():
            if not isinstance(value, list):
                value = [value]
            _changes[field] = (MODIFY_REPLACE, value)
        response = self.__ldap__.modify(dn, _changes)
        return response

    def delete_group(self, dn):
        response = self.__ldap__.delete(dn)
        return response

    def add_user_group(self, user_dn, group_dn):
        response = ad_add_members_to_groups(self.__ldap__, user_dn, group_dn)
        return response

    def delete_user_group(self, user_dn, group_dn):
        pass
