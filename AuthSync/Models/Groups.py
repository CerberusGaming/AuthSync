from . import Base
from AuthSync import AppConfig
from sqlalchemy import Column, Index, String, text
from sqlalchemy.dialects.mysql import INTEGER


class Group(Base):
    __tablename__ = str(AppConfig.get('MYSQL_PREFIX') + 'usergroups')
    __table_args__ = (
        Index('idx_usergroup_parent_title_lookup', 'parent_id', 'title', unique=True),
        Index('idx_usergroup_nested_set_lookup', 'lft', 'rgt')
    )

    id = Column(INTEGER(10), primary_key=True)
    parent_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("0"))
    lft = Column(INTEGER(11), nullable=False, server_default=text("0"))
    rgt = Column(INTEGER(11), nullable=False, server_default=text("0"))
    title = Column(String(100, 'utf8mb4_unicode_ci'), nullable=False, index=True, server_default=text("''"))


class GroupMap(Base):
    __tablename__ = str(AppConfig.get('MYSQL_PREFIX') + 'user_usergroup_map')

    user_id = Column(INTEGER(10), primary_key=True, nullable=False, server_default=text("0"))
    group_id = Column(INTEGER(10), primary_key=True, nullable=False, server_default=text("0"))
