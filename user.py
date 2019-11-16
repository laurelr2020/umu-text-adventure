
class User():
    @property
    def name(self):
        '''Name of current player'''
        return self._name;

    @name.setter
    def name(self, name):
        self._name = name