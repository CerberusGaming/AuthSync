import datetime
from AuthSync.LDAP.Models.Fields import Field


class Group(object):
    _mapping = {
        'DN': {
            'loc': '',
            'get': 'dn',
            'put': ['dn']
        },

        'Name': {
            'loc': 'attributes',
            'get': 'cn',
            'put': ['cn', 'name', 'sAMAccountName']
        },

        'MemberOf': {
            'loc': 'attributes',
            'get': 'memberOf',
            'put': ['memberOf']
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

        'JoomlaID':{
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
        }
    }

    # LDAP attributes
    DN = str()
    CN = str()
    # naming attributes
    Name = str()
    # Group Membership
    MemberOf = list()
    # Account Params
    GUID = str()
    SID = str()
    # Stats
    WhenCreated = datetime.datetime
    WhenChanged = datetime.datetime

    def __init__(self, group):
        # Clean raw data (smaller object size, unused keys)
        for key in list(group.keys()):
            if 'raw' in str(key).lower():
                del group[key]
        self.raw = group

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
