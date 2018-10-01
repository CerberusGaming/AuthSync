import datetime


class GroupFieldMap(object):
    # LDAP attributes
    DN = ['dn']
    # naming attributes
    Name = ['cn', 'name', 'sAMAccountName']
    # Group Membership
    MemberOf = ['memberOf']
    # Account Params
    GUID = ['objectGUID']
    SID = ['objectSid']
    # Stats
    WhenCreated = ['whenCreated']
    WhenChanged = ['whenChanged']


class Group(object):
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
        pass
