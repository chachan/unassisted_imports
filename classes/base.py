''' Base Class '''
from abc import ABCMeta, abstractmethod

class ClassBase(metaclass=ABCMeta):
    ''' does nothing '''

    @abstractmethod
    def action(self):
        ''' does nothing '''

    def another_action(self):
        ''' does nothing '''
