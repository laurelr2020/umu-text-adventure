
class User():
    @property
    def name(self):
        '''Name of current player'''
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def purple_raider(self):
        '''Identifies as a member of the University of Mount Union'''
        return self._purple_raider

    @purple_raider.setter
    def purple_raider(self, attend_umu):
        self._purple_raider = bool('yes' in attend_umu.lower())