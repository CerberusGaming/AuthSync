import datetime
from AuthSync.App.Storage import Session
from AuthSync.Joomla.Models.Groups import Group, GroupMap
from AuthSync.Joomla.Models.Users import User


class JoomlaGroup(object):
    ID = int()
    Title = str()
    Parent = object()

    def __init__(self, group: Group):
        self.ID = group.id
        self.__left__ = group.lft
        self.__right__ = group.rgt
        self.__parent_id__ = group.parent_id
        self.Title = group.title

    def get_param(self, param):
        param = "__" + param + "__"
        value = getattr(self, param)
        return value


class JoomlaUser(object):
    ID = int()
    Name = str()
    Username = str()
    EMail = str()
    Password = str()
    Block = bool()
    SendEmail = bool()
    RegisterDate = datetime.datetime
    LastVisitDate = datetime.datetime
    Activation = str()
    Params = str()
    LastResetTime = datetime.datetime
    ResetCount = int()
    OTPKey = str()
    OTEP = str()
    RequireReset = bool()
    Groups = []

    def __init__(self, user: User):
        # Set Direct mapping
        self.ID = user.id
        self.Name = user.name
        self.Username = user.username
        self.EMail = user.email
        self.Password = user.password
        self.RegisterDate = user.registerDate
        self.LastVisitDate = user.lastvisitDate
        self.Activation = user.activation
        self.Params = user.params
        self.LastResetTime = user.lastResetTime
        self.ResetCount = user.resetCount
        self.OTPKey = user.otpKey
        self.OTEP = user.otep
        # Set Block status
        if int(user.block) > 0:
            self.Block = True
        else:
            self.Block = False
        # Set Send Email
        if int(user.sendEmail) > 0:
            self.SendEmail = True
        else:
            self.SendEmail = False
        # Set Requires Reset status
        if int(user.requireReset) > 0:
            self.RequireReset = True
        else:
            self.RequireReset = False


class Joomla:
    def __init__(self, init=False):
        self.init = init
        if init:
            self.sync()

    def sync(self):
        self.Users = {}
        self.Groups = {}
        self.GroupMap = {}

        for group in self.__get_groups__():
            group = JoomlaGroup(group)
            self.Groups[group.ID] = group

        for id in self.Groups.keys():
            parent = self.Groups[id].get_param("parent_id")
            if parent == 0:
                parent = None
            else:
                parent = self.Groups[parent]
            self.Groups[id].Parent = parent

        for mapping in self.__get_groupmap__():
            if mapping.user_id not in self.GroupMap.keys():
                self.GroupMap[mapping.user_id] = []
            self.GroupMap[mapping.user_id].append(mapping.group_id)

        for user in self.__get_users__():
            user = JoomlaUser(user)
            groups = []
            for group in self.GroupMap[int(user.ID)]:
                groups.append(self.Groups[group])
            user.Groups = groups
            self.Users[user.ID] = user
        self.init = True

    def __get_users__(self):
        session = Session()
        users = session.query(User).all()
        session.close()
        return users

    def __get_groups__(self):
        session = Session()
        groups = session.query(Group).all()
        session.close()
        return groups

    def __get_groupmap__(self):
        session = Session()
        groupmap = session.query(GroupMap).all()
        session.close()
        return groupmap
