class Field(object):
    get = str()
    update = list()
    value = None

    def __init__(self, get, update, value):
        self.get = get
        self.update = update
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
