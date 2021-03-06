FROM python:3.7-slim

# MySql / MariaDB Config
ENV MYSQL_USER "mysql_user"
ENV MYSQL_PASSWORD "mysql_password"
ENV MYSQL_HOST "mysql_host"
ENV MYSQL_PORT "3306"
ENV MYSQL_DATABASE ""
ENV MYSQL_PREFIX "_"

# LDAP Config
ENV LDAP_HOST "ldap_host"
ENV LDAP_PORT "389"
ENV LDAP_SSL "false"
ENV LDAP_TLS "false"

ENV LDAP_BINDDN ""
ENV LDAP_BINDPASS ""

ENV LDAP_BASEDN ""

ENV LDAP_USERBASE ""
ENV LDAP_USERFILTER ""

ENV LDAP_GROUPBASE ""
ENV LDAP_GROUPFILTER ""

ENV LOG_LEVEL ""

WORKDIR /usr/src/app
RUN apt-get update && apt-get -y install git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/CerberusGaming/AuthSync.git .

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
