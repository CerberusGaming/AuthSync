from AuthSync.Joomla import Joomla
from AuthSync.LDAP import LDAP

async_timer = 1


class GroupSync:
    def __init__(self):
        if Joomla.init:
            self.create_groups()
            self.delete_groups()
            print('ping')

    def create_groups(self):
        joomla_groups = Joomla.Groups
        for group in joomla_groups:
            group = joomla_groups[group]
            ldap_group = LDAP.read_group("(cn=" + group.Title + ")")
            if ldap_group is None:
                LDAP.create_group(group.Title, group.ID)
            elif ldap_group[0].JoomlaID is None:
                print(LDAP.update_group(ldap_group[0].DN, {'joomlaID': group.ID}))
            else:
                pass

    def delete_groups(self):
        print(Joomla.Groups.keys())
        for group in LDAP.read_group():
            if group.JoomlaID in Joomla.Groups.keys():
                print(group)
        pass