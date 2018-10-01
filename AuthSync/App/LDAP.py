from AuthSync import AppConfig
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES

LDAPConn = Connection(
    Server(
        host=AppConfig.get("LDAP_HOST", "localhost"),
        port=AppConfig.getint("LDAP_PORT", "389"),
        use_ssl=AppConfig.getbool("LDAP_SSL", False),
        tls=AppConfig.getbool("LDAP_TLS", False),
        get_info=ALL
    ),
    user=AppConfig.get("LDAP_BINDDN", None),
    password=AppConfig.get("LDAP_BINDPASS", None),
    auto_bind=True,
    return_empty_attributes=True
)
LDAPAttrs = ALL_ATTRIBUTES
