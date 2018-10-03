import datetime
from AuthSync.LDAP.Models.Fields import Field


class User(object):
    _mapping = {
        'DN': {
            'loc': '',
            'get': 'dn',
            'put': ['dn']
        },

        'DisplayName': {
            'loc': 'attributes',
            'get': 'displayName',
            'put': ['cn', 'displayName', 'name']
        },

        'Username': {
            'loc': 'attributes',
            'get': 'sAMAccountName',
            'put': ['sAMAccountName']
        },

        'EMail': {
            'loc': 'attributes',
            'get': 'mail',
            'put': ['mail']
        },

        'GUID': {
            'loc': 'attributes',
            'get': 'objectGUID',
            'put': ['objectGUID']
        },

        'SID': {
            'loc': 'attributes',
            'get': 'objectSid',
            'put': ['objectSid']
        },

        'UPN': {
            'loc': 'attributes',
            'get': 'userPrincipalName',
            'put': ['userPrincipalName']
        },

        'UAC': {
            'loc': 'attributes',
            'get': 'userAccountControl',
            'put': ['userAccountControl']
        },

        'PrimaryGroup': {
            'loc': 'attributes',
            'get': 'primaryGroupID',
            'put': ['primaryGroupID']
        },

        'MemberOf': {
            'loc': 'attributes',
            'get': 'memberOf',
            'put': ['memberOf']
        },

        'JoomlaID': {
            'loc': 'attributes',
            'get': 'joomlaID',
            'put': ['joomlaID']
        },

        'WhenCreated': {
            'loc': 'attributes',
            'get': 'whenCreated',
            'put': ['whenCreated']
        },

        'WhenChanged': {
            'loc': 'attributes',
            'get': 'whenChanged',
            'put': ['whenChanged']
        },

        'LastLogon': {
            'loc': 'attributes',
            'get': 'lastLogon',
            'put': ['lastLogon']
        },

        'LogonCount': {
            'loc': 'attributes',
            'get': 'logonCount',
            'put': ['logonCount']
        },

        'LastLogoff': {
            'loc': 'attributes',
            'get': 'lastLogoff',
            'put': ['lastLogoff']
        },

        'PwdLastSet': {
            'loc': 'attributes',
            'get': 'pwdLastSet',
            'put': ['pwdLastSet']
        },

        'BadPwdTime': {
            'loc': 'attributes',
            'get': 'badPasswordTime',
            'put': ['badPasswordTime']
        },

        'BadPwdCount': {
            'loc': 'attributes',
            'get': 'badPwdCount',
            'put': ['badPwdCount']
        },
    }

    # LDAP name
    DN = str()
    CN = str()
    # Descriptive Fields
    DisplayName = str()
    FullName = str()
    Username = str()
    EMail = str()
    # Identifiers
    GUID = str()
    SID = str()
    UPN = str()
    UAC = int()
    PrimaryGroup = int()
    # Group membership
    MemberOf = list()
    # Joomla Fields
    JoomlaID = int()

    # Stats
    WhenCreated = datetime.datetime
    WhenChanged = datetime.datetime
    LastLogon = datetime.datetime
    LogonCount = int()
    LastLogoff = datetime.datetime
    PwdLastSet = datetime.datetime
    BadPwdTime = datetime.datetime
    BadPwdCount = int()

    def __init__(self, user):
        # Clean raw data (smaller object size, unused keys)
        for key in list(user.keys()):
            if 'raw' in str(key).lower():
                del user[key]
        self.raw = user

        # Map parameters
        for field, params in self._mapping.items():
            value = self.raw.copy()
            if params['loc'] == '':
                pass
            else:
                for path in params['loc'].split('.'):
                    if path in value.keys():
                        value = value[path]
            if params['get'] in value.keys():
                value = value[params['get']]
            else:
                value = None
            setattr(self, field, Field(params['get'], params['put'], value))

    # Return string-casted raw dictionary for debug use
    def __str__(self):
        return str(self.raw)
