from AuthSync.Joomla import Joomla
from AuthSync.LDAP import LDAP

async_timer = 60


class GroupSync:
    def __init__(self):
        if Joomla.init:
            self._joomla_ldap_groups = []
            ldap_groups = LDAP.read_group("(joomlaID=*)")
            if ldap_groups is not None:
                for group in ldap_groups:
                    if group is not None:
                        self._joomla_ldap_groups.append(group.DN.value)
            self.create_groups()
            self.delete_groups()
            self.update_users()
            self.map_users()
            self.demap_users()

    def create_groups(self):
        joomla_groups = Joomla.Groups
        for group in joomla_groups:
            group = joomla_groups[group]
            ldap_group = LDAP.read_group("(cn=" + group.Title + ")")
            if ldap_group is None:
                LDAP.create_group(group.Title, group.ID)
            elif ldap_group[0].JoomlaID is None:
                print(LDAP.update_group(ldap_group[0].DN.value, {'joomlaID': group.ID}))

    def delete_groups(self):
        for group in LDAP.read_group():
            if group.JoomlaID.value not in list(Joomla.Groups.keys()):
                LDAP.delete_group(group.DN.value)

    def update_users(self):
        for user_id, user_obj in Joomla.Users.items():
            if LDAP.read_user("(joomlaID=" + str(user_id) + ")") is None:
                ldap_user = LDAP.read_user("(sAMAccountName=" + str(user_obj.Username) + ")")
                if ldap_user is not None and len(ldap_user) == 1:
                    ldap_user = ldap_user[0]
                    LDAP.update_user(ldap_user.DN.value, {'joomlaID': user_obj.ID})

    def map_users(self):
        for user_id, user_groups in Joomla.GroupMap.items():
            ldap_user = LDAP.read_user("(joomlaID=" + str(user_id) + ")")
            if ldap_user is not None and len(ldap_user) == 1:
                ldap_user = ldap_user[0]
                ldap_user_dn = ldap_user.DN.value
                ldap_user_groups = ldap_user.MemberOf.value
                if ldap_user_groups is None:
                    ldap_user_groups = []
                for group_id in user_groups:
                    ldap_group = LDAP.read_group("(joomlaID=" + str(group_id) + ")")
                    if ldap_group is not None and len(ldap_group) == 1:
                        ldap_group = ldap_group[0]
                        ldap_group_dn = ldap_group.DN.value
                        if ldap_group_dn in self._joomla_ldap_groups:
                            if ldap_group_dn not in ldap_user_groups:
                                LDAP.add_user_group(ldap_user_dn, ldap_group_dn)

    def demap_users(self):
        for user_id, user_groups in Joomla.GroupMap.items():
            ldap_user = LDAP.read_user("(joomlaID=" + str(user_id) + ")")
            if ldap_user is not None and len(ldap_user) == 1:
                ldap_user = ldap_user[0]
                ldap_user_dn = ldap_user.DN.value

                ldap_user_groups = set(ldap_user.MemberOf.value) - set(self._joomla_ldap_groups)
                ldap_user_groups = set(ldap_user.MemberOf.value) - ldap_user_groups
                ldap_correct_groups = []
                for group_id in user_groups:
                    ldap_group = LDAP.read_group("(joomlaID=" + str(group_id) + ")")
                    if ldap_group is not None:
                        ldap_correct_groups.append(ldap_group[0].DN.value)
                ldap_correct_groups = set(ldap_correct_groups)
                ldap_delete_groups = list(ldap_user_groups - ldap_correct_groups)

                if len(ldap_delete_groups) != 0:
                    for delete_group in ldap_delete_groups:
                        LDAP.delete_user_group(ldap_user_dn, delete_group)
