from AuthSync.LDAP import LDAP
from AuthSync.Joomla import Joomla

Joomla.sync()
for user_id, user_obj in Joomla.Users.items():
    print(user_id)
    print(user_obj)