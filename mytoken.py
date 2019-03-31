class MyToken:
    def __init__(self, token):
        self.type = token.type
        self.value = token.value
        self.lineno = token.lineno
        self.lexpos = token.lexpos
        self._data = token.__dict__

    def __str__(self):
        return "[{} {} {}]".format(self.type, self.value, self.lexpos)

    def __repr__(self):
        return self.__str__()