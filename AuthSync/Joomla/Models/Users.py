from . import Base
from AuthSync import AppConfig
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMTEXT, TINYINT


class User(Base):
    __tablename__ = str(AppConfig.get('MYSQL_PREFIX') + 'users')

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(400, 'utf8mb4_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    username = Column(String(150, 'utf8mb4_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    email = Column(String(100, 'utf8mb4_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    password = Column(String(100, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    block = Column(TINYINT(4), nullable=False, index=True, server_default=text("0"))
    sendEmail = Column(TINYINT(4), server_default=text("0"))
    registerDate = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    lastvisitDate = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    activation = Column(String(100, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    params = Column(MEDIUMTEXT, nullable=False)
    lastResetTime = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    resetCount = Column(INTEGER(11), nullable=False, server_default=text("0"))
    otpKey = Column(String(1000, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    otep = Column(String(1000, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    requireReset = Column(TINYINT(4), nullable=False, server_default=text("0"))
