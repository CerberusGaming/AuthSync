from AuthSync.Joomla import Joomla
from AuthSync.LDAP import LDAP

async_timer = 30


class DisableUser:
    def __init__(self):
        if Joomla.init:
            self.uac_enabled = 512
            self.uac_disabled = 514
            self.enable_disable_users()

    def enable_disable_users(self):
        for user in LDAP.read_user():
            user_dn = user.DN.value
            user_jid = user.JoomlaID.value
            user_uac = user.UAC.value
            if user_jid is not None and user_uac in [self.uac_disabled, self.uac_enabled]:
                joomla_user = Joomla.Users[user_jid]
                if joomla_user.Block:
                    LDAP.update_user(user_dn, {'userAccountControl': self.uac_disabled})
                else:
                    LDAP.update_user(user_dn, {'userAccountControl': self.uac_enabled})
