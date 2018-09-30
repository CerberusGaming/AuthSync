from AuthSync import AppConfig
from ldap3 import Server, Connection, ALL

__host = AppConfig.get("LDAP_HOST")
__port = AppConfig.get("LDAP_PORT")
__use_ssl = AppConfig.getbool("LDAP_SSL", False)
__tls = AppConfig.getbool("LDAP_TLS", False)
LDAPServer = Server(host=__host, port=__port, use_ssl=__use_ssl, tls=__tls, get_info=ALL)

__user = AppConfig.get("LDAP_BINDDN", None)
__password = AppConfig.get("LDAP_BINDPASS", None)
LDAPConn = Connection(LDAPServer, __user, __password)
