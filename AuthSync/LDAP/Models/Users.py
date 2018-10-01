import datetime


class UserFieldMap(object):
    # LDAP name
    DN = ['dn']
    # Descriptive Fields
    DisplayName = ['cn', 'displayName', 'name']
    Username = ['sAMAccountName']
    EMail = ['mail']
    # Identifiers
    GUID = ['objectGUID']
    SID = ['objectSid']
    UPN = ['userPrincipalName']
    UAC = ['userAccountControl']
    PrimaryGroup = ['primaryGroupID']
    # Group membership
    MemberOf = ['memberOf']
    # Joomla Fields
    JoomlaID = ['joomlaID']
    # Stats
    WhenCreated = ['whenCreated']
    WhenChanged = ['whenChanged']
    LastLogon = ['lastLogon']
    LogonCount = ['logonCount']
    LastLogoff = ['lastLogoff']
    PwdLastSet = ['pwdLastSet']
    BadPwdTime = ['badPasswordTime']
    BadPwdCount = ['badPwdCount']


class User(object):
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
        pass
